low = 1000
max = 5000
count = 0

print("Second prime number between" , low , "and" , max , "is: ")
for x in range(low, max + 1):
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        count = count + 1
        if count == 1:
            continue
        print(x)
        if count == 2:
            break