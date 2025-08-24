n = int(input("Enter a number: "))
t = n
r = 0
c = 0
while(t >0):
    t = t//10
    c+=1
t = n
while(t > 0):
    r = r + (t%10)**c
    
    t = t//10
if(n == r):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
    