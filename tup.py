fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()

for line in fh:
    if line.startswith("From "):
        words = line.split()
        for word in words:
            if ':' in word:
                word = word[:2]
                counts[word] = counts.get(word,0) + 1

newtup = sorted( [ (k,v) for k,v in counts.items() ])

for k,v in newtup:
    print(k,v)
