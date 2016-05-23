import abNester

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]


names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]

abNester.printRecursiveList(movies)
abNester.printRecursiveList(movies,True,0)
abNester.printRecursiveList(movies,True,4)

abNester.printRecursiveList(names)
