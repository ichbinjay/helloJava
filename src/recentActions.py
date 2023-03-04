'''
works for sample cases, gives TLE for some cases
ip:
10
1 1
2
3 2
5 4
4 5
5 9 9 5 7
5 5
6 7 8 9 10
3 4
4 4 4 4
4 4
5 5 6 6
3 5
4 5 5 5 4
4 20
5 5 24 24 24 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20
5 7
7 8 7 11 7 12 10
6 7
8 11 7 8 8 8 12

op:
1 
-1 2 1 
-1 5 2 1 
5 4 3 2 1 
-1 -1 1 
-1 -1 3 1 
-1 2 1 
8 7 3 1 
7 6 4 2 1 
-1 -1 7 3 2 1 
'''
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	a = [int(x) for x in range(1, n+1)]
	p = [int(x) for x in input().split()]
	res = {x: -1 for x in a}
	count = 0
	pop_count = 0
	for i in p:
		if pop_count == n:
			break
		count += 1
		if i in a:
			ind = a.index(i)
			a[1: ind+1] = a[:ind]
			a[0] = i
		else:
			res[a[-1]] = count
			a.pop()
			pop_count += 1
			a.insert(0, i)
	print(*res.values(), sep=" ")


