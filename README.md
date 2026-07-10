# FASTA Explorer

FASTA Explorer is my second beginner bioinformatics project.

The project builds on BioSeq Toolkit by moving from one DNA sequence to a FASTA file containing multiple real bacterial 16S rRNA gene sequences.

## Project Question

How do sequence length and GC content differ among 16S rRNA gene sequences from different bacterial species?

## What the Program Does

- downloads verified 16S rRNA records from NCBI RefSeq
- reads multiple sequences from one FASTA file
- counts how many sequences are present
- calculates the length of each sequence
- calculates GC content for each sequence
- identifies the longest and shortest sequences
- identifies the highest and lowest GC content
- saves the summary as a CSV file

## Species Included

- *Escherichia coli*
- *Bacillus subtilis*
- *Staphylococcus aureus*
- *Pseudomonas aeruginosa*

The exact strains, accession numbers, and sequence status are listed in `accession_sources.csv`.

## Project Files

```text
bioinformatics-project-01-fasta-explorer/
├── download_sequences.py
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

The sequence records come from NCBI RefSeq. The project uses these verified accessions:

| Species | Accession | Record type |
|---|---|---|
| *Escherichia coli* | NR_024570.1 | Partial 16S rRNA |
| *Bacillus subtilis* | NR_112116.2 | Complete 16S rRNA |
| *Staphylococcus aureus* | NR_037007.2 | Complete 16S rRNA |
| *Pseudomonas aeruginosa* | NR_117678.1 | Partial 16S rRNA |

Because two records are partial and two are complete, sequence-length differences should be interpreted partly as differences in record coverage, not only as biological differences.

## How to Run

First download the real sequence data:

```bash
python download_sequences.py
```

This creates:

```text
bacterial_16s_sequences.fasta
```

Then run the analysis:

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
- Verified NCBI accessions documented
- Real-data download script added
- Local testing and screenshots pending

## Next Step

Run both scripts locally, review the generated CSV file, and add the real output and screenshot to this README.
