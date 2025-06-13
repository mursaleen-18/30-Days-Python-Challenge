class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"File {self.filename} closed safely.")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        # Returning False will re-raise the exception after __exit__
        return False

# Example usage
with FileManager('demo.txt', 'w') as f:
    f.write("Hello from your custom context manager!\n")
    f.write("This was safely written and the file will close automatically.")
