from itertools import count
from operator import itemgetter
from pprint import pprint

def information(file):
    count = 0
    list3 = []
    with open(file, 'r', encoding='utf-8') as third:
        for lenth in range(100):
            data = third.readline().strip()
            if data != "":
                count += 1
            else:
                break
            list3.append(data)
    return [str(file), str(count), list3]

list1 = []
list2 = []
def who_first_inf(file):
    information(file)
    list1.append(information(file)[1])
    list1.sort()
    # for i in list1:
        # if i in information(file):
            # print(information(file))
    # if list1[0] in information(file)[1]:
    #     print(information(file))

who_first_inf('1.txt')
who_first_inf('2.txt')
who_first_inf('3.txt')

# print(list2)

list2.append(information('1.txt'))
list2.append(information('2.txt'))
list2.append(information('3.txt'))
# list2.sort()
sorted(list2, key=itemgetter(0))

pprint(list2)
# def write_done(file):
#     with open("Done.txt", 'a', encoding='utf-8') as done:
#         for i in information(file):
#             if type(i) != list:
#                 done.write(i)
#                 done.write('\n')
#             else:
#                 for o in i:
#                     done.write(o)
#                     done.write('\n')
#
#
# pprint(information("1.txt"))
# pprint(information("2.txt"))
# pprint(information("3.txt"))

