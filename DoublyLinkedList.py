
class Node():
	def __init__(self,data,next, prev):
		self.data=data
		self.next=next
		self.prev=prev

class Linkedlist():
	head = None
	tail = None
	prev = None
	temp = None
	size = 0

	def append(self,data):
		node=Node(data, None, None)
		if self.head == None:
			self.head = self.tail = self.temp =node
			self.head.prev = None
			self.tail.prev = None
			#print self.head.data

		else:
			self.tail.next = node


		self.tail = node
		self.tail.prev = self.temp
		self.temp = self.tail
		#print self.head.prev
		self.head.prev = None


	def show(self):
		current_node = self.head
		#size = 0
		while current_node != None:
			print current_node.data
			#self.size = self.size + 1
			current_node = current_node.next


		# print 'Reverse assignment'
		# current_node = self.tail
		# while current_node is not None:
		# 	print current_node.data
		# 	#print current_node.prev
		# 	current_node = current_node.prev

	def get_size(self):
		current_node = self.head
		while current_node != None:
			
			self.size = self.size + 1
			current_node = current_node.next
		
	def remove(self, data):
		if self.head.data == data:
			self.head = self.head.next
			self.head.prev = None
			print '******Element Deleted*******'
			return
		current_node = self.head
		prev_node = None
		while current_node.next != None:
			if current_node.data == data:
				prev_node = current_node.prev
				prev_node.next = current_node.next
				current_node = current_node.next
				current_node.prev = prev_node
				print '******Element Deleted*******'
				return

			else:
				current_node = current_node.next

		if current_node.data == data:
			prev_node = current_node.prev
			prev_node.next = None
			print '******Element Deleted*******'
			return

		print '*******Element Not Found********'

	def insert(self, position, data):
		if position < 1:
			print 'Invalid index'
			return
		print self.size
		if self.size + 2 > position:
			place = 2
			node = Node(data, None, None)
			

			if position == 1:
				current_node = self.head
				node.next = current_node
				current_node.prev = node
				self.head = node
				return
			current_node = self.head.next
			if self.size > position:
				while current_node != None:
					if position == place:
						prev_node = current_node.prev
						node.next = current_node
						current_node.prev = node
						node.prev = prev_node
						prev_node.next = node

						return
					place = place + 1
					current_node =current_node.next

			current_node = self.tail
			node.prev = current_node
			current_node.next = node
			self.tail = node
			return
		else:
			print '\nInvalid index\n'





print 'Developed by Anant and Shreyas\n'

s = Linkedlist()
s.append(3)
s.append(5)
s.append(59)
s.append(50)
s.append(55)
#s.show()

#s.remove(55)
#s.show()
print 'Enter the position'
position = int(raw_input())
print 'Enter the data'
data = int(raw_input())
s.get_size()
s.insert(position, data)
print 'List with the new element\n'
s.show()