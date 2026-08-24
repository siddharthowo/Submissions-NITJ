#LDA Assignment
w_l=[]
h_l=[]
n=int(input("Enter number of entries:"))
for i in range(n):
    w=float(input("Enter weight:"))
    w_l.append(w)
    h=float(input("Enter height:"))
    h_l.append(h)

X=[]
Y=[]
w_sum=0
h_sum=0
for i in range(n):
    w_sum+=w_l[i]
    h_sum+=h_l[i]
w_avg=w_sum/n
h_avg=h_sum/n

X_2sum=0
Y_2sum=0
XYsum=0

for i in range(n):
    x_val=h_l[i]-h_avg
    y_val=w_l[i]-w_avg    
    X_2sum+=x_val**2
    Y_2sum+=y_val**2
    XYsum+=x_val*y_val

covar_matrix=[[X_2sum/(n-1), XYsum/(n-1)], [XYsum/(n-1), Y_2sum/(n-1)]]
print("\nCovariance matrix for entered data is:", covar_matrix)