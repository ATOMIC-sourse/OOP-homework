from itertools import count
from operator import itemgetter
from pprint import pprint

list1 = []

def information(file):
    count = 0
    text = []
    with open(file, 'r', encoding='utf-8') as third:
        for lenth in range(100):
            data = third.readline().strip()
            if data != "":
                count += 1
            else:
                break
            text.append(data)
    list1.append([str(file), str(count), text])
    return [str(file), str(count), text]

(information("1.txt"))
(information("2.txt"))
(information("3.txt"))

list_sorted = sorted(list1, key=itemgetter(2), reverse=True)

with open("Done.txt", 'a', encoding='utf-8') as done:
        for inf in list_sorted:
            for string in inf:
                if type(string) == list:
                    for text in string:
                        done.write(text)
                        done.write('\n')
                else:
                    done.write(string)
                    done.write('\n')