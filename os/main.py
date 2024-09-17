import os
source_file = "original.txt"
destination_file = "copy.txt"
# Check if source file exists
if os.path.exists(source_file):
    with open(source_file, "rb") as source:
        with open(destination_file, "wb") as destination:
            for chunk in iter(lambda: source.read(1024), b""):
                destination.write(chunk)
    print("File copied successfully!")
else:
    print(f"Error: Source file '{source_file}' does not exist.")