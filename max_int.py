num_int = int(input("Input a number: "))
max_int=0
while num_int > 0:
    max_int = max(num_int, max_int)
    num_int = int(input("Input a number: "))    # Do not change this line
print("The maximum is", max_int)    # Do not change this line
