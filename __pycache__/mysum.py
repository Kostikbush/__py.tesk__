def mysum(L): # Использует расширенную
	first, *rest = L # операцию присваивания
	return first if not rest else first + mysum(rest)

def sums(L):
	tot = 0
	for x in L:
		if not isinstance(x, list):
			tot+=x
		else:
			tot+=sums(x)
	return tot


