list = []

n = int(input(""))
for i in range(0, n):
    number = int(input())
    list.append(number)

print(list)
flag = False

for i in range(0, n):
    number1 = list[i] #2 i=7
    for j in range(i, n):
        if number1 == list[j] and number1: #2 == 2
            if flag:
                list[j] = 0
                flag = False
                print(list)
                continue

            else:
                flag = True

print(list)
