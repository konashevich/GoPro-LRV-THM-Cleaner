import os
import sys

def delete_files(folder_path, extensions):
    """
    Deletes files with the specified extensions in the specified folder.

    :param folder_path: The path to the folder where files will be searched and deleted.
    :param extensions: A list of file extensions to delete.
    """
    # Ensure the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    print(f"Deleting files in: {folder_path}")
    
    # Count of deleted files for feedback
    deleted_files_count = 0

    # Walk through all files in the specified folder
    for file in os.listdir(folder_path):
        # Check if the file has an extension that needs to be deleted
        if file.endswith(tuple(extensions)):
            file_path = os.path.join(folder_path, file)
            try:
                os.remove(file_path)
                deleted_files_count += 1
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    if deleted_files_count == 0:
        print("No files found with the specified extensions.")
    else:
        print(f"Total deleted files: {deleted_files_count}")

if __name__ == "__main__":
    extensions = ['.THM', '.LRV']

    # Check if a path is passed as a command-line argument
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]  # Use the provided path
    else:
        # Attempt to use the executable's directory when no argument is provided
        folder_path = os.path.dirname(sys.argv[0])

    delete_files(folder_path, extensions)
