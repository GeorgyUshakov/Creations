r_1 = [1]
r_2 = [1, 2, 1]

list = [r_1, r_2]

number = int(input("Which row would you like to go to? "))

if number >= 1:
    print(list[0])
if number >= 2:
    print(list[1])

while len(list) < number:
    r = [1]
    a = list[-1]
    n = 0
    while n < len(a)-1:
        r.append(a[n] + a[n+1])
        n += 1
    r.append(1)
    list.append(r)
    print(r)