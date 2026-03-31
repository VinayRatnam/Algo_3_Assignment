import sys
import hvlcs
import output_writer
import input_parser

def main():
    try:
        lines = sys.stdin.readlines()

        values, s1, s2 = input_parser.parse_input(lines)
        hvlcs.hvlcs_algo(values, s1, s2)

        output_writer.write_output()

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")


if __name__ == "__main__":
    main()
