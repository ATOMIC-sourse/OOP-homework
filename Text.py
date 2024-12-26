from itertools import count

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

with open("Done.txt", 'a', encoding='utf-8') as done:
    for i in information("1.txt"):
        if type(i) != list:
            done.write(i)
            done.write('\n')
        else:
            for o in i:
                done.write(o)
                done.write('\n')

    for i in information("2.txt"):
        if type(i) != list:
            done.write(i)
            done.write('\n')
        else:
            for o in i:
                done.write(o)
                done.write('\n')

    for i in information("3.txt"):
        if type(i) != list:
            done.write(i)
            done.write('\n')
        else:
            for o in i:
                done.write(o)
                done.write('\n')