# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d=dict()

for _ in range(0,n):
    name,number = input().split()
    d[name]=number
for _ in range(0,n):
    try:
        name = input()
        #print (name)
        if name in d:       
            print("{}={}".format(name,d[name]))        
        else:
            print ("Not found")
    except:
        break
