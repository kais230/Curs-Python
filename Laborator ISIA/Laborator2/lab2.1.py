import numpy as np


v1=np.array([1,1,5,8,9,3,2])
v2=np.array([8,7,6,5,1,9,4])


#ex 1

print(v1.max()*v2.min())


#ex 2

m1=np.array([[2,2,2],[3,3,3],[1,5,5]])
m2=np.array([[6,1,9],[1,1,1],[1,4,5]])
m3=np.array([[6,2,3],[1,1,1],[1,4,5]])

print(np.dot((m1+m2),m3))
#ex 3

print (m2.min()/m1.max())

#ex 4

print(m1[1][2]-m2[0][1])


#ex 5

print (m1[0]+m2[2])

#ex 6

print( (m1[1]*m2[1]))

print(np.dot(m1[1],m2[1]))

#ex 7
print(m1[:,:2]+m2[1:3,:].T)

#ex 8

m2[m2<m1[2].max()] = 0

print(m2)