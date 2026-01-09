import os

class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        # Nothing special to return
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Remove the file if it exists when exiting the context
        if os.path.exists(self.filename):
            os.remove(self.filename)
