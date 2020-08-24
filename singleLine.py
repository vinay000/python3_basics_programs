#taking input in single line
x,y = input().split();
l = list(map(int, input().split()));
print("x-->" + str(x) + "  y---->" + str(y))
print(l)


#printing output in single line  where end = seperator
for i in range(0,10):
	print(i, end="")