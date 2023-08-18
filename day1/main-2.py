R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

m = []
print("Enter the elements")

for i in range(R):		 
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	m.append(a)

for i in range(R):
	for j in range(C):
		print(m[i][j], end = " ")
	print()
print("Diagonal elements")
for i in range(R):
    for j in range(C):
         if i == j:
            print(m[i][j],end=" ")
print("\nlower bound elements:")
for i in range(R):
    for j in range(C):
        if i>j:
            print(m[i][j],end=" ")
print("\nUpper bound elements:")
for i in range(R):
    for j in range(C):
        if i<j:
            print(m[i][j],end=" ")
print()            
    

            
