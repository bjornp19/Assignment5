n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1=0
num2=1
num3=2
print(num1)
print(num2)
print(num3)
for i in range(n):
    next_num= num1 + num2 + num3
    print(next_num)
    num1 = num2
    num2 = num3
    num3 = next_num
    