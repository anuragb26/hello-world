# generate all combinations of N items
def powerSet(items):
	N = len(items)
	# enumerate the 2**N possible combinations
	for i in range(2**N):
		combo = []
		for j in range(N):
			# test bit jth of integer i
			print("\ni {} and j {} and {}".format(i,j,i>>j))
			if (i >> j) % 2 == 1:
				print("in adding {}".format(items[j]))
				combo.append(items[j])
		yield combo

for item in powerSet(['a','b','c']):
	print(item)