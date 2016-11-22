class Node(object):
	def __init__(self,value=None,nextNode=None):
		self.value=value
		self.nextNode=None

	def getNext(self):
		return self.nextNode

	def getData(self):
		return self.value

	def setNext(self,nextNode):
		self.nextNode=nextNode

	def __str__(self):
		return "data = "+ str(self.value) 


class LinkedList(object):
	
	def __init__(self,node=None):
		self.head=node

	def getHead(self):
		return self.head

	def insert(self,data):
		node=Node(data)
		node.setNext(self.head)
		self.head=node

	def size(self):
		count=0
		current=self.head
		while(current):
			current=current.getNext()
			count+=1

		return count

	def delete(self,data):
		previous=None
		current=self.head
		found=False
		while(current.getNext() !=None and found == False):
			if(current.getData()==data):
				found=True
			else:
				previous=current
				current=current.getNext()

		if(previous == None):
			self.head=current.getNext
		else:
			previous.setNext(current.getNext())

	def search(self,data):
		current=self.head
		found=False
		while(current.getNext()!=None and not found):
			if(current.getData() == data):
				found=True
			else:
				current=current.getNext()
		if not found:
			raise ValueError("Data not present in list")

	def __str__(self):
		res=[]
		current=self.getHead()
		while(current is not None):
			res.append(str(current.getData()))
			if current.getNext() is not None:
				res.append("->")
			current=current.getNext()
		return "".join(res)


def addTwoNos(l1,l2):
	
	resHead=None
	prev=None
	head1=l1.head
	head2=l2.head
	carry=0
	while(head1 is not None or head2 is not None):

		fData=head1.getData() if head1 is not None else 0
		sData=head2.getData() if head2 is not None else 0


		sum = fData + sData+carry
		carry=sum//10 if sum >= 10 else 0
		sum=sum%10 if sum >= 10 else sum
		temp=Node(sum)
		
		if resHead is None:
			resHead=LinkedList(temp)
		else:
			prev.setNext(temp)
		prev=temp
		#print("resHead is {}".format(resHead))

		if head1 is not None:
			head1=head1.getNext()
		if head2 is not None:
			head2=head2.getNext()
		

	if(carry > 0):
		temp.setNext(node(carry))

	print("output is {}".format(resHead))
	return resHead

def recursiveAddNodeHelper(curr1,curr2,currDiff,l1,l2):

	if(curr1==None and curr2==None):
		return (None,0)
	
	if(currDiff > 0):
		addL,carry=recursiveAddNodeHelper(curr1.getNext(),None,currDiff-1,l1,l2)
	elif(currDiff< 0):
		addL,carry=recursiveAddNodeHelper(None,curr2.getNext(),currDiff+1,l1,l2)
	else:
		curr1Next=l1 if curr1==None else curr1.getNext()
		curr2Next=l2 if curr2==None else curr2.getNext()
		addL,carry=recursiveAddNodeHelper(curr1Next,curr2Next,currDiff,l1,l2)

	d1=0 if curr1==None else curr1.getData()
	d2=0 if curr2==None else curr2.getData()
	s=(d1 + d2 +carry)%10
	c=(d1 + d2 + carry)//10

	currNode=Node(s)
	currNode.setNext(addL)

	return currNode,c

def getCount(n):
	c=0
	while(n is not None):
		n=n.getNext()
		c+=1
	return c

def printList(n):
	s=""
	while n is not None:
		s+=str(n.getData()) + "->"
		n=n.getNext()

	return s.strip("->")
def recursiveAddTwoNos(l1,l2):

	count1=getCount(l1)
	count2=getCount(l2)
	#print(l1)
	diff=count1-count2

	if(diff > 0):
		addL,carry=recursiveAddNodeHelper(l1,None,diff-1,l1,l2)
	elif(diff < 0):
		addL,carry=recursiveAddNodeHelper(None,l2,diff+1,l1,l2)
	else:
		addL,carry=recursiveAddNodeHelper(l1,l2,diff,l1,l2)
	if(carry ==1):
		cNode=Node(1)
		cNode.nextNode(addL)
		return cNode
	return addL
first = LinkedList()
second = LinkedList()
 
# Create first list
first.insert(6)
first.insert(4)
first.insert(9)
first.insert(5)
first.insert(7)
print("First List is  {}".format(first))
 
# Create second list
second.insert(4)
second.insert(8)
print("Second List is  {}".format(second))
print("Addition is {}".format(addTwoNos(first,second)))

aFirst=LinkedList()
aFirst.insert(7)
aFirst.insert(5)
aFirst.insert(9)
aFirst.insert(4)
aFirst.insert(6)


sFirst=LinkedList()
sFirst.insert(8)
sFirst.insert(4)

hFirst=aFirst.getHead()
hSecond=sFirst.getHead()

print("Actual first list is {}".format(aFirst))
print("Actual second list is {}".format(sFirst))
print("Addition is {}".format(printList(recursiveAddTwoNos(hFirst,hSecond))))




































