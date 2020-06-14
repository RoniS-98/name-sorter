names=list()

# membaca file unsorted list
filename='unsorted-names-list.txt'
with open(filename) as fin:
    for line in fin:
        names.append(line.strip())

# menyortir list
names.sort(key=lambda x: x.split(" ")[-1])
print(names)

#menulis hasil sorter pada file txt
filename='sorted-names-list.txt'
with open(filename,'w') as fout:
    for name in names:
        fout.write(name+'\n')
