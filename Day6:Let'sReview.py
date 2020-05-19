# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input().strip())
for i in range(0,T):
    S=input()
    even=S[::2]
    odd=S[1::2]
    print(even+' '+odd)
        
