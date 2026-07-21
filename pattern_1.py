# for i in range(1,6):
#     for j in range(1,7):
    
#         print("*", end=" ")
#     print()




# for i in range(1,6):
#     for j in range(1,7):
#         print("*",end=" ")
#     print()



# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# n=5
# for i in range(n,0,-1):
#     print( '*' * i)




# for i in range(6):
#     for j in range(7):
#         if i==0 or i==5 or j==0 or j==6:
#             print('*',end= ' ')
#         else:
#             print('$',end=" ")
#     print()







# a = ["mango", "banana", "apple"]
# count = 0
# for i in a:
#     if count == 0:
#         print(i[0])
#     count += 1




# a=["mango","banana","orange"]
# b={i: a.count(i) for i in a}
# print(b)







# pyramid

n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2 * i-1):
#         print("*",end=" ")
#     print()






# reverese pyramid

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2* i-1):
#         print("*",end=" ")
#     print()





# reverse triangle


# n = 5
# for i in range(n):
#     for j in range(n):
#         if j >= n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()





# oppisite triangle

# n=5
# for i in range(n):
#     for j in range(n):
#         if j >=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()








# armstrong 

# n=int(input("enter your number"))
# p=len(str(n))
# temp=n
# s=0
# while temp>0:
#     a=temp%10
#     s+=a**p
#     temp=temp//10
# if s==n:
#     print("this is a armstrong number")
# else:
#     print("this is not a armstrong number")





# factorial

# n=int(input("enter your factorial number"))

# fact=1
# for i in range(1,n+1):
#     fact=i
# print(fact)




# def my_factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# n = int(input("Enter your factorial number: "))
# result = my_factorial(n)
# print(result)





# recursive


# n=int(input("enter your number"))
# def my_fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*my_fact(n-1)
# print(my_fact(5))





# sum=0
# for i in range(11):
#     sum+=i
# print(sum)





# sum=0
# for i in range(11):
#     sum+=i**2
# print(sum)


# first 10 numbers lo even ki square kattali odd ki cube kattali vere vere  sum tho 





# even_sum = 0
# odd_sum = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         even_sum += i ** 2     
#     else:
#         odd_sum += i ** 3      
# print(even_sum)
# print(odd_sum)









# even_sum = 0
# odd_sum = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, "->", i**2)
#         even_sum += i**2
#         print()
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i, "->", i**3)
#         odd_sum += i**3
# print("Even Square Sum =," "even_sum")
# print("Odd Cube Sum  =," "odd_sum")







# n=153
# t=n
# p=len(str(n))
# s=0
# while t>0:
#     x=t%10
#     s+=(x**p)
#     t=t//10
# if s==n:
#     print("this is an armstrong number")
# else:
#     print("this is not an armstrong number")






# n=10
# x,y=0,1
# if n<0:
#     print("please enter positive number")
# else:
#     for i in range(11):
#         print(x,end='  ')
#         x,y=y,x+y





# x=10
# y=15
# x,y=y,x
# print(x,y)




# n=10
# sum=0
# for i in range(n+1):
#     sum=sum+(i**2)
# print(sum)





# 10
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)




# a=[10,20,30,40]
# sum=0
# for i in a:
#     sum+=i
# print(sum)




# a=[40,30,50,10,20,100]
# lar=a[0]
# for i in a:
#     if i> lar:
#         lar=i
# print(lar)




# a = [40, 30, 50, 10, 20, 100]
# lar = a[0]
# for i in range(6):
#     if a[i] > lar:
#         lar = a[i]
# print(lar)




# x=[10,20,30]
# y=[40,50,60]
# z=x+y
# print(z)


# a=[10,40,20,60,30,15,99]
# x=[10,40,20,60,30]
# y=[15,99]
# print(y+x)



# a=[10,40,20,60,30,15,99]
# x=a[:(len(a)-2)]
# y=a[(len(a)-2):]
# z=y+x
# print(z)



# a=[10,40,20,30,15,99]
# r=2
# x=a[:r]
# y=a[r:]
# z=print(y+x)







































# import os
# import random
# import smtplib
# def automatic_email():
#     user = input("Enter Your Name >>: ")
#     email = input("Enter Your Email >>: ")
#     message = (f"Dear {user}, Welcome to Thecleverprogrammer")
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login("Your Gmail Account", "Your App Password")
#     s.sendmail('&&&&&&&&&&&', email, message)
#     print("Email Sent!")   
# automatic_email()












