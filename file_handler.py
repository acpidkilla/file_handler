# file_handler.py

def create_file(filename, content):
    """Creates a file and writes content to it."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")

def read_file(filename):
    """Reads the content of a file and prints it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    filename = "example.txt"
    content = "This is an example file.\nWelcome to the world of Python!"

    create_file(filename, content)
    read_file(filename)
