# Write a program to print 1 to n armstrong number using lsit comprehension.

def armstrong(n):
   res=0
   while n!=0:
         r=n%10
         n=n//10
         res=res+r*r*r
   return res
n=int(input())
temp=n
l=[i for i in range(1,n+1) if i==armstrong(i)]
for i in l:
   print(i,end=' ')

