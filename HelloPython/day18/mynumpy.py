import numpy as np
data = np.load("x_train.npy")
#print(data)

for i in data :
    print("--------------------------------------------------------------------------")
    for j in i :
        line = ''
        for k in j :
            if k > 1:
                k = 1
            elif k == 0 :
                k = 0
            line += str(k)
        print(line)