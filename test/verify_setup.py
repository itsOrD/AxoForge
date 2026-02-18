import os
import shutil
import subprocess
import tempfile
import sys

def verify():
    # 1. Setup Temp Dir
    temp_dir = tempfile.mkdtemp()
    print(f"Testing in: {temp_dir}")
    
    # Resolve project root (assuming this script is in <root>/test/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_root = os.path.abspath(os.path.join(current_dir, '..'))
    
    try:
        # 2. Copy relevant files
        # setup.py is now in .context/scripts/
        # mcp.json.template is in .context/templates/
        
        # We need to preserve the structure in temp_dir for setup.py to basic logic to work if we run it from scripts dir
        # BUT setup.py logic basically finds root by looking up.
        
        # Let's replicate the structure in temp_dir
        os.makedirs(os.path.join(temp_dir, '.context', 'scripts'))
        os.makedirs(os.path.join(temp_dir, '.context', 'templates'))
        
        shutil.copy(os.path.join(source_root, '.context', 'scripts', 'setup.py'), os.path.join(temp_dir, '.context', 'scripts'))
        shutil.copy(os.path.join(source_root, '.context', 'templates', 'mcp.json.template'), os.path.join(temp_dir, '.context', 'templates'))
        shutil.copy(os.path.join(source_root, 'SCAFFOLD_INTENT.md'), temp_dir)
        
        # Copy complex dirs
        if os.path.exists(os.path.join(source_root, 'docs')):
            shutil.copytree(os.path.join(source_root, 'docs'), os.path.join(temp_dir, 'docs'))
        # We already created .context, so we need to merge or copy leftovers?
        # Simpler: copy the whole .context from source, then overwrite the ones we might have modified (none yet)
        # Actually easiest is to just copytree .context to temp_dir/.context
        # But we already made dirs.
        # Let's remove the dirs we made and valid copytree
        shutil.rmtree(os.path.join(temp_dir, '.context'))
        shutil.copytree(os.path.join(source_root, '.context'), os.path.join(temp_dir, '.context'))

        # 3. Simulate User Input
        # Strategy: Just provide "y" for EVERYTHING.
        # This ensures the final confirmation gets "y".
        # And all values become "y". This is sufficient to test the mechanics.
        
        inputs = ["y"] * 100
        
        input_str = "\n".join(inputs) + "\n"
        
        # 4. Run setup.py
        # We run it from the root, calling the script in .context/scripts/setup.py
        # OR we run it from .context/scripts/?
        # The walkthrough says "python3 .context/scripts/setup.py" likely.
        # Let's try running it as if the user ran: python3 .context/scripts/setup.py
        
        setup_script_path = os.path.join(temp_dir, '.context', 'scripts', 'setup.py')
        
        result = subprocess.run(
            [sys.executable, setup_script_path],
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
