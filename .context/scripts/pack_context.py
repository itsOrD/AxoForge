import os
import sys

# Files to include in the packed context, in order of importance
CONTEXT_FILES = [
    "SCAFFOLD_INTENT.md",
    ".context/rules/coding.md",
    "docs/MCP.md",
    "docs/SKILLS.md",
    "docs/ARCHITECTURE.md" # If it exists
]

def pack_context():
    """Reads key files and concatenates them."""
    project_root = os.getcwd()
    # Handle running from .context/scripts or root
    if os.path.basename(project_root) == 'scripts':
        project_root = os.path.abspath(os.path.join(project_root, '../../'))
    
    packed_content = []
    
    print(f"Packing context from {project_root}...\n")
    
    for rel_path in CONTEXT_FILES:
        full_path = os.path.join(project_root, rel_path)
        if os.path.exists(full_path):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    packed_content.append(f"--- START FILE: {rel_path} ---")
                    packed_content.append(content)
                    packed_content.append(f"--- END FILE: {rel_path} ---\n")
            except Exception as e:
                print(f"Error reading {rel_path}: {e}")
        else:
             print(f"Skipping missing file: {rel_path}")

    return "\n".join(packed_content)

if __name__ == "__main__":
    result = pack_context()
    
    # Check if piping to stdout or file
    if sys.stdout.isatty():
        print("--- PACKED CONTEXT START ---")
        print(result)
        print("--- PACKED CONTEXT END ---")
        print("\n(Tip: Pipe this output to pbcopy to copy to clipboard: python3 pack_context.py | pbcopy)")
    else:
        print(result)
