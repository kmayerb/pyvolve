import re

class Node:
	def __init__(self):
		self.name = None # this can either be None (internal) or a leaf name.
		self.children = [] # list of children, each of which is a node
		self.BL = None # Branch length leading up to node
		self.seq = None # Sequence can be stored here when simulating


def printTree(tree, level=0, num=0):
	indent=''
	for i in range(level):
		indent+='\t'
	print indent, tree.name, tree.BL, num
	num+=1
	if len(tree.children)>0:
		print indent,"here i am", len(tree.children)
		for node in tree.children:
			num=printTree(node, level+1, num)
	return num
	
def readBranchLength(tstring, index):
	assert(tstring[index]==':')
	
	end = index
	while True:
		end += 1
		if end==len(tstring):
			break
		if tstring[end]==',' or tstring[end]==')':
			break
	BL = float( tstring[index+1:end] )
	return BL, end

def readLeaf(tstring, index):
	end = index
	node = Node()
	while True:
		end += 1
		assert( end<len(tstring) )
		
		# Leaf has a branch length
		if tstring[end]==',' or tstring[end]==')':
			node.name = tstring[index+1:end]
			node.BL = None
			break
		
		# Leaf has no branch length	
		if tstring[end]==':' :
			node.name = tstring[index:end]
			node.BL, end = readBranchLength(tstring, end)
			break
			
	return node, end



def parseTree(tstring, index=0):

	assert(tstring[index]=='(')

	index += 1
	node = Node()
	while True:
	
		if tstring[index]=='(':
			subtree, index=parseTree(tstring, index)
			node.children.append( subtree )
		
		elif tstring[index]==',':
			index += 1
			
		elif tstring[index]==')':
			index+=1
			if index<len(tstring):
				BL, index = readBranchLength(tstring, index)
				node.BL = BL
			break
		
		else:
			subtree, index = readLeaf(tstring, index)
			node.children.append( subtree )
	
	return node, index


def readTree(treefile):

	t = open(treefile, 'r')
	tstring = t.read()
	t.close()
	
	############ Format tree appropriately. ############### 
	tstring = re.sub(r"\s", "", tstring)                  # Remove all whitespace
	tstring = tstring.rstrip(';')                         # Remove trailing semi-colon

	# Go to town
	(tree, index) = parseTree(tstring,  0)
	return tree

tree = readTree('small.tre')
printTree(tree)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	