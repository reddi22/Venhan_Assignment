from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
   
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")

# Example usage:
file_path = r'C:\Users\redda\Downloads\sample1.txt'
lines_to_write = ["Line 1", "Line 2", "Line 3"]
write_file(file_path, lines_to_write)

r'C:\Users\redda\Downloads\sample1.txt'