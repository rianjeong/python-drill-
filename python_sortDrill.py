num_list = [67,45,2,13,1,988]
new_list = []

while num_list:
    minimum = num_list[0]
    for x in num_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    num_list.remove(minimum)

print (new_list)

num_list1 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
new_list1 = []

while num_list1:
    minimum = num_list1[0]
    for x in num_list1:
        if x < minimum:
           minimum = x
    new_list1.append(minimum)
    num_list1.remove(minimum)

print (new_list1)
