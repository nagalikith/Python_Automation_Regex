import re
def string_converter (given_string): 
    s = "A_WIRE_WRAP#(*) ?_wrapper(.IN(*), .OUT(?));"
    x = re.search("\[+", given_string)
    if x:
        y = re.split("\s", given_string)
        for i in y:
            if re.search("^ANA",i):
                try:
                    l = re.split("\[", i)
                    s = re.sub("\?",l[0],s)
                    if re.search("\:+",l[1]):
                        num = int(re.split("\:", l[1])[0]) + 1
                    else:
                        # Case it wont work if the value doesn't contain ":" and has more the 2 digits
                        num = int(l[1][0])
                    s = re.sub("\*", str(num), s, 1)
                except:
                    print ("A")
                    print(y)
            elif re.search("^db",i):
                try:
                    l = re.split("\[", i)
                    s = re.sub("\*",l[0],s)
                    num = int(re.split("\:", l[1])[0]) + 1
                    s = re.sub("\*", str(num), s, 1)
                except:

                    print ("B")
                    print (y)
    else:
        y = re.split("\s", given_string)
        for i in y:
            if re.search("^ANA",i):
                s = re.sub("\*","1",s,1)
                s = re.sub("\?",i,s)
            elif re.search("^db",i):
                s = re.sub("\*",i[:-1],s)
    return s
f = open("analog_converted.txt", "a")
with open('analog_assign.txt') as reader:
    line = reader.readline()
    while line!= '':
        f.write(string_converter(line)+'\n')
        line = reader.readline()
f.close()

