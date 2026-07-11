# FASTA Explorer

FASTA Explorer is my second beginner bioinformatics project.

The project builds on BioSeq Toolkit by moving from one DNA sequence to a FASTA file containing multiple real bacterial 16S rRNA gene sequences.

## Project Question

How do sequence length and GC content differ among complete 16S rRNA sequences from different bacterial species?

## What the Program Does

- reads multiple sequences from one FASTA file
- counts how many sequences are present
- calculates the length of each sequence
- calculates GC content for each sequence
- identifies the longest and shortest sequences
- identifies the highest and lowest GC content
- calculates the average GC content across all sequences
- saves the summary as a CSV file

## Species Included

- *Escherichia coli*
- *Bacillus subtilis*
- *Staphylococcus aureus*
- *Pseudomonas aeruginosa*

The accession numbers and sequence details are listed in `accession_sources.csv`.

## Project Files

```text
bioinformatics-project-01-fasta-explorer/
├── fasta_explorer.py
├── bacterial_16s_sequences.fasta
├── accession_sources.csv
├── fasta_summary.csv
├── images/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Data Source

The four complete 16S rRNA records are already included in `bacterial_16s_sequences.fasta`.

| Species | Accession | Record type | Database |
|---|---|---|---|
| *Escherichia coli* | J01859.1 | Complete 16S rRNA | NCBI GenBank |
| *Bacillus subtilis* | NR_112116.2 | Complete 16S rRNA | NCBI RefSeq |
| *Staphylococcus aureus* | NR_037007.2 | Complete 16S rRNA | NCBI RefSeq |
| *Pseudomonas aeruginosa* | NR_026078.1 | Complete 16S rRNA | NCBI RefSeq |

Using complete records makes the sequence-length comparison more meaningful than comparing a mixture of partial and complete records.

## How to Run

Run the analysis directly:

```bash
python fasta_explorer.py
```

When asked for the file name, enter:

```text
bacterial_16s_sequences.fasta
```

The program will also create:

```text
fasta_summary.csv
```

## Current Status

- Project structure created
- Multi-FASTA analysis code added
- Four complete real 16S rRNA records included
- Average GC content calculation added
- Accession numbers documented
- Local testing and screenshots pending

## Next Step

Run `fasta_explorer.py`, review the generated CSV file, and add the real terminal output and screenshot to this README.
