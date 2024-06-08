from typing import List

def read_file(file_path: str) -> List[str]:
    
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip()) 
    return lines

# Example usage:
file_path = r'C:\Users\redda\Downloads\sample1.txt'
lines = read_file(file_path)
print(lines)