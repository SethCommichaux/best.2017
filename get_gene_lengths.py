# This program takes a fasta input file and returns a file of gene lengths, one gene length per line.

from Bio import SeqIO

results = []

for i in SeqIO.parse('refseq.fasta','fasta'):
	results.append(len(i.seq))

results = sorted(results)

o = open('gene_lengths_refseq.txt','w')

for i in results:
	o.write(str(i)+'\n')

o.close()
