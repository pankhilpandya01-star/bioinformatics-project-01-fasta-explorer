# FASTA Explorer
# Project 2: Analyze multiple DNA sequences from one FASTA file

import csv


def read_multi_fasta(filename):
    sequences = {}
    current_id = ""
    current_sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_id != "":
                    sequences[current_id] = current_sequence

                current_id = line.replace(">", "")
                current_sequence = ""
            else:
                current_sequence = current_sequence + line

        if current_id != "":
            sequences[current_id] = current_sequence

    return sequences


def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    if len(sequence) == 0:
        return 0

    gc_percent = ((g_count + c_count) / len(sequence)) * 100
    return round(gc_percent, 2)


def save_summary(results, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Sequence ID", "Length (bp)", "GC Content (%)"])

        for result in results:
            writer.writerow(result)


print("FASTA Explorer")
print("This program compares multiple DNA sequences from one FASTA file.")
print()

filename = input("Enter the multi-FASTA file name: ")

try:
    sequences = read_multi_fasta(filename)

    if len(sequences) == 0:
        print("No sequences were found in the FASTA file.")
    else:
        results = []

        print()
        print("Sequences found:", len(sequences))
        print()
        print("Sequence Summary")
        print("----------------")

        for sequence_id in sequences:
            sequence = sequences[sequence_id].upper()
            sequence_length = len(sequence)
            sequence_gc = gc_content(sequence)

            results.append([sequence_id, sequence_length, sequence_gc])

            print(sequence_id)
            print("Length:", sequence_length, "bp")
            print("GC content:", str(sequence_gc) + "%")
            print()

        longest = max(results, key=lambda row: row[1])
        shortest = min(results, key=lambda row: row[1])
        highest_gc = max(results, key=lambda row: row[2])
        lowest_gc = min(results, key=lambda row: row[2])

        print("Comparison Results")
        print("------------------")
        print("Longest sequence:", longest[0], "(" + str(longest[1]) + " bp)")
        print("Shortest sequence:", shortest[0], "(" + str(shortest[1]) + " bp)")
        print("Highest GC content:", highest_gc[0], "(" + str(highest_gc[2]) + "%)")
        print("Lowest GC content:", lowest_gc[0], "(" + str(lowest_gc[2]) + "%)")
        print()

        output_file = "fasta_summary.csv"
        save_summary(results, output_file)
        print("Results saved to:", output_file)

except FileNotFoundError:
    print()
    print("File not found. Please check the file name and try again.")
