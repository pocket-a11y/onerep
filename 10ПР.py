#1
n = 5
a = []
with open("vvod.txt") as file:
    for line in file:
        arr = [int(x.strip()) for x in line.split()]
        a.append(arr)

for i in a:
     print(*i)

for i in range(n):
    a[i][0], a[i][-1] = a[i][-1], a[i][0]
print('_'*10)
arr = a
file_v = open('vivod.txt','w')
file_v.write(str(arr))
file_v.close()
for i in arr:
    print(*i)