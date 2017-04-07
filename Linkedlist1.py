class Node(object):

	def __init__(self, data, num,next):
		self.data=data
		self.num=num
		self.next=next


class Linkedlist(object):
	head=None
	tail=None
	def append(self, data,num):
	 	node=Node(data, num,None)
	 	if self.head is None:
	 		self.head=self.tail=node
	 	else:
	 		self.tail.next= node
	 	self.tail= node
	def show(self):
	 	current= self.head
	 	while current is not None:
	 		print(current.data,current.num)
	 		
	 		current= current.next
	 	print("Done")

	def remove(self, value):
	 	temp=0
	 	current=self.head
	 	prev=None
	 	while(current is not None):
	 		if  current.data==value:

	 			if prev is not None:
	 				prev.next=current.next
	 				temp=1
	 			else:
	 				self.head=current.next
	 				temp=1
	 		prev=current
	 		current=current.next
	 	if temp == 1:
	 		print("Element deleted")
	 	else:
	 		print("Element Not found")
	 	
      
           
s=Linkedlist()
print("Select one of the choice")
y, z = 'Y','Y'
while(y==z):
	print("1- Append 2- Show 3- To delete")
	a=int(input())
	if a==1:
		print("Enter the Contact details")
		c=input()
		d=input()
		s.append(c,d)

	if a==2:
		s.show()

	if a==3:
		print("Enter a data to remove")
		a=input()
		s.remove(a)
		s.show()
	print("Do u wish to continue")
	z=input()	

