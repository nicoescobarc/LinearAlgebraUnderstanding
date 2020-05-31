import numpy as np

#A=np.array([[-1,-4,3],[-2,-5,-3],[2,2,3]])
A=np.array([[-1.5,10,-3],[-2,-5,3],[12,2,3]])
n=np.shape(A)[1]
H_tot=np.identity(n)
R=np.copy(A)

for i in range(0,n-1):
    u=np.array([np.copy(R[i:,i])]).T
    u[0]=u[0]-np.linalg.norm(u)
    u=u/np.linalg.norm(u)
    
    H=np.identity(n)
    H[i:,i:]=np.identity(n-i)-2*u@u.T
    R=H@R
    H_tot=H@H_tot

Q=H_tot.T
#Q2,R2=np.linalg.qr(A)
#HEY, THIS IS A CHANGE