with open("3.txt", 'r', encoding='utf-8') as third:
    list3 = []
    count = 0
    for lenth in range(100):
        data = third.readline().strip()
        if data != "":
            count += 1
        else:
            break
        list3.append(data)
    print('1.txt')
    print(count)
    for l in list3:
        print(l)


# with open("2.txt", 'r', encoding='utf-8') as second:
#     list2 = []
#     count = 0
#     for lenth in range(100):
#         data = second.readline().strip()
#         if data != "":
#             count += 1
#         else:
#             break
#         list2.append(data)
#     print('1.txt')
#     print(count)
#     for l in list2:
#         print(l)

# with open("1.txt", 'r', encoding='utf-8') as first:
#     list1 = []
#     count = 0
#     for lenth in range(100):
#         data = first.readline().strip()
#         if data != "":
#             count += 1
#         else:
#             break
#         list1.append(data)
#     print('1.txt')
#     print(count)
#     for l in list1:
#         print(l)

# with open("Done.txt", 'a', encoding='utf-8') as done:
#     with open("1.txt", 'r', encoding='utf-8') as first:
#         list1 = []
#         count = 0
#         for lenth in range(100):
#             data = first.readline().strip()
#             if data != "":
#                 count += 1
#             else:
#                 break
#             list1.append(data)
#         print('1.txt')
#         print(count)
#         for l in list1:
#             print(l)

    # done.write(str("1.txt\n"))
    # done.write(str(count))
