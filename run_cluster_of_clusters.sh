#!/bin/bash

# command for slurm submission
# sbatch --nodes=1 --cpus-per-task=4 --mem=30GB --time=100:00:00 --qos=large run_cluster_of_clusters.sh

cd /cbcb/project-scratch/BEST2017/data/IGC_data/1.GeneCatalogs

python cluster_of_clusters.py CGC.clstr
python cluster_of_clusters.py AGC.clstr
python cluster_of_clusters.py EGC.clstr
python cluster_of_clusters.py SPGC.clstr

cat EGCcluster_of_clusters.txt AGCcluster_of_clusters.txt CGCcluster_of_clusters.txt > all_cluster_of_clusters.txt 

python parent_cluster_of_clusters.py 3CGC.clstr all_cluster_of_clusters.txt

cat 3CGCcluster_of_clusters.txt SPGCcluster_of_clusters.txt > all_parent_cluster_of_clusters.txt

python parent_cluster_of_clusters.py IGC.clstr all_parent_cluster_of_clusters.txt

python cluster_count.py all_cluster_of_clusters.txt
python cluster_count.py all_parent_cluster_of_clusters.txt
python cluster_count.py IGCcluster_of_clusters.txt

# These final commands remove the intermediate files
#rm EGCcluster_of_clusters.txt AGCcluster_of_clusters.txt CGCcluster_of_clusters.txt
#rm all_cluster_of_clusters.txt 3CGCcluster_of_clusters.txt SPGCcluster_of_clusters.txt
#rm all_parent_cluster_of_clusters.txt
