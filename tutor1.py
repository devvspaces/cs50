data=[]
while n:
	x=input("Enter a new number: ")
	if len(x) == 0:
		break
	else:
		x=int(x)
		data.append(x)
avg=sum(data)/len(data)
avg=round(avg)
print(avg)