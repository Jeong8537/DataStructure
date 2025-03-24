array = [11, 9, -77, 8]
# print(f"{array[0]}, {id(array[0])}")
# print(f"{array[1]}, {id(array[1])}")
# print(f"{array[2]}, {id(array[2])}")
# print(f"{array[-1]}, {id(array[-1])}")
for i in range(len(array)):
    print(f"{array[i]}, {id(array[i])}")