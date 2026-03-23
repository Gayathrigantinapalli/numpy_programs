# import numpy as np
# x=np.array([12,13,14,15])
# print(x)
# y=x .copy()
# y=x
# print(y)
# y[0]=100
# print(y)



# import numpy as np
# x=np.array([12,13,14,15,16])
# print(x.shape)
# print(x.ndim)



# import numpy as np
# x=np.array([12,13,14,15,16,17])
# y=x.reshape(2,3)
# print(y)



# import numpy as np
# x=np.array([12,13,14,15,16,17])
# y=x.reshape(3,2)
# print(y)




# import numpy as np
# x=np.array([10,11,12,13,14,15,16,17])
#1-d to 3-d
# y=x.reshape(2,2,2)
# y=x.reshape(3,2,2)
# print(y)






# import numpy as np
# x=np.array([10,11,12,13,14,15,16,17])
# # import numpy as np
# x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# y=[]
# for i in range(len(x)):

#     y.append(x[i])
# print(x)




# import numpy as np
# x=np.array([10,11,12,13,14,15,16,17])
# for i in range (len(x)):
#     if (x[i]%3)==0:
#         x[i]=100
# print(x)





# import numpy as np
# x=np.array([[10,11,12,13,15],[16,17,18,19,20]])
# for i in x:
#     # print(x)
#     for j in i:
#         print(j)






# import numpy as np
# x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# for i in x:
#     # print(i)
#     for j in i:
#         print(j)
#         for k in j:
#             print(k)





import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
for i in range (len(x)):
    x[i]=np.where(x[i]%3==0,100,x[i])    
print(x)





# import numpy as np
# x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# y=[]
# for i in range(len(x)):

#     for j in range(len(x[i])):
#         for k in range(len(x[i][j])):
#             y.append(x[i][j][k])
#         #    y = x.flatten()
#         #    y = x.flatten().tolist()
# print(y)





# import numpy as np
# x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# for i in x:
#     # print(x)
#     for j in i:
#         print(j)


