fname = input("Enter file name: ")
fh = open(fname)
count = 0 
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find('0')
        count = count + 1
        num = num + float(line[index:])
        avg = num/count 
print("Average spam confidence:", avg)
