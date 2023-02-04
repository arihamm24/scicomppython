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

#Pulling emails from document, ommitting duplicate properties
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
count = 0

fh = open(fname)
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        word = line.split()
        count = count + 1
        print(word[1])
print("There were", count, "lines in the file with From as the first word")
