# class non_veg:
#     def lunch(self):
#         print("i am eating chicken biriyani")
# class veg:
#     def lunch(self):
#         print("i am eating sambar rice")
# nv=non_veg()
# # nv.lunch()
# v=veg()
# # v.lunch()
# for i in (non_veg(),veg()):
#             i.lunch()




# class non_veg:
#     def lunch(self):
#         print("i am eating chicken biriyani")
# class veg:
#     def lunch(self):
#         print("i am eating sambar rice")
# nv=non_veg()
# v=veg()
# for i in (non_veg(),veg()):
#             i.lunch()







# class non_veg:
#     def __init__(self, food, curry):
#         self.food = food
#         self.curry = curry

#     def lunch(self):
#         print(f"i am eating {self.food}, {self.curry}")

# class veg:
#     def __init__(self, food, curry):
#         self.food = food
#         self.curry = curry

#     def lunch(self):
#         print(f"i am eating {self.food}, {self.curry}")

# nv=non_veg("chapathi", "mutton curry")
# v=veg("white rice", "pachadi")
# for i in (nv, v):
#             i.lunch()








# class qis:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def s_details(self):
#         print("student details is belongs to qis")
# class prakasam(qis):
#     pass
# class pace(qis):
#     def s_details(self):
#         print("student details is belongs to pace")
# class rice(qis):
#     def s_details(self):
#         print("students belongs to rice")
# ong1=qis("gayee",234)
# ong2=prakasam("chitti",9876)
# ong3=pace("sai",90087)
# ong4=rice("latha",8765)
# for i in (ong1,ong2,ong3,ong4):
#     print(i.name)
#     print(i.rollno)
#     print(i.s_details())





# class food:
#     def __init__(self,items,curry,amount):
#         self.items=items
#         self.__curry=curry
#         self._amount=amount
#     def get_curry(self):
#         print("my curry is :",self.__curry)
#     def price(self):
#         print("my amount is :",self._amount)
# obj=food("biriyani","chicken",100)
# print(obj.items)
# obj.get_curry()
# obj.price()







# decorators
# def my_decorators(func):
#     def wrapper(a,b,c):
#         if a>1000:
#            print("simple interest process shortlist")
#            return func(a, b, c)
#         else:
#             print("enter valid amount")
#     return wrapper
# @my_decorators 
# def my_si(p,t,r):
#     si=(p*t*r)/100
#     print("simple interest is :",si)
# my_si(2000,86,9)
  





# def my_decorators(func):
#     def my_list(a):
#         if a>40:
#             print("qualified ")
#             # return func(a,b,c)
#         else:
#             print("not qualified  ")
#             return func(a)
#     return my_list
# @my_decorators
# def eamcet_marks(a):
#     print()
# eamcet_marks(35,78,40)





# def log_in(func):
#     def inner(password):
#         if password==1234:
#            return func(password)
#         else:
#             print("Invalid Password")
#     return inner
# @log_in
# def academy(password):
#     print("Welcome to Kotesh Academy")
# academy(1234)    





# def my_decarator1(func):
#     def wrapper1():
#         print("before")
#         func()
#         print("after")
#     return wrapper1
# def my_decarator2(func):
#     def wrapper2():
#         print("hii")
#         func()
#         print("bye")
#     return wrapper2
# @my_decarator1
# @my_decarator2
# def greet():
#     print("welcome to kdkr")
# greet()
   
























# def my_decarator1(func):
#     def wrapper1():
#         print("before")
#         func()
#         print("after")
#     return wrapper1


# def my_decarator2(func):
#     def wrapper2():
#         print("hii")
#         func()
#         print("bye")
#     return wrapper2


# @my_decarator1
# @my_decarator2
# def greet():
#     print("welcome to kdkr")


# greet()




# map(function,input)
# def my_add(n):
#     print(n*2)
# n=[1,2,3,4]
# res=map(my_add,n)
# print(list(res))



# a=["1","2","3"]
# for i in a:
#     print(int(i))
# b=list(map(int,a))
# print(b)
       


# manual
# a=[1,2,3,4]
# print(list(map(str,a)))




# logic
# a=[1,2,3,4]
# b=lambda x:x**2
# # print(list(map(b,a)))
# c=map(lambda x:x**2,a)
# print(list(c))




# function 
# a=[1,2,3,4,5,6,7]
# def my_squr(x):
#     if x%2==0:
#          return x*2
#     else:
#          return "sorry"
# res=map(my_squr,a)
# print(list(res))




# a=[13,9,9]
# b=[2,5]
# c=map(lambda x,y:x+y,a,b)
# print(list(c))




# a=[1,2,3,3]
# def my_filter(x):
#     if x%2==0:
#         return 'even'     
# c=filter(my_filter,a)
# print(list(c))





