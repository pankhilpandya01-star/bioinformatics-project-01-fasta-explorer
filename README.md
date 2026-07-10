# FASTA Explorer

FASTA Explorer is my second beginner bioinformatics project.

The project builds on BioSeq Toolkit by moving from one DNA sequence to a FASTA file containing multiple real bacterial 16S rRNA gene sequences.

## Project Question

How do sequence length and GC content differ among 16S rRNA gene sequences from different bacterial species?

## What the Program Will Do

- read multiple sequences from one FASTA file
- count how many sequences are present
- calculate the length of each sequence
- calculate GC content for each sequence
- identify the longest and shortest sequences
- identify the highest and lowest GC content
- save the summary as a CSV file

## Planned Files

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

The final dataset will contain verified bacterial 16S rRNA records from a public nucleotide database. Each FASTA header will include the organism name and accession number so the data can be traced back to its source.

The accession list and downloaded sequences will be added only after every record has been checked to confirm that it represents the intended 16S rRNA sequence.

## Current Status

- Project structure created
- Multi-FASTA analysis code added
- Public sequence records being verified
- Local testing and screenshots still pending

## Next Step

After the real multi-FASTA dataset is added, the program will be run locally and the real output will be added to this README.
