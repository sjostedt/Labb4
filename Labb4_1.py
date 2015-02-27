##################
### Labb 4
### Mikael Sjöstedt & Alexander Ramm
### version 1

from bintreeFile import *
from LinkedQFile import *
from string import ascii_lowercase




def createtree():
	#Skapar träd med alla ord från word3.txt
	tree = Bintree()
	duplicate_tree = Bintree()
	
	with open("word3.txt", "r", encoding = "utf-8") as fil:
	    for rad in fil:
	        ordet = rad.strip()                # Ett trebokstavsord per rad
	        if tree.exists(ordet):
	            #duplicate_tree.put(ordet) 
	            pass
	        else:
	            tree.put(ordet)             # in i sökträdet
	return (tree, duplicate_tree)
	

def makequeue(input):
	#Skapar barn och lägger dom i kön ?
	pass
def uppgift1(words, bad_words):
	print ("\n")
	temp = None
	queue = LinkedQ()
	bad_tree = Bintree()
	start_org = "söt"
	slut = "sur"

	start_org = list(start_org)
	start = list(start_org)
	# Lista med alfabetet
	L = list(ascii_lowercase)
	L= L + ["å", "ä", "ö"] # Lägger till non ascii
	


	
	# for i in range(len(start)):
	# 	for k in range(len(L)):
	# 		start[i] = L[k]
	# 		testword = "".join((start[0],start[1],start[2]))
	# 		testword = str(testword)
	# 		print (testword)
	# 		#print (type(testword))
	# 		if words.exists(testword) and not bad_tree.exists(testword): # Jag har någon tanke med bad_tree här ....
	# 			print("kör vi ? ")
	# 			temp = Node(testword)
	# 			temp.prev = testword
	# 			queue.put(temp)
	# 	start[i] = start_org[i]

	print ("Det här ligger i templistan nu \n")
	for i in range (queue.length):
		tempnode = queue.get()
		print (tempnode.value)

def rekursiv(start, slut, parentqueue, alphabet, bad_tree,words):
	for k in range(parentqueue.length):
		parentwordNode = parentqueue.get()
		parentword = list(parentwordNode.value) # Läser in ett ord från kön
		testword = list(parentwordNode.value)
		for i in range(len(parentword)):
			for k in range(len(alphabet)):
				testword[i] = alphabet[k]
				testword = "".join((testword[0],testword[1],testword[2]))
				testword = str(testword)			## Byter ut en bokstav i ordet från kö 
				#print (testword)
				#print (type(testword))
				if words.exists(testword) and not bad_tree.exists(testword): # Jag har någon tanke med bad_tree här ....
					bad_tree.put(testword)
					print("kör vi ? ")
					temp = Node(testword)
					temp.prev = parentword
					queue.put(temp)
					if testword == slut:
						return queue
			testword[i] = parentword[i]	

	
	rekursiv(start, slut, queue, alphabet, bad_tree,words)




def main():
	queue = LinkedQ()
	tree = createtree()
	

	uppgift1(tree[0],tree[1])


if __name__ == "__main__":
	main()
	# startword = input('Vilket ord vill du börja söka från ? ')
	# startword.lower()
	# endword = input('Vilket ord vill du sluta på? ')
	# startword.lower()



# class Node(object):        
#     def __init__(self, amount=1.00, currency=1, parent=None):
#         # breddenförst-trädsobjekt
#         self.amount = amount          # belopp
#         self.currency = currency      # valuta, SEK, USD,...
#         self.parent = None            # förälderpekare

# def makechildren(node):
#    # Skapar barn och lägger dom i kön


# #Inläsning av växlingskurserna 
# q = Queue()
# urmoder = Node() 
# q.put(urmoder)
# try:
#     while not q.isEmpty():
#         node = q.get()
#         makechildren(node)
#         # I makechildren görs "raise Klar(kedja)"
#     print("Ingen lönsam växling")
# except Klar as k: 
#     print("Växla fort:", k)