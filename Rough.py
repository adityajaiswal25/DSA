# def rec(x):
#     if x ==0:
#         return
#     rec(x-1)
#     print(x)
# rec(4)
# ---------------------------------sum of n natural numbers-------------------
# def sum(s,i , n):
#     if i > n:
#         return s
#     s += i
#     return sum(s, i+1, n)
# print(sum(0,1,4))
# ---------------------------------sum of n natural numbers backtracking-------------------
# def f(n):
#     if n == 1:
#         return 1
#     return n + f(n-1)
# print(f(4))
# ---------------------------------factorial of a number-------------------
# def fact(n):
#     if n ==1 :
#         return 1
#     return(n*fact(n-1))
# print(fact(3))


# a = 5
# b = 10
# # print(f"a ={a}b ={b}")
# # a,b =b,a
# # print(f"a ={a}b ={b}")
# def array(arr,left,right):
#     if left>= right :
#         return arr
#     arr[left],arr[right] = arr[right],arr[left]
#     return array(arr,left+1,right-1)
# print(array([1,2,3,4,5],1,3))
     
# -------------------palindrome-------------------
# def pal(s):
#     t =""
#     for i in s:
#         t = i + t
#     if t == s:
#         return True 
#     return False
# print(pal("jack"))

# -------------------palindrome using recursion-------------------
# def pal(s):
#     t = ""
#     def rev (s,l,t):
#         if l<0:
#             return t
#         t = t + s[l]
#         return rev(s,l-1,t)
#     t = rev(s,len(s)-1,t)
#     if t == s:
#         return True 
#     return False
# print(pal("racecar"))
def pal(s):
    l = 0
    r = len(s)-1
    def rev (s,l,r):
        if l>=r:
            return True
        if s[l] != s[r]:
            return False
        return rev(s,l+1,r-1)
print(pal("racecar"))
       

        
    

        


    
    
    
    