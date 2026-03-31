import random
import string
import os
import argparse

def generate_example(filename, k, len_a, len_b, max_value=20):
    """
    Generates a mock input file for the Highest Value Longest Common Subsequence program.
    """
   
    k = min(k, 26)
    
    # k unique characters for the alphabet
    alphabet = random.sample(string.ascii_lowercase, k)
    
    # assign random values to each character
    char_values = {char: random.randint(1, max_value) for char in alphabet}
    
    # generate strings A and B
    A = ''.join(random.choices(alphabet, k=len_a))
    B = ''.join(random.choices(alphabet, k=len_b))
    
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(f"{k}\n")
        for char, val in char_values.items():
            f.write(f"{char} {val}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")
    print(f"Generated {filename}: Alphabet Size={k}, String A Length={len_a}, String B Length={len_b}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate input examples for the HVLCS algorithm")
    parser.add_argument("--filename", type=str, default="data/example_generated.in", help="Output file path")
    parser.add_argument("-k", type=int, default=5, help="Number of characters in the alphabet (max 26)")
    parser.add_argument("--lena", type=int, default=30, help="Length of String A")
    parser.add_argument("--lenb", type=int, default=30, help="Length of String B")
    parser.add_argument("--maxval", type=int, default=15, help="Maximum value for a character")
    
    args = parser.parse_args()
    
    generate_example(args.filename, args.k, args.lena, args.lenb, args.maxval)
