
def increase(a):
    a += 1

def increaseRef(a):
    a[0] += 1

a = 1
b = [3]    
    
print(a)
print(b[0])

increase(a)
increaseRef(b)    
    
print(a)
print(b[0])