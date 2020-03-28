list = [0,1]

number = int(input("What number would you like to go to? "))

if number >= 1:
    print(list[0])
if number >= 2:
    print(list[1])

while len(list) < number:
    f = list[-1] + list[-2]
    list.append(f)
    print(f)