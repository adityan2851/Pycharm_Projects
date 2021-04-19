list = [1, 3, 5, 6]
target = int(input(""))

if target in list:
    index = list.index(target)
    print(index)

else:
    for i in range(0, 4):
        if list[i] > target:
            print(i)
            break
        if list[len(list) - 1] < target:
            print(len(list))
            break
