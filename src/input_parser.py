import sys

def parse_input(raw_lines):
    # Remove empty lines and whitespace
    lines = [line.strip() for line in raw_lines if line.strip()]
    
    if not lines:
        return {}, "", ""
        
    K = int(lines[0])
    
    char_values = {}
    # Read K characters and their values
    for i in range(1, K + 1):
        parts = lines[i].split()
        if len(parts) >= 2:
            char = parts[0]
            val = int(parts[1])
            char_values[char] = val
            
    # Read the two main strings
    A = lines[K + 1] if len(lines) > K + 1 else ""
    B = lines[K + 2] if len(lines) > K + 2 else ""
            
    return char_values, A, B

if __name__ == "__main__":
    # Simple test execution when running this file directly with a pipe
    raw_lines = sys.stdin.readlines()
    char_values, A, B = parse_input(raw_lines)
    print("Character Values:", char_values)
    print("String A:", A)
    print("String B:", B)
