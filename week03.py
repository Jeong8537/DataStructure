import array
arr = array.array('f',[11, 9, -77, 8])
# print(f"{array[0]}, {id(array[0])}")
# print(f"{array[1]}, {id(array[1])}")
# print(f"{array[2]}, {id(array[2])}")
# print(f"{array[-1]}, {id(array[-1])}")
for i in range(len(arr)):
    print(f"{arr[i]:3}, {id(arr[i])}")

