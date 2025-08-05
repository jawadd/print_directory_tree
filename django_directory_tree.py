import os

def print_tree(directory, prefix="", exclude_dirs=None):
    """Recursively prints a clean directory tree structure, excluding specified directories."""
    if exclude_dirs is None:
        exclude_dirs = {'venv', 'migrations', '__pycache__'}  # Default directories to exclude

    if not os.path.isdir(directory):
        print(f"\n❌ Invalid directory: {directory}\nPlease update the path in the script.")
        return

    # Get all files and directories, excluding hidden ones and those in exclude_dirs
    files = sorted([f for f in os.listdir(directory) 
                    if not f.startswith('.') and 
                    (os.path.isfile(os.path.join(directory, f)) or 
                     f not in exclude_dirs)])
    
    pointers = ['├── '] * (len(files) - 1) + ['└── ']

    for pointer, file_name in zip(pointers, files):
        file_path = os.path.join(directory, file_name)
        print(prefix + pointer + file_name)
        if os.path.isdir(file_path):
            extension = '│   ' if pointer == '├── ' else '    '
            print_tree(file_path, prefix + extension, exclude_dirs)

if __name__ == "__main__":
    # ✏️ Set your folder path here:
    folder_path = r"C:\Users\786\Downloads\django_boilerplate-master\moonbow"

    print(f"\n📁 Directory structure of: {folder_path}\n")
    print_tree(folder_path)