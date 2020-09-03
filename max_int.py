
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
#Algorithm to find the highest integer by user input
#We check if user input is higher than the user input before and replace
#that number if it is, but leave it as is if it isn't
while num_int > 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    else: continue

print("The maximum is", max_int)    # Do not change this line