lst = [1, 2, 3, 4, 5]
st  = (11, 22, 44, 33)

for i in range(len(st)):          # size mismatch fix
    if lst[i] == 3 and st[i] == 33:   # & → and, value fix
        print(lst[i], st[i])
print("nothing")



# lst = [1,2,3,4,5]
# st = (11,22,3,44)

# for i in range(min(len(lst), len(st))):
#     if lst[i] == 3 and st[i] == 3:
#         print(lst[i], st[i])
