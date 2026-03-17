# import numpy as np
# x=np.array(100)



# import numpy as np
# print(x.ndim)
# y=np.array([20,30,10,40,5])
# print(y.ndim)
# print(y[1:3])
# print(y[0:5])
# print(y[4:5])
# print(y[3:6])
# print(y[2:4])
# print(y[-4:-2])




# import numpy as np
# z=np.array([[1,2,3,4,],[5,6,7,8],[9,10,11,12]])
# print(z)
# print(z.ndim)
# print(z[1,1])
# print(z[2,3])
# # print(z[1:3,0:2])
# print(z[0:2,2:4])
# print (z[:2,2:])
# print(z[0,:])
# print(z[1,:])
# print(z[:3])
# print(z[:,3])
# print(z[:,0])




# import numpy as np
# w=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(w[0,0,2])
# print(w[0,:,1])
# print(w[1,1,:])
# print(w[1,:,1:])




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
# y=[]
# for i in range(len(x)):
#     # print(i)
#     if i%3==0:
#         y.append(100)
#     else:
#         y.append(i)
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



import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
for i in x:
    # print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)

