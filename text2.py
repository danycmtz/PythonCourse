fname = input("Enter file name: ")
fh = open(fname)
count = 0
listnum = list()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    numfind = line.find('0')
    num = line[numfind:]
    numf = float(num)
    listnum.append(numf)

mean = sum(listnum)/len(listnum)
print(listnum)
print("Average spam confidence:", mean)
