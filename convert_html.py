import os

# Specify the directory and the file extension you want to add
directory = './slalom_docs/website/'
extension = '.html'

# Loop through the files in the directory
for filename in os.listdir(directory):
    # Create the new filename with the added extension
    new_filename = filename + extension
    
    # Get the full paths for the old and new filenames
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_path, new_path)

print(f'Added {extension} extension to every file in {directory}')
