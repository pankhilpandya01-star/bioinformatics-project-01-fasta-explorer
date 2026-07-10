# Temporary helper used to download the verified 16S rRNA dataset.
# After the FASTA file is saved in the repository, this helper can be removed.

from urllib.request import Request, urlopen


accessions = [
    "NR_024570.1",
    "NR_112116.2",
    "NR_037007.2",
    "NR_117678.1",
]

output_file = "bacterial_16s_sequences.fasta"

# Download all four records in one request to avoid sending several rapid
# requests to NCBI and triggering a temporary rate limit.
accession_text = ",".join(accessions)
url = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    "?db=nuccore&id=" + accession_text + "&rettype=fasta&retmode=text"
)

request = Request(
    url,
    headers={"User-Agent": "FASTA-Explorer-beginner-project/1.0"},
)

print("Downloading four verified 16S rRNA records from NCBI...")

try:
    sequence_data = urlopen(request, timeout=30).read().decode("utf-8")

    with open(output_file, "w") as fasta_file:
        fasta_file.write(sequence_data)

    print("Download complete.")
    print("Sequences saved to:", output_file)

except Exception as error:
    print("The download could not be completed.")
    print("Error:", error)
