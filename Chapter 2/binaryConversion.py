binaryNumber = int(input("Enter a 3 digit number: "))	
right = binaryNumber % 10   		
binaryNumber = binaryNumber // 10	
middle = binaryNumber % 10
binaryNumber = binaryNumber // 10
left = binaryNumber % 10
answer = (left*4) + (middle*2) + (right*1)
print(answer)

