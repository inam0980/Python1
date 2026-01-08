print("Hello World")

lst = []
n = int(input("Enter your size of list: "))

for i in range(n):
    lst.append(int(input()))



print(*lst)

print(type(lst))