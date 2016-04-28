
cast=["Cleese","Palin","Jones","Idle"]

cast.extend(["Gilliam","Chapman"])

cast.remove("Chapman")

cast.insert(0,"Chapman")

#print(cast)


movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]

#print(movies)

movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)

#print(movies)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

#print("Nested lists")
#print(movies)


#for each_item in movies:
	#if(isinstance(each_item,list)):
	#	for nested_item in each_item:
	#		print(nested_item)
	#else:
		#print(each_item)



def recursivePrintLists(entity):
	if(not isinstance(entity,list)):
		print(entity)
	else:
		for each_item in entity:
			recursivePrintLists(each_item)




recursivePrintLists(movies)






