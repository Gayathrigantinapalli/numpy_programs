# a=["mango","banana","apple"]
# for i in a:
# print(i)

# b=iter(a)
# print(next(b))
# print(next(b))




# a=["mango","banana","apple"]
# class kdkr:
#     def __iter__(self):
#         self.fruits=["mango","banana"]
#         self.index=0
#         return self
#     def __next__(self):
#         x=self.fruits(self.index)
#         self.index=self.a
#         self.a+=1
#         return x
# ong = iter(kdkr())

# print(next(ong))
# print(next(ong))
# print(next(ong))





# class kdkr:
#     def __iter__(self):
#         self.fruits=["mango","banana","apple"]
#         self.index=0
#         return self
#     def __next__(self):
#         if self.index<len(self.fruits):
#             fruits=self.fruits[self.index]
#             self.index +1
#             return fruits
#         else:
#             print("try again")
# obj=kdkr()
# c=iter(obj)
# print(next(c))
# print(next(c))
# d=iter(obj)
# print(next(d))
# print(next(d))




# try:
#     a = int(input("Enter your number: "))
#     b=int(input("enter your temp :"))

#     c=a/b
#     print(c)
        
#     # else:
#     #     print("Odd")
# except NameError:
#     print("Please enter both are in same formates :")
# except ZeroDivisionError:
#     print("you entered denominator value is 0 :")
# finally:
#     print("my taks is completed")
# # c=a/b
# # print(c)




# try:
#     print(4/0)
# except ZeroDivisionError:
#     print("you got an error")
# except NameError:
#     print("please enter correct data type")
# else:
#     print("my divison task completed")
# finally:
#     print("program sucessfully completed")