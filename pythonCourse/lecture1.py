import pprint

class Food(object):
	def __init__(self,n,v,c):
		self.name=n
		self.value=v
		self.calories=c
	def getValue(self):
		return self.value
	def getCost(self):
		return self.calories
	def getDensity(self):
		return self.getValue()/self.getCost()
	def __str__(self):
		return self.name + ': <' + str(self.value)\
				+ ',' + str(self.calories) + '>'
	def __repr__(self):
		return self.__str__()


def greedy(items,maxCost,keyFunction):

	itemsCopy=sorted(items,key=keyFunction,reverse=True)
	print("Items Copy")
	pprint.pprint(itemsCopy)
	totalCost,totalVal=0.0,0.0
	result=[]
	for i in range(len(itemsCopy)):
		if(totalCost + itemsCopy[i].getCost() < maxCost):
			result.append(itemsCopy[i])
			totalCost+=itemsCopy[i].getCost()
			totalVal+=itemsCopy[i].getValue()
	return result,totalVal

def greedyResult(items,constraint,func):
	result,val=greedy(items,constraint,func)
	print("Result : {0}".format(val))
	pprint.pprint(result)


def greedyTest(items,maxCost):
	print('Use greedy by value to allocate', maxCost,
          'calories')
	greedyResult(items,maxCost,Food.getValue)
	print('\nUse greedy by cost to allocate', maxCost,
          'calories')
	greedyResult(items,maxCost,lambda x:1/Food.getCost(x))
	print('\nUse greedy by density to allocate', maxCost,
          'calories')
	greedyResult(items,maxCost,Food.getDensity)

def buildMenu(names,values,calories):
	menu=[]
	for i in range(len(values)):
		menu.append(Food(names[i],values[i],calories[i]))
	return menu

def maxVal(items,avail):
	if(items==[] or avail <=0):
		print ("In blank")
		result=(0,())
	elif(items[0].getCost() > avail):
		print("In higher Cost for {}".format(items[0]))
		result=maxVal(items[1:],avail)
	else:
		print("In choosin for {}".format(items[0]))
		chosenOne=items[0]
		#take the first item
		withVal,valToTake=maxVal(items[1:],avail-chosenOne.getCost())
		withVal+=chosenOne.getValue()
		#don't take the first item
		withoutVal,valNotTaken=maxVal(items[1:],avail)
		#choose the better option
		if withVal> withoutVal:
			print ("choosing {}".format(items[0]))
			result=(withVal,valToTake+(chosenOne,))
		else:
			print("Not choosing {}".format(items[0]))
			result=(withoutVal,valNotTaken)
	return result


def maxValHelper(items,constraint):
	print('Use search tree to allocate {} calories'.format(constraint))
	val,itemsTaken=maxVal(items,constraint)
	print("Value {0}".format(val))
	pprint.pprint(itemsTaken)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
print("Food")
pprint.pprint(foods)
#greedyTest(foods,750)
maxValHelper(foods,200)


