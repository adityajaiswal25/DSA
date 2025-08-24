import math
n = int(input("Enter a number: "))
result = []
# for i in range(1,( n//2)+1):
#     if(n%i == 0):
#         result.append(i)
# result.append(n)
        
# print("The factors of", n, "are", result)
for i in range(1,int((math.sqrt(n)+1))):
    if(n%i == 0):
        result.append(i)
        if i != int(math.sqrt(n)):
            result.append(n//i)

result.sort()
print("The factors of", n, "are", result)
        
          
