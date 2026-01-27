def DNA_strand(dna):
    reference = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    complementary = [reference[n] for n in dna]
    return ''.join(complementary)