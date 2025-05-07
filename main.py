import os

def print_tree(directory, prefix=""):
    """Recursively prints a directory tree structure."""
    if not os.path.isdir(directory):
        print(f"\n❌ Invalid directory: {directory}\nPlease update the path in the script.")
        return

    files = sorted(os.listdir(directory))
    pointers = ['├── '] * (len(files) - 1) + ['└── ']

    for pointer, file_name in zip(pointers, files):
        file_path = os.path.join(directory, file_name)
        print(prefix + pointer + file_name)
        if os.path.isdir(file_path):
            extension = '│   ' if pointer == '├── ' else '    '
            print_tree(file_path, prefix + extension)

if __name__ == "__main__":
    # ✏️ Set your folder path here:
    folder_path = r"C:\Users\786\Downloads\src(2)\src"


    print(f"\n📁 Directory structure of: {folder_path}\n")
    print_tree(folder_path)
