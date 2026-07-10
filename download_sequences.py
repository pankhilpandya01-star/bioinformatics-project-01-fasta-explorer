# Download verified 16S rRNA sequences from NCBI

from urllib.request import urlopen


accessions = [
    "NR_024570.1",  # Escherichia coli
    "NR_112116.2",  # Bacillus subtilis
    "NR_037007.2",  # Staphylococcus aureus
    "NR_117678.1",  # Pseudomonas aeruginosa
]

output_file = "bacterial_16s_sequences.fasta"

with open(output_file, "w") as fasta_file:
    for accession in accessions:
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            "?db=nuccore&id=" + accession + "&rettype=fasta&retmode=text"
        )

        print("Downloading:", accession)
        sequence_data = urlopen(url).read().decode("utf-8")
        fasta_file.write(sequence_data)

print()
print("Download complete.")
print("Sequences saved to:", output_file)
