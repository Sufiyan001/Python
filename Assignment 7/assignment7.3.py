try:
    file = open("mbox.txt","r")
    output = []
    count = 0
    for lines in file:
        line = file.readline().rstrip()
        if line.startswith("From"):
            word = line.split()
            if len(word)>1:
                sender = word[1]
                print(sender)
                output.append(sender)
                count = count + 1
    print(f"Total {count} lines were printed.")
except:
    print("file is not found...")