#############
##### Labb 2
##### Länkad lista
##### Mikael Sjöstedt & Alexander Ramm



class Node():
	def __init__(self, value = None):
		self.value = value
		self.next = None
		self.prev = None

	def printout(self):
		return self.value


class LinkedQ():
	#Linked LIST
	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	def put(self, listinput):
	# lägger till en nod nest i listan
		self.length += 1
		new = Node(listinput)

		if self.head == None:
			self.head = new
			self.tail = new

		else:
			self.tail.next = new
			new.prev = self.tail
			self.tail = new

	def get(self):
	# tar bort den första noden i listan
		#self.lenght = self.lenght - 1

		if self.length > 1:
			self.length = self.length - 1
			first = self.head
			temp = self.head.next
			temp.prev = None
			self.head = temp

			return first

		elif self.length == 1:
			self.length = self.length - 1
			first = self.head
			self.head = None
			self.tail = None

			return first

		else:
			return []



	def isEmpty(self):
	# kollar om det finns några noder
		if self.length == 0:
			return True
		else:
			return False

	def __str__(self):
		tmp=self.head
		the_list = []
		for i in range (self.length):
			the_list.append(tmp.value)
			tmp = tmp.next
		return str(the_list)



def main():
	trollkarl()


def trollkarl():
	lista = input('Vilken ordning ligger korten i? (mellanslag för att skilja)')
	#print(lista)
	
	lista = lista.split()
	
	#print(lista)

	t = LinkedQ()
	# Lägger in alla element i listen i den ordningen de skrevs in
	for i in range(len(lista)):
		t.put(lista[i])
	# Plockar ut den översta och printar
	print (t)
	for i in range(t.length):
		t.put(t.get())
		print(t.get())

if __name__ == "__main__":
	main()