
logfile=open("c:/Users/Satsan/Documents/password vm.txt",'r') # path should be yours
for line in logfile:
    line_split=line.split()
    print(line_split)
    list = line_split[0],line_split[1],line_split[2],line_split[3]
    print(list)