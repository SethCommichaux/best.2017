import sys

n = sys.argv[1] # A .txt file of gene lengths provided on the command line.  Each line is one number, the length of a gene.

f = sorted([int(i.strip()) for i in open(sys.argv[1])]) # Sort gene lengths from least to greatest

freq_distribution_sampling = int(sys.argv[2]) # A user-provided number that represents how frequently the distribution of sorted gene lengths should be sampled.  For example, if distribution of gene lengths is 1,2,3,4,5,6,7,8,9,10 and the user enter 2, then the numbers returned will be 2,4,6,8,10.

divide_by_three = sys.argv[3] # If genes provided are nucleotides, user might want gene lengths in amino acids and thus should enter "Y" here

o = open(n[:-4]+str(freq_distribution_sampling)+'.txt','w') # Adds frequency of sampling number to .txt extension.  For example, if gene lengths file was "gene_lengths.txt", and frequency of sampling was 1000, then the output file will be gene_lengths1000.txt 

if divide_by_three.upper() == "Y":
	for i in range(0,len(f),int(round(float(len(f))/freq_distribution_sampling))):
		o.write(str(f[i]/3)+'\n')
elif divide_by_three.upper() == "N":
        for i in range(0,len(f),int(round(float(len(f))/freq_distribution_sampling))):
                o.write(str(f[i])+'\n')

o.close()
