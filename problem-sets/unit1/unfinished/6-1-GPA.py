
list =[]
individual = []
dict = {}
number_of_classes = 0

f = open('../../inFile.txt', 'r')
for i in f.readlines():
    list.append(i)
    list[-1] = list[-1].strip()
f.close()



for i in range(len(list)):
    # print (len(list[i].split()))
    number_of_classes = int(((len(list[i].split())) - 1) / 3)
    # print (number_of_classes)
    # print (list[i])
    # print (list[i].split())
    individual.append(list[i].split())

print(individual)

for m in range(len(individual)):
    num = int((len(individual[m])))
    print(num)
    id = individual[m][0]
    dict.update({id: individual[m][1]})
    # for z in range(num):




print(dict)









