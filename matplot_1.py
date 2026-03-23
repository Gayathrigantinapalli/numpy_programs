# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([9,12,13,0,4,6])
# y=np.array([1,2,3,4,5,6])

# plt.plot(x,y)
# plt.show()

# plt.plot(x, y, marker='o')
# plt.show()


# plt.plot(x, y, color='green', linestyle='--')
# plt.show()

# plt.plot(x, y, marker='o')
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("My First Graph")
# plt.show()




import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,20,9,6])
y=np.array([8,4,1,0])

# plt.plot(x, y)
# plt.show()

# plt.plot(x, y, marker='o')
# plt.show()

# plt.plot(x, y, color='black', linestyle='--')
# plt.show()


# plt.plot(x, y, marker='o')
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("My new Graph")
# plt.show()

# plt.scatter(x, y)
# plt.show()

plt.plot(x, y)
plt.savefig("graph.png")
plt.show()