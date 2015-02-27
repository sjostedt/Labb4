#################
### Labb 3.1
### Mikael Sjöstedt & Alexander Ramm
### Version 1

class Node:
	def __init__(self, value = None):
		self.value = value
		self.right = None
		self.left = None


class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
    	#Stoppar in värdet newvalue i trädet och sorterar det till rätt plats
        self.root = self.putFunc(self.root,newvalue)

    def exists(self,value):
    	#Testar om value finns i trädet och returnerar True/False
        return self.existsFunc(self.root,value)

    def write(self):
    	#Skriver ut alla värden i trädet i bokstavsordning
        self.writeFunc(self.root)
        print("\n")


    def putFunc(self, parent, value):
    	#rekursiv grej
    	#newNode = Node(value)
    	if self.root == None:
    		#newNode = Node(value)
    		#newNode.right = newNode
    		#newNode.left = newNode
    		root = Node(value)
    		#print('self.root måste göras först')
    		#return newNode
    		return root

    	#Testar åt höger
    	elif value > parent.value:
    		if parent.right == None:
    			#print('parent.right görs')
    			parent.right = Node(value)
    			return parent
    		else:
    			self.putFunc(parent.right, value)
    			return parent

    	#Testar åt vänster
    	elif value < parent.value:
    		if parent.left == None:
    			#print('parent.left görs')
    			parent.left = Node(value)
    			return parent
    		else:	
    			#print("rekurs")
    			self.putFunc(parent.left, value)
    			return parent

    	else:
    		print("ERROR, something went wrong when building tree")
    		

    def existsFunc(self, root, value):
    	found = False

    	if root == None:
    		return False
    	if value == root.value:
    		return True
    	if value < root.value:
    		return self.existsFunc(root.left, value)
    	if value > root.value:
    		return self.existsFunc(root.right, value)

    	
    def writeFunc(self, root):
    	if root.left != None:
    		#print("rekursiv left")
    		self.writeFunc(root.left)
    	print (root.value)
    	if root.right:
    		#print("rekursiv right")
    		self.writeFunc(root.right)




def main():
	# Testar lite
	tree = Bintree()
	
	tree.put("gurka")
	tree.put("morot")
	tree.put("krak")
	tree.put("banan")
	tree.put("banan2")
	tree.put("bana")

	
	tree.write()
	print ('värde på exist ', tree.exists("morot"))

	#print(tree.root.right.value)
	#print(tree.root.left.value)
	#testfunc()
	#tree.write()
	#print (tree.root.left.value)
	#print (tree.root.right.value)


if __name__ == "__main__":
	main()
