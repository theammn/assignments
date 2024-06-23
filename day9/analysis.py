import argparse
from Bio import SeqIO
import os

def find_longest_repeating_subsequence(sequence):
    """Finds the longest repeating sub-sequence in a given DNA sequence."""
    n = len(sequence)
    longest_subseq = ""
    # Iterate over possible lengths of sub-sequences
    for length in range(1, n//2 + 1):
        # Check all sub-sequences of the current length
        for i in range(n - length * 2 + 1):
            subseq = sequence[i:i + length]
            # Check if this sub-sequence appears again later in the sequence
            if sequence.find(subseq, i + length) != -1:
                if len(subseq) > len(longest_subseq):
                    longest_subseq = subseq
    return longest_subseq

def calculate_gc_content(sequence):
    """Calculates the GC content of a given DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence) * 100

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Analyze DNA sequences.")
    parser.add_argument("file", help="Path to the input file (FASTA or GeneBank format).")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeating sub-sequence.")
    parser.add_argument("--gc_content", action="store_true", help="Calculate GC content of the sequence.")

    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.isfile(args.file):
        print(f"Error: {args.file} does not exist.")
        return

    # Read the sequence from the input file
    sequence = ""
    for record in SeqIO.parse(args.file, "fasta"):
        sequence = str(record.seq)
        break

    # Perform the requested analyses
    if args.duplicate:
        longest_subseq = find_longest_repeating_subsequence(sequence)
        print(f"Longest repeating sub-sequence: {longest_subseq}")

    if args.gc_content:
        gc_content = calculate_gc_content(sequence)
        print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
