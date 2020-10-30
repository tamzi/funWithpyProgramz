## This is an Alogorithm that will take in an input of integers
# It then adds all the elements in the arrays(List).

input_string = input("Enter some numbers separated by space: ")

print("\n")
inputList = input_string.split()
print("The list created is ", inputList)

# This bit Calculates the sum of teh list elements
sum1 = 0
for num in inputList:
    sum1 += int(num)
print("Sum = ", sum1)