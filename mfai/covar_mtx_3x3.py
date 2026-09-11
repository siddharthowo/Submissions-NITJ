# Covariance matrix calculation (3x3)
x,y,z=[],[],[]

n=int(input("Enter number of entries:"))

for i in range(n):
    xi, yi, zi = map(float, input(f"Enter x, y, z for entry {i+1}: ").split())
    x.append(xi)
    y.append(yi)
    z.append(zi)

x_sum=sum(x)
y_sum=sum(y)
z_sum=sum(z)

x_avg=x_sum/n
y_avg=y_sum/n
z_avg=z_sum/n

x2_sum=0
y2_sum=0
z2_sum=0
xy_sum=0
xz_sum=0
yz_sum=0

for i in range(n):
    dx=x[i]- x_avg
    dy=y[i]-y_avg
    dz=z[i]-z_avg
    
    x2_sum+=dx*dx
    y2_sum+=dy*dy
    z2_sum+=dz*dz
    
    xy_sum+=dx*dy
    xz_sum+=dx*dz
    yz_sum+=dy*dz

cov_xx=x2_sum/(n-1)
cov_yy=y2_sum/(n-1)
cov_zz=z2_sum/(n-1)
cov_xy=xy_sum/(n-1)
cov_xz=xz_sum/(n-1)
cov_yz=yz_sum/(n-1)

covar_matrix = [
    [cov_xx,cov_xy,cov_xz],
    [cov_xy,cov_yy,cov_yz],
    [cov_xz,cov_yz,cov_zz]
]

print("\nCovariance matrix for entered data is:")
for row in covar_matrix:
    print(row)