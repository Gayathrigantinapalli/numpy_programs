# import numpy as np
# a=np.array([1,2,3]
# b=np.array([4,5,6])
# concat=np.concatenate((a,b))
# # vstack=np.vstack((a,b))
# # hstack=np.hstack((a,b))
# # print(hstack)
# # print(vstack)
# print(concat)


# import numpy as np
# x=[1,2,5,3,4,6]
# y=[4,2,1,6,7,8]
# z=np.concatenate((x,y),axis=0)
# print(z)



# import numpy as np

# x =np.array([1, 2, 5, 3, 4, 6])
# y = np.array([4, 2, 1, 6, 7, 8])

# z = np.concatenate((x, y), axis=0)
# print(z)





# import numpy as np
# a=np.array([10,11,12,14,16,18])
# x =np.array([[1, 2, 5, 3, 4, 6]])
# y = np.array([[4, 2, 1, 6, 7, 8]])
# print(x)





# z = np.concatenate((x, y), axis=0)
# print(z)
# w=np.dstack((x,y))
# print(w)




# import numpy as np
# a=np.array([10,11,12,14,16,18])
# x =np.array([1, 2, 5, 3, 4, 6])
# y = np.array([4, 2, 1, 6, 7, 8])
# k=np.array_split(a,2)
# k=np.array_split(a,3)
# k=np.array_split(a,4)
# print(k)




# import numpy as np
# a=np.array([10,11,12,14,16,18])
# x =np.array([1, 2, 5, 3, 4, 6])
# y = np.array([4, 2, 1, 6, 7, 8])
# k=np.array_split(x,2)
# k=np.array_split(x,3)
# k=np.array_split(x,4)
# print(k)


# this is a search function in numpy
# import numpy as np
# x=np.array([[10,11,2,-3,4,5,6]])
# y=np.where(x==6)
# y=np.where(x==10)
# y=np.where(x%2==0)
# print(y)


# sort in numpy function
# import numpy as np
# x=np.array([10,20,-3,4,6])
# y=np.array([[1,2,-1],
#             [10,-5,8,-7]])
# z=np.sort(x)
# print(z)



# import numpy as np
# x=np.array([[10,20,-3,4,6]])
# y=np.array([[[1,2,-1,5],
#             [10,-5,8,-7]]])
# z=np.sort(y)
# print(z)






# random function in numpy 

# from numpy import random
# x=random.rand(3,3,2)
# print(x)



# from numpy import random
# x=random.randint(5,size=(2,3))
# print(x)



# from numpy import random
# x=random.choice(20,size=(2,3))
# print(x)



# import numpy as np
# a=np.array([[10,20,3,9]])
# b=np.array([[1,2,3,4]])
# c=[]
# for i in a:
#     if i%2==0:
#         c.append(i)
#     else:
#         c.append(10)
# print(c)


# import numpy as np

# a = np.array([[10,20,3,9]])
# c = []

# for row in a:
#     for i in row:
#         if i % 2 == 0:
#             c.append(i)
#         else:
#             c.append(10)

# print(c)





# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# # concat=np.concatenate((a,b))
# # print(concat)
# vstack=np.vstack((a,b))
# print(vstack)





# import numpy as np

# a = np.array([[[10,20,3,9]]])
# b=np.array([[[20,3,8,9]]])
# c = []

# for i in a:
        
#         for j in i:
#              for k in j:
#                    if k%2==0:
#                        c.append(k)
#                    else:
#                          c.append(8)
            #  if j%2==0:
            #       c.append(j)
            #  else:
            #       c.append(3)
    
    
        # if i % 2 == 0:
        #     c.append(i)
        # else:
        #     c.append(10)

# print(c)


# import numpy as np
# from numpy import random
# x=np.random.randint(1000,10000,size=2)
# # x=np.random.randint(0,10,size=5)
# print(x)



import numpy as np
from numpy import random
y=np.array([1,2,3,4,5])
np.random.shuffle(y)
print(y)



 


