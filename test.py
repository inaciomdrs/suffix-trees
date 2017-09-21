from suffix_trees.STree import STree

words = ['los angeles','lossless']

tree = STree(words)

LCS = tree.lcs()

for pattern in LCS:
	print pattern,
