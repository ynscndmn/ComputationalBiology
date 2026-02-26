import collections

def get_top_codons(fasta_file, top_n=5):
    #Standard genetic code mapping
    amino_acids = {
        'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'AAT': 'Asn', 'AAC': 'Asn',
        'GAT': 'Asp', 'GAC': 'Asp',
        'TGT': 'Cys', 'TGC': 'Cys',
        'CAA': 'Gln', 'CAG': 'Gln',
        'GAA': 'Glu', 'GAG': 'Glu',
        'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'CAT': 'His', 'CAC': 'His',
        'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile',
        'TTA': 'Leu', 'TTG': 'Leu', 'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
        'AAA': 'Lys', 'AAG': 'Lys',
        'ATG': 'Met',
        'TTT': 'Phe', 'TTC': 'Phe',
        'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser', 'AGT': 'Ser', 'AGC': 'Ser',
        'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'TGG': 'Trp',
        'TAT': 'Tyr', 'TAC': 'Tyr',
        'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
        'TAA': 'Stop', 'TGA': 'Stop', 'TAG': 'Stop'
    }

    codon_counts = collections.Counter()
    
    #Parsing the FASTA file
    with open(fasta_file, 'r') as file:
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                #Processing the accumulated sequence before starting the new one
                if sequence:
                    full_seq = "".join(sequence).upper()
                    #Extracting codons (step by 3)
                    for i in range(0, len(full_seq) - 2, 3):
                        codon = full_seq[i:i+3]
                        #Only count clean, valid length codons
                        if len(codon) == 3 and 'N' not in codon:
                            codon_counts[codon] += 1
                sequence = [] #Reseting for the next sequence
            else:
                sequence.append(line)
                
        #Processing the very last sequence in the file
        if sequence:
            full_seq = "".join(sequence).upper()
            for i in range(0, len(full_seq) - 2, 3):
                codon = full_seq[i:i+3]
                if len(codon) == 3 and 'N' not in codon:
                    codon_counts[codon] += 1

    #Getting the top N codons
    top_codons = codon_counts.most_common(top_n)
    
    #Printing the results
    print(f"Top {top_n} Most Frequent Codons:")
    print("-" * 40)
    for rank, (codon, count) in enumerate(top_codons, 1):
        aa = amino_acids.get(codon, "Unknown")
        print(f"{rank}. {codon} -> Encodes: {aa} | Count: {count:,}")

#File path
fasta_filename = "Homo_sapiens.GRCh38.cds.all.fa"
print("File reading started")
get_top_codons(fasta_filename)
