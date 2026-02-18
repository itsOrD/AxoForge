import os
import re
import json
import sys

# Configuration
SKIP_EXTENSIONS = ['.py', '.pyc', '.git', '.png', '.jpg', '.jpeg', '.lock']
SKIP_DIRS = ['.git', '__pycache__', 'node_modules', 'venv', '.venv']

def find_placeholders(root_dir):
    """Recursively find all unique {{PLACEHOLDERS}} in text files."""
    placeholders = set()
    matches_in_files = {}

    for root, dirs, files in os.walk(root_dir):
        # Filter directories in place
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            
            # Skip this script and binary/ignored files
            if file_path == os.path.abspath(__file__):
                continue
            if ext in SKIP_EXTENSIONS or file == 'mcp.json.template':
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = re.findall(r'(\{\{[A-Z0-9_]+\}\})', content)
                    if matches:
                        for m in matches:
                            placeholders.add(m)
                            if file_path not in matches_in_files:
                                matches_in_files[file_path] = []
                            matches_in_files[file_path].append(m)
            except UnicodeDecodeError:
                continue # Skip binary files that we accidentally tried to read

    return sorted(list(placeholders)), matches_in_files

def get_user_values(placeholders):
    """Prompt user for values for each placeholder."""
    values = {}
    print("\n--- Project Configuration ---")
    print("Please provide values for the following placeholders found in the templates.\n")
    
    defaults = {
        '{{BUILD_COMMAND}}': 'npm run build',
        '{{TEST_COMMAND}}': 'npm test',
        '{{LINT_COMMAND}}': 'npm run lint',
        '{{LOG_DIR}}': './logs',
    }

    for p in placeholders:
        key = p
        clean_key = p.replace('{{', '').replace('}}', '')
        default_val = defaults.get(p, '')
        
        prompt = f"Value for {clean_key} (default: '{default_val}'): " if default_val else f"Value for {clean_key}: "
        user_input = input(prompt).strip()
        
        if not user_input and default_val:
            values[p] = default_val
        elif user_input:
            values[p] = user_input
        else:
            values[p] = f"TODO_{clean_key}" # Fallback if empty
            
    return values

def replace_in_files(matches_in_files, values):
    """Replace placeholders with values in the identified files."""
    print("\n--- Applying Changes ---")
    for file_path, placeholders in matches_in_files.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for p in placeholders:
                if p in values:
                    new_content = new_content.replace(p, values[p])
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

def generate_mcp_config(values, project_root):
    """Generate mcp.json from template and user values."""
    print("\n--- Generating MCP Config ---")
    
    # Template is now in .context/templates/mcp.json.template relative to project root
    template_path = os.path.join(project_root, '.context', 'templates', 'mcp.json.template')
    output_path = os.path.join(project_root, 'mcp.json')
    
    if not os.path.exists(template_path):
        print(f"Warning: {template_path} not found. Skipping MCP generation.")
        return

    try:
        with open(template_path, 'r') as f:
            data = json.load(f)
            
        # Add database server if configured
        db_server_name = values.get('{{DATABASE_MCP_SERVER}}')
        db_conn_var = values.get('{{ENV_VAR_NAME}}')
        
        if db_server_name and not db_server_name.startswith("TODO"):
            # This is a heuristic: assuming the user wants to add a server for the DB
            # We add a generic entry that the user can tune later
            if 'mcpServers' not in data:
                data['mcpServers'] = {}
                
            server_config = {
                "command": "npx", # Defaulting to npx, user might need to change
                "args": ["-y", db_server_name],
                "env": {
                     "DATABASE_URL": f"${{{db_conn_var}}}" if db_conn_var else "postgres://user:pass@localhost/db"
                }
            }
            # Use the package name as the key, or a generic name
            key_name = db_server_name.split('/')[-1]
            data['mcpServers'][key_name] = server_config
            print(f"Added MCP server entry for: {key_name}")

        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Generated: {output_path}")
        
    except Exception as e:
        print(f"Error generating mcp.json: {e}")

def reset_git_repo(project_root):
    """Re-initialize the git repository."""
    print("\n--- Git Initialization ---")
    confirm = input("Do you want to reset the git repository? (deletes .git and runs git init) (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            git_dir = os.path.join(project_root, '.git')
            if os.path.exists(git_dir):
                import shutil
                shutil.rmtree(git_dir)
                print(f"Removed {git_dir}")
            
            os.system(f"cd {project_root} && git init")
            print("Initialized new git repository.")
        except Exception as e:
            print(f"Error resetting git repo: {e}")
    else:
        print("Skipping git reset.")

def setup_readme(values, project_root):
    """Replace README.md with the project specific template."""
    print("\n--- README Setup ---")
    confirm = input("Do you want to overwrite README.md with a fresh project starter? (y/n): ").strip().lower()
    if confirm == 'y':
        template_path = os.path.join(project_root, '.context', 'templates', 'README.md.template')
        readme_path = os.path.join(project_root, 'README.md')
        
        if not os.path.exists(template_path):
             print(f"Warning: {template_path} not found. Skipping README update.")
             return

        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace placeholders in the template first
            new_content = content
            for p, v in values.items():
                new_content = new_content.replace(p, v)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Updated README.md with project details.")
        except Exception as e:
            print(f"Error updating README.md: {e}")
    else:
        print("Skipping README update.")

def main():
    print("Initializing AI Native Repo Setup...")
    
    # Determine Project Root
    # If this script is in .context/scripts/, root is ../../
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir) == 'scripts' and os.path.basename(os.path.dirname(current_dir)) == '.context':
        project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    else:
        project_root = os.getcwd()

    print(f"Project Root: {project_root}")
    
    placeholders, matches_in_files = find_placeholders(project_root)
    
    if not placeholders:
        print("No {{PLACEHOLDERS}} found in text files. Nothing to hydrate.")
        return

    values = get_user_values(placeholders)
    
    # Confirm
    print("\nProposed Values:")
    for k, v in values.items():
        print(f"  {k} -> {v}")
    
    confirm = input("\nProceed with replacement? (y/n): ").lower()
    if confirm != 'y':
        print("Aborted.")
        return

    replace_in_files(matches_in_files, values)
    generate_mcp_config(values, project_root)
    
    # Optional Steps
    reset_git_repo(project_root)
    setup_readme(values, project_root)
    
    print("\nSetup Complete! 🚀")

if __name__ == "__main__":
    main()
