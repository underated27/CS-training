s=int(input("Enter the size of array:"))
array= []
for i in range(s):
     e=int(input(f"Enter element:"))
     array.append(e)
count = 0
for i in range(s):
        if array[i] != 0:
          array[count] = array[i]
          count += 1
while count < s:
        array[count] = 0
        count += 1
print("The resulting array is:",array)
    

            
