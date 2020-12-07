fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()

for line in fh:
    if line.startswith("From "):
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if '@' in word:
        if bigcount is None or count > bigcount:
            bigcount = count
            bigword = word

print(bigword,bigcount)
