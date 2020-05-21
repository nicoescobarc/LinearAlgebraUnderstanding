import numpy as np


#Real Matrix (anything special)
#A=np.array([[-1,-4,3],[-2,-5,-3],[2,2,3]])

#Skew-symmetric matrix
A=np.array([[0,-4,-3,1],[4,0,-1,3],[3,1,0,-1],[-1,-3,1,0]])

Lambdas_python,evectors=np.linalg.eig(A)
A_orig=A
n=100
B=np.identity(A.shape[1])
for i in range(0,n):
    Q,R=np.linalg.qr(A)
    A=R@Q
    B=Q.T@B
    print(B)
    
    error=(np.array(sorted(np.diag(A),key=abs))-
           np.array(sorted(Lambdas_python,key=abs)))
B=B.T

Lambdas_numeric=np.array(sorted(np.diag(A), reverse=True))