import os
import re

def update_references(directory):
    extensions_to_replace = re.compile(r'\.(png|jpg|jpeg)', re.IGNORECASE)
    file_types = ('.html', '.css', '.json', '.js')
    
    for root, dirs, files in os.walk(directory):
        if 'env' in dirs:
            dirs.remove('env')  # Skip virtual env
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith(file_types):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = extensions_to_replace.sub('.webp', content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated references in: {file}")
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    update_references(".")
