# a script to add find members of gene clusters in the IGC and 3CGC that come from AGC/CGC/EGC/SPGC

# commands
# refer to run_cluster_of_clusters.sh for usage

import sys

c=0
THREECGC = sys.argv[1]
AEC = {i.strip('\n').split('\t')[0].strip():i.strip('\n').split('\t')[1:] for i in open(sys.argv[2])}

o = open(THREECGC[:-6]+'cluster_of_clusters.txt','w')
o1 = open(sys.argv[1][:-4]+'remainder.txt','w')

cluster_recruits = {} # dictionary where keys are cluster centroids and values are recruited sequences

for i in open(THREECGC):
	if i.startswith('>'):
		continue
	else:
		c += 1
		i = i.split('\t')[1].strip()
		if i.endswith('*'):
			x = i.split(' *')[0]
			cluster_recruits[x] = AEC[x]
			AEC.pop(x,None)
		else:
			y = i.split(' at ')[0]
			cluster_recruits[x].append(y)
			cluster_recruits[x]+AEC[y]
			AEC.pop(y,None)

for k,v in cluster_recruits.items():
	o.write(k+'\t'+'\t'.join(v)+'\n')

for k,v in AEC.items():
	o1.write(k+'\t'+'\t'.join(v)+'\n')

o.close()
o1.close()

print THREECGC+'\t'+str(c)+'\n'
