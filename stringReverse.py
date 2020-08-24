s = "Sentence"
s = ''.join(sorted(s))
ds = ''
for i in s:
	ds = i + ds 
print(ds)

a = 12
for i in range(0, 7):
	for j in range(0, a):
		print(end=" ")
	a = a - 2
	for j in range(0, i+1):
		print("* ", end="")
	print()
	