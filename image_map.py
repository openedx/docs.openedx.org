import os
import subprocess

def grep_for_filenames(source_dir, search_dir):
    # Loop through each file in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            # Define the full path to the current file
            file_path = os.path.join(root, file_name)
            
            # Get the base file name (without path) to search for it
            base_file_name = os.path.basename(file_path)
            
            print(f"Searching for '{base_file_name}' in {search_dir}...")

            # Use subprocess to call grep recursively in the target directory
            result = subprocess.run(
                ["grep", "-rl", base_file_name, search_dir],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.stdout:
                print(f"Found occurrences of '{base_file_name}':\n{result.stdout}")
            else:
                print(f"No occurrences found for '{base_file_name}'")
            
            if result.stderr:
                print(f"Error: {result.stderr}")


# Define the source directory (containing file names) and search directory
source_dir = "source/educators/migration_wip/images"
search_dir = "source/"

# Call the function
grep_for_filenames(source_dir, search_dir)

