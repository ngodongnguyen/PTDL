#numpy
import numpy as np
# ========== cau 4 ==========
a=np.empty(10)
print(a)
# ========== cau 5 ==========
a=np.array([26,7,19,27,12,29])
print(a)
print(a.shape)
# ========== cau 6 ==========
a=np.random.randint(1,10,size=15)
print(a)
# ========== cau 7 ==========
a=np.random.randint(1,10,size=(3,4))
print(a.shape)
# ========== cau 8 ==========
a=np.array([[5,10,21],[11,23,18],[22,19,35],[96,22,26]])
print(a)
print(a.shape)
print(a[1:3])
#======- Tạo một vector với các giá trị được lấy từ cột thứ 3 =========
vector_a=a[:,2]
print("vector la: ",vector_a)
#Tạo ra một ma trận mới với các giá trị được lấy từ ma trận trên 

a_new=np.array(a[1:,1:])
a_new[2,0]=30
print(a_new)
# ========== cau 9 ==========
a=np.arange(10, 20, 1)
print(a.shape)
a_new=np.reshape(a,(-1,5))
print(a_new.shape)
# ========== cau 10 ==========
a=np.array([99,46,87,62,11,32])
print("Max: ",np.max(a))
print("Min: ",np.min(a))
a.sort()
print(a)
x=np.where(a%2==0)
print(a[x])
print(a[x].shape)
print("mean: ",a.mean())
print("median: ",np.median(a))
print("sum: ",np.sum(a))
a[2]=np.mean(a)
a=np.delete(a,3)
print(a)
# ========== cau 11 ==========
a=np.array([[[5,10,21],[11,23,18],[22,19,35]],[[50,10,41],[61,23,28],[42,11,25]],[[96,22,26],[87,56,23],[90,75,32]]])
print(a[0:1,1:3])
print(np.mean(a[0:1]))
a[1:2,:,0]=np.mean(a[0:1])
print(a[1:2,:,0])
print("tong",np.sum(a[2:3]))
a[2:3,2:3]=-1
b=np.array(a[1:2])
print(b.shape)
vector_b=b[0:1]
print(vector_b)

