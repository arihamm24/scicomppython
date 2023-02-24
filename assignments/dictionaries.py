#iteration1: i plan to revisit this program and rework
name = input("Enter file:")
if len(name) < 1: #remove if statement, just allow file entry
    name = "mbox-short.txt"
handle = open(name)
sends = dict()
for line in handle: 
    if line.startswith("From") and not line.startswith("From:"): #parsing w/diff files or lines?
        sender = line.split()
        addy = sender[1] #targets email addresses in file
        if addy in sends:
            sends[addy] = sends[addy] + 1
        if addy not in sends:
            sends[addy] = 1
if sends[addy] > 4: #what if max value unknown?
    print(addy, sends[addy]) 
