n = int(input("Enter a number: "))
t = n
r = 0
while(t > 0):
    r = (r*10 ) +  (t%10)
    
    t = t//10 
if(n == r):
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")

    