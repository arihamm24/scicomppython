#Sorting a line from Romeo & Juliet, omitting repeated words
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for x in words: #loop checks list content
        if x not in lst:
            lst.append(x)
lst.sort()
print(lst)
