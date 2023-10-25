file = open("mbox.txt","r")
count = 0
for line in file:
    if line.startswith("From:"):
        line = line.rstrip()
        position = line.find("@")
        host = line[position+1:]
        count = count + 1
        print(host)
print("total %d host found."%count)