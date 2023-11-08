try:
    open_file = open("romeo.txt","r")
    unique_list = []
    for line in open_file:
        lines = open_file.readline().rstrip()
        words = lines.split()
        for word in words:
            if word not in unique_list:
                unique_list.append(word)
    unique_list.sort()
    print(unique_list)
except:
    print("The file is not exist...")

