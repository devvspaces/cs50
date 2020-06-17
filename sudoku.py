import random
import string
import time
digits=[int(i) for i in list(string.digits)]

puzzle = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

def sudoku(t):
	new_p=[]
	for x in range(3):
		test=True
		#getting box, row and column
		box1=[]
		box2=[]
		for i in range(3*x,3*(x+1)):
			for a in t[i][0:3]:
				box1.append(a)
		#getting possible values
		nums=[i for i in digits if i not in box1]
		print(nums)
		rands=[]
		while test:
			w=nums
			y=True
			while y:
				random.shuffle(nums)
				if nums not in rands:
					rands.append(nums)
					y=False
			#setting empty values and getting thier positions
			box2=box1.copy()
			pos=[]
			for i in nums:
				for a,b in enumerate(box2):
					if b == 0:
						pos.append(a)
						box2[a]=i
						break
			#testing inserted values
			tests=[]
			rows=[[0,1,2],[3,4,5],[6,7,8]]
			cols=[[0,3,6],[1,4,7],[2,5,8]]
			for i in pos:
				v=box2[i]
				#getting row for position
				for a,b in enumerate(rows):
					if i in b:
						row=t[a+(3*x)]
				#getting col for position
				for a,b in enumerate(cols):
					if i in b:
						col=[j[a] for j in t]
				if v in box1 or v in row or v in col:
					tests.append(True)
			if True not in tests:
				test=False
				
				#Changing the value of the puzzle
				for p in pos:
					for a,r in enumerate(rows):
						if p in r:
							pow=a+(3*x)
					for a,c in enumerate(cols):
						if p in c:
							cow=a
					t[pow][cow]=box2[p]
	
	#displaying solved puzzle
	for i in t:
		print(i)
	
	
	

sudoku(puzzle)

ans=[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
print("********\n"*2)
for i in ans:
	print(i)
