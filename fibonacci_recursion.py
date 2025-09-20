# def feb(n):
    
    
#     def start(n,a,b):
#         if n <0:
#             return a
#         # print(a,end=" ")
#         a,b = b,a+b
#         return start(n-1,a,b)

        
#     return(start(n-2,0,1))
# print(feb(5))
def feb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)
print(feb(5))
        