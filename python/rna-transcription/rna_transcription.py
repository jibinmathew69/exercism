def to_rna(dna_strand):
    convert = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }
    try:
        dna_strand = map(lambda x: convert[x], dna_strand)
    except:
        raise Exception("invalid character found")
    return "".join(dna_strand)

