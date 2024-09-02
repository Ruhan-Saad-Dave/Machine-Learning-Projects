import numpy as np
arr = np.array([12, 34, 56, 78])
print(arr)
print(type(arr))

#the array will change the data type accoring to the data type of the elements
print(arr[1:4])

arr1 = np.arange(1, 11, 2)
print("arr1:\n", arr1)

arr2 = np.ones([10, 2])
print("arr2:\n", arr2)

arr3 = np.zeros([10, 2])
print("arr3:\n", arr3)
print("Dimensions:\n", arr3.ndim)
print("Shape:\n", arr3.shape)
print("Size:\n", arr3.size)

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("arr4:", arr4)
print("element at 1st row 2nd column:\n", arr4[0][1])
print("elements of 1st to 3rd row and 2nd to 3rd column:\n", arr4[0:3, 1:4])
print("arr4[1:3, :] = \n", arr4[1:3, :])
print("Before dimensions:", arr4.shape)
print("after reshaping into (3:4)=\n", arr4.reshape(3, 4))
#the reshape size should have the same number of elements
print("Convert into 3D=\n", arr4.reshape(3,2,2))
print("Shape:", arr4.reshape(3,2,2).shape)
print("reshaping with one dimension unknown:\n", arr4.reshape(6, -1))
print("arr4=\n", arr4)

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
arr6 = np.array([[9, 8, 7], [6, 5, 4]])
print("arr5:\n", arr5)
print("arr6:", arr6)
print("addition:\n", arr5 + arr6)
print("subtraction:\n", arr5 - arr6)
print("multiplication:\n", arr5 * arr6)
print("matrix multi:\n", arr5 @ arr6.T)
arr7 = np.array([[1, 2, 3], [4, 5, 5], [7, 8, 9]])
print("arr7:\n", arr7)
print("determinant of arr7:\n", np.linalg.det(arr7))
print("inverse of arr7:\n", np.linalg.inv(arr7))

arr8 = np.array([23, 23, 23, 4, 5, 6, 4])
print("arr8:\n", arr8)
print("unique elements:\n", np.unique(arr8))

print("minimum element:", np.min(arr))
#print("mode of arr8:", np.mode(arr)[0])