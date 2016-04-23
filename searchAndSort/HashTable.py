class HashTable:
	def __init__(self):
		self.hashSize=11
		self.slots=[None]*self.hashSize
		self.data=[None]*self.hashSize


	def put(self,key,value):
		hashValue=self.hashFunction(key)

		if(self.slots[hashValue]==None):
			self.slots[hashValue]=key
			self.data[hashValue]=value
		elif(self.slots[hashValue]==key):
			self.data[hashValue]=value
		else:
			nextSlot=self.rehash(hashValue)
			stop=False
			while(self[nextSlot] != None and self[nextSlot] != key and not stop):
				if(nextSlot==hashValue):
					stop=True
				nextSlot=self.rehash(nextSlot)


			if(self.slots[nextSlot]==None):
				self.slots[nextSlot]=key
				self.data[nextSlot]=value
			else:
				self.slots[nextSlot]=key
				self.data[nextSlot]=value

	def hashFunction(self,key):
		return (key)%self.hashSize
	def rehash(self,hashValue):
		return (hashValue+1)%self.hashSize

	def get(self,key):
		hashValue=self.hashFunction(key)
		if(self.slots[hashValue]== key):
			return self.data[hashValue]
		else:
			currentHash = self.rehash(hashValue)
			found=False
			stop = False
			data = None
			while(self.slots[currentHash] != None and not found and not stop):
				if(self.slots[currentHash] == key):
					found=True
					data=self.data[currentHash]
				elif(currentHash == hashValue):
					stop=True
				else:
					currentHash=self.rehash(currentHash)

		return data


	def __getitem__(self,key):
		return self.get(key)


	def __setitem__(self,key,value):
		self.put(key,value)



H=HashTable()
H[0]=0
H[1]=1
H[2]=2
H[3]=3
H[4]=4
H[5]=5
H[6]=6
H[7]=7
H[8]=8
H[9]=9
H[10]=10
H[11]=20
print("Before")
print(H.slots)
print(H.data)
H[110]=220
print("After")
print(H.slots)
print(H.data)
print(H[11])
print(H[110])



