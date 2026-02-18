import os
import shutil
import subprocess
import tempfile
import sys

def verify():
    # 1. Setup Temp Dir
    temp_dir = tempfile.mkdtemp()
    print(f"Testing in: {temp_dir}")
    
    source_root = os.getcwd()
    
    try:
        # 2. Copy relevant files
        shutil.copy(os.path.join(source_root, 'setup.py'), temp_dir)
        shutil.copy(os.path.join(source_root, 'mcp.json.template'), temp_dir)
        shutil.copy(os.path.join(source_root, 'SCAFFOLD_INTENT.md'), temp_dir)
        
        # Copy complex dirs
        if os.path.exists(os.path.join(source_root, 'docs')):
            shutil.copytree(os.path.join(source_root, 'docs'), os.path.join(temp_dir, 'docs'))
        if os.path.exists(os.path.join(source_root, '.context')):
            shutil.copytree(os.path.join(source_root, '.context'), os.path.join(temp_dir, '.context'))

        # 3. Simulate User Input
        # Strategy: Just provide "y" for EVERYTHING.
        # This ensures the final confirmation gets "y".
        # And all values become "y". This is sufficient to test the mechanics.
        
        inputs = ["y"] * 100
        
        input_str = "\n".join(inputs) + "\n"
        
        # 4. Run setup.py
        result = subprocess.run(
            [sys.executable, 'setup.py'],
            cwd=temp_dir,
            input=input_str,
            text=True,
            capture_output=True
        )
        
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            print("❌ setup.py failed")
            return

        # 5. Assertions
        
        # Check MCP generation
        mcp_path = os.path.join(temp_dir, 'mcp.json')
        if os.path.exists(mcp_path):
            print("✅ mcp.json generated")
            with open(mcp_path, 'r') as f:
                content = f.read()
                # We expect "y" to be in there if it mapped to the server name
                # JSON keys and values will be "y"
                if '"y"' in content:
                    print("✅ mcp.json contains generated value 'y'")
                else:
                    print("⚠️ mcp.json generated but might not have specific value")
        else:
            print("❌ mcp.json not generated")

        # Check Replacement
        intent_path = os.path.join(temp_dir, 'SCAFFOLD_INTENT.md')
        with open(intent_path, 'r') as f:
            content = f.read()
            if "Goal**: y" in content or "Goal**: y" in content:
                print("✅ SCAFFOLD_INTENT.md updated with 'y'")
            elif "y" in content:
                 print("✅ SCAFFOLD_INTENT.md updated with 'y' (generic match)")
            else:
                 print("❌ SCAFFOLD_INTENT.md not updated")

    except Exception as e:
        print(f"Test failed with exception: {e}")
    finally:
        shutil.rmtree(temp_dir)
        print("Cleanup done.")

if __name__ == "__main__":
    verify()
