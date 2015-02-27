##################
### Labb 4
### Mikael Sjöstedt & Alexander Ramm
### version 3

from bintreeFile import *
from LinkedQFile import *
from string import ascii_lowercase
from pythonds.graphs import Graph
import queue

class Nod(object):        
    def __init__(self,value = None):
        # breddenförst-trädsobjekt
        self.value = value          # ord
        self.parent = None            # förälderpekare


def createtree(prog):
	#Skapar träd med alla ord från word3.txt
	# Returnar ett träd med alla ord
	tree = Bintree()
	duplicate_tree = Bintree()
	
	with open(prog, "r", encoding = "utf-8") as fil:
	    for rad in fil:
	        ordet = rad.strip()                # Ett trebokstavsord per rad
	        if tree.exists(ordet):
	            #duplicate_tree.put(ordet) 
	            pass
	        else:
	            tree.put(ordet)             # in i sökträdet
	return (tree)	

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

def result_list(li,word):
	#Prints order of the words and returns a list with the words aswell
	if word != None:
		try:
			iterword = result_list(li, word.parent.value)
			li.append(word.value)
			
			print(word.value, end = " ")
			return (li, word.value)
			
		except AttributeError:
			print(word.value, end = " ")
			li.append(word.value)
			return(li, word.value)
		finally:
			pass


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:

        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)

    return g

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = LinkedQ()
  vertQueue.put(start)
  while (vertQueue.length > 0):
    currentVert = vertQueue.get()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.put(nbr)
    currentVert.setColor('black')


def makechildren(start, slut, parentqueue, alphabet, bad_tree,words):
	#for x in range(parentqueue.length):
	while not parentqueue.isEmpty():
	
		parentwordNode = parentqueue.get()
		#print(parentwordNode.value.value)
		parentword = list(parentwordNode.value.value) # Läser in ett ord från kön
		testword = list(parentwordNode.value.value)
		
		
		for i in range(len(parentword)):
			for k in range(len(alphabet)):
				testword = list(testword)
				#print (testword)
				testword[i] = alphabet[k]			## Byter ut en bokstav i ordet från kö 
				

				
				testword = "".join(testword)
				testword = str(testword)			## Gör om det till en string efter att ha varit en lista
				
				if words.exists(testword) and not bad_tree.exists(testword): #Om det nya ordet finns skapas en nod med det ordet tillsammans med pekare till förälder
					
					bad_tree.put(testword)
					current = Nod(testword)
					current.parent = parentwordNode
					parentqueue.put(current)
					if testword == slut:
						print ("Det finns en väg till", slut)
						return current

			testword = list(testword)
			testword[i] = parentword[i]
			longest = current
	
	print("Hittade INGEN väg från", start, "till", slut)
	print("Men, den längsta vägen till", start, " är: ")
	return longest

	
	# Kan även göras rekursivt genom att byta ut while not till for x in range(parentqueue.length) och ta bort kommentaren nedan
	#recursive = makechildren(start, slut, parentqueue, alphabet, bad_tree,words)
	#return recursive

def uppgift123():
	#Uppgift 1 till 3. Frågar om man vill köra word3 eller word5
	queue = LinkedQ()

	prog = input("Vilket program vill du köra, word3 eller word5? (1/2): ")

	state = True
	while state:
		try:
			prog = int(prog)
			if prog>0 and prog<3:
				state = False
			else:
				prog = input("Inte ett giltigt val, välj igen:  ") 
		except ValueError:
			prog = input("Inte ett giltigt val, välj igen:  ")
	if prog == 1:
		prog = "word3.txt"
	else:
		prog = "word5.txt"

	tree = createtree(prog)
	

	uppgift1(tree,prog)
	print ("\n")

def uppgift1(words, prog):
	# Breddenförst sökning mellan orden start och slut
	
	## Create initial values
	print ("\n")
	temp = None
	queue = LinkedQ()
	bad_tree = Bintree()

	#Lista med alfabetet
	L = list(ascii_lowercase)
	L= L + ["å", "ä", "ö"] # Lägger till non ascii

	print ("Du letar nu efter vägar i ",prog)
	start = input("Vilket ord vill du starta på? ")
	slut =  input("Vilket ord vill du sluta på? ")
	start = start.lower()
	slut = slut.lower()
	print("\n")

	bad_tree.put(start)

	temp = Nod(start)
	queue.put(temp)
	
	foo = makechildren(start, slut, queue, L, bad_tree, words)
	li = []
	result = result_list(li, foo)
	print ("\n")
	#print (result[0])

def uppgiftC():
	# g = buildGraph("word5.txt")
	# #print(type(g))

	# for v in g:
	# 	for w in v.getConnections():
	# 		print("(%s , %s )" % (v.getId() , w.getId()))
	
	#bfs(g, g.getVertex("söt"))
	####
	##Printgrej
	#traverse(g.getVertex('sur'))
	g = buildGraph('word3.txt')
	g_bfs = bfs(g, g.getVertex('söt'))
	v = g.getVertex('sur')
	while v != None:
		print(v.id)
	v = v.getPredicate()

	

def main():

	#uppgift123()
	uppgiftC()

 



if __name__ == "__main__":
	main()
