import os

# Function to create or append to files
def create_or_append_file(filename, content):
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as f:
        f.write(content)

# Generate 100 text files
for i in range(1, 101):
    filename = f"file{i}.txt"
    content = f"This is file {i}."
    create_or_append_file(filename, content)

print("Files created successfully.")
