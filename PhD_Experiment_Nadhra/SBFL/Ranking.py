import time
def f1(text):
    name, _,num = text.partition(',')
    return float(num)

with open("input.txt", "r") as file, open("output.txt", "a") as my_output:
    #start
    start = time.time()
    count = 0 
    l = file.read().splitlines()
    l.sort(key=f1, reverse=True)
    for line in l:
        count+=1
       # x = l
        x = l[:10]
#my_output.write(x)
print(x)
print ("Done in :%ss" % (time.time() - start))
