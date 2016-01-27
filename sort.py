from array import array

tuple =[]
array1=[1,7,3]
array2=[4,5,6]
array3=[14,35,26]
array4=[19,25,126]
tuple.append(array1)
tuple.append(array2)
tuple.append(array3)
tuple.append(array4)

f = open("list","w")
for line  in sorted(tuple, key=lambda number: number[1]):
	for i in range(len(line)):
		print i
	        listToString = str(line[i])
		if i==len(line)-1: 
			listToString += "\n"
			print listToString
		else :listToString += "  "
		f.write(listToString)
	#for word in listToString.strip("[").strip("]").split(","):
	#	word.strip(" ")
	#	print word
	
