fname = input("Enter file name: ")
fh = open(fname)
count = 0
nums = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    numfind = line.find('0')
    num = line[numfind:]
    numf = float(num)
    nums = nums + numf

mean = nums/count
print("Average spam confidence:", mean)
