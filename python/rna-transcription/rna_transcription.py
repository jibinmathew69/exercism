def to_rna(dna_strand):
    convert = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }
    rna = list(dna_strand)
    rna = map(lambda x: convert[x], rna)
    return "".join(rna)

