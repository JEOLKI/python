
for i in range(5):
    print(i)


print("\n*** 2단 ***")

for i in range(1,10):
    print("2 * {} = {}" .format(i, 2 * i))


print("\n*** 구구단  ***")

for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}" .format(i, j, i * j))
        
