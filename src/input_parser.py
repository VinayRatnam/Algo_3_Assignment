import sys

def parse_input():
    """
    Parses the input from standard input (stdin) when using pipes.
    
    Expected format:
    K
    x1 v1
    x2 v2
    ...
    xK vK
    A
    B
    
    Returns:
        char_values (dict): A dictionary mapping characters to their integer values.
        A (str): The first string.
        B (str): The second string.
    """
    # Read all lines from standard input and remove empty lines
    lines = [line for line in sys.stdin.read().splitlines() if line.strip()]
    
    if not lines:
        return {}, "", ""
        
    K = int(lines[0].strip())
    
    char_values = {}
    # Read K characters and their values
    for i in range(1, K + 1):
        parts = lines[i].strip().split()
        if len(parts) >= 2:
            char = parts[0]
            val = int(parts[1])
            char_values[char] = val
            
    # Read the two main strings
    A = lines[K + 1].strip() if len(lines) > K + 1 else ""
    B = lines[K + 2].strip() if len(lines) > K + 2 else ""
            
    return char_values, A, B

if __name__ == "__main__":
    # Simple test execution when running this file directly with a pipe
    char_values, A, B = parse_input()
    print("Character Values:", char_values)
    print("String A:", A)
    print("String B:", B)
