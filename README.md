# Community
# Language: Python
# Input: CSV
# Output: NOA
# Tested with: PluMA 1.1, Python 3.6

Analyze the cluster (community) of a target entity

The plugin expects as input a TXT file of tab-delimited keyword-value pairs:
abundances: NOA file of taxa and abundances
clusters: CSV file of clusters
centroids: CSV file of cluster centroids
target: OTU to target

It will produce an NOA file of the cluster of the target OTU, including the abundances and whether or not each node is a centroid.
