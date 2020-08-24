l = [11,5,88,61,22,1,22,8]

for round in range(1,len(l)):
	for i in range(0,len(l)-round):
		if(l[i]>l[i+1]):
			#swap
			temp = l[i]
			l[i] = l[i+1]
			l[i+1] = temp
print("the sorted array" + str(l))
print(l)
