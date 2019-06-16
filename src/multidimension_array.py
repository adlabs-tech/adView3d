import numpy as np 

list_a = [1, 2, 3, 4]

# array_a = np.array([list_a])

# # # print all data
# # print(array_a)

# # # slicing
# # print(array_a[1,:])

# # print(array_a[:,3])

# for i in range(5):
# 	array_a = np.append(array_a, [list_a], axis=0)

# print(array_a.shape)

a = np.zeros(shape=(2,3,4)) # Z, Y, X

# print(a)

a[0,0,:] = list_a

print(a)