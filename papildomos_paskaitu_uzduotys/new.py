def read_file_as_string(filename: str) -> Optional[str]:
    """
    Reads the contents of a file into a string.
    Returns the file contents as a string on success, or None on failure.
    """
    pass

with open(source_file, 'r') as reader:
  dos_content = reader.read()

print(read_file_as_string("test.json"))

