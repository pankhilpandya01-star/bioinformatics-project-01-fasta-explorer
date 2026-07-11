# FASTA Explorer
# Project 2: Analyze multiple DNA sequences from one FASTA file

# The csv module is used to save the final results in a spreadsheet-friendly file.
import csv


# Read all DNA sequences from a multi-FASTA file.
# Each sequence is stored in a dictionary using its FASTA header as the key.
def read_multi_fasta(filename):
    sequences = {}
    current_id = ""
    current_sequence = ""

    # Open the FASTA file and read it one line at a time.
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # A line beginning with ">" marks the start of a new FASTA record.
            if line.startswith(">"):
                # Save the previous sequence before starting the next one.
                if current_id != "":
                    sequences[current_id] = current_sequence

                current_id = line.replace(">", "")
                current_sequence = ""
            else:
                # Add each DNA line to the current sequence.
                current_sequence = current_sequence + line

        # Save the final sequence after the end of the file is reached.
        if current_id != "":
            sequences[current_id] = current_sequence

    return sequences


# Calculate the percentage of G and C bases in a DNA sequence.
def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    # Avoid dividing by zero if an empty sequence is found.
    if len(sequence) == 0:
        return 0

    gc_percent = ((g_count + c_count) / len(sequence)) * 100
    return round(gc_percent, 2)


# Save the sequence ID, length, and GC content for every record in a CSV file.
def save_summary(results, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Sequence ID", "Length (bp)", "GC Content (%)"])

        for result in results:
            writer.writerow(result)


# Display the program title and ask the user for the FASTA filename.
print("FASTA Explorer")
print("This program compares multiple DNA sequences from one FASTA file.")
print()

filename = input("Enter the multi-FASTA file name: ")

try:
    # Read the sequences from the file supplied by the user.
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

        # Analyze each sequence separately and store its results.
        for sequence_id in sequences:
            sequence = sequences[sequence_id].upper()
            sequence_length = len(sequence)
            sequence_gc = gc_content(sequence)

            results.append([sequence_id, sequence_length, sequence_gc])

            print(sequence_id)
            print("Length:", sequence_length, "bp")
            print("GC content:", str(sequence_gc) + "%")
            print()

        # Compare all records using their length and GC-content values.
        longest = max(results, key=lambda row: row[1])
        shortest = min(results, key=lambda row: row[1])
        highest_gc = max(results, key=lambda row: row[2])
        lowest_gc = min(results, key=lambda row: row[2])

        # Add all GC-content values and divide by the number of sequences.
        total_gc = 0
        for result in results:
            total_gc = total_gc + result[2]

        average_gc = round(total_gc / len(results), 2)

        # Display the main comparison results in the terminal.
        print("Comparison Results")
        print("------------------")
        print("Longest sequence:", longest[0], "(" + str(longest[1]) + " bp)")
        print("Shortest sequence:", shortest[0], "(" + str(shortest[1]) + " bp)")
        print("Highest GC content:", highest_gc[0], "(" + str(highest_gc[2]) + "%)")
        print("Lowest GC content:", lowest_gc[0], "(" + str(lowest_gc[2]) + "%)")
        print("Average GC content:", str(average_gc) + "%")
        print()

        # Export the same results to a CSV file.
        output_file = "fasta_summary.csv"
        save_summary(results, output_file)
        print("Results saved to:", output_file)

# Show a clear message if the user enters a filename that does not exist.
except FileNotFoundError:
    print()
    print("File not found. Please check the file name and try again.")
