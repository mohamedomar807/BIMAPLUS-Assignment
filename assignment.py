# import Libraries
from tabulate import tabulate

# Define the number of polygon points
n =int (input("Enter the number of polygon points:"))
while n < 3:
    print ("Error: impossible to create polygon with less than 3 points")
    n = int(input("Re-enter the number of polygon points:"))
    if n > 2:
        break
print ("n = ",n)

# Poylgon (x,y) Coordinates to be defined and entred by end-user
print ("Enter x and y coordinates for polygon points (The points must be ordered counter clockwise):")
x=[];
y=[];
for i in range(n):
    print("Point:")
    xvalue=float(input("x:"))
    x.append (xvalue)
    yvalue= float(input("y:"))
    y.append (yvalue)

# Poylgon (x,y) Coordinates Table
print ("_______________________________")
print (" ")
print ("Coordinates Table:")
table = [["points", "x", "y"]]
for i in range(n):
    table.append(["point " + str(i +1), round(x[i],2), round(y[i],2)])
print (tabulate(table, headers="firstrow", tablefmt="fancy_grid", floatfmt=".2f"))

# Calculating Cross-Sectional Area (Ax)
Ax_i_Total=[]
for i in range(0, n):
    Ax_i = (1/2) * (x[i]+x[i-1]) * (y[i]-y[i-1])
    Ax_i_Total.append (Ax_i) 
Ax = float(sum(Ax_i_Total))

# Calculating Static Moments of the Cross-section (Sx & Sy)
# Sx:
Sx_i_Total=[]
for i in range(0, n):
    Sx_i = -1 * (1/6) * (x[i]-x[i-1]) * (y[i]**2+y[i]*y[i-1]+y[i-1]**2)
    Sx_i_Total.append (Sx_i) 
Sx = sum(Sx_i_Total)
# Sy:
Sy_i_Total=[]
for i in range(0, n):
    Sy_i = (1/6) * (y[i]-y[i-1]) * (x[i]**2 + x[i]* x[i-1] + x[i-1]**2)
    Sy_i_Total.append (Sy_i)
Sy = sum(Sy_i_Total)

# Calculating Axial Moments of intertia of the transmission (Ix & Iy & Ixy)
# Ix:
Ix_i_Total=[]
for i in range(0, n):
    Ix_i = -1 * (1/12) * (x[i]-x[i-1]) * (y[i]**3+y[i]**2 * y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    Ix_i_Total.append (Ix_i) 
Ix = sum(Ix_i_Total)
# Iy:
Iy_i_Total=[]
for i in range(0, n):
    Iy_i = (1/12) * (y[i]-y[i-1]) * (x[i]**3+x[i]**2 * x[i-1]+x[i]*x[i-1]**2+x[i-1]**3)
    Iy_i_Total.append (Iy_i) 
Iy = sum(Iy_i_Total)
# Ixy:
Ixy_i_Total=[]
for i in range(0, n):
    Ixy_i = -1 * (1/24) * (y[i]-y[i-1]) *(y[i]*(3*x[i]**2+ 2*x[i]*x[i-1]+x[i-1]**2)+ y[i-1] *(3*x[i-1]**2+2*x[i] *x[i-1] + x[i]**2))
    Ixy_i_Total.append (Ixy_i) 
Ixy = sum(Ixy_i_Total)

#Calculating Coordinates of the Centroid of the Cross-section (xt & yt)
#xt
xt = Sy / Ax
#yt
yt = Sx / Ax

#Moments of inertia with respect to the axex moved in parallel through the points of gravity of the cross-section (Ixt & Iyt & Ixyt)
#Ixt
Ixt = Ix - ((yt**2) * Ax)
#Iyt
Iyt = Iy - ((xt**2) * Ax)
#Ixyt
Ixyt = Ixy + (xt*yt*Ax)

# Results Table
print ("_______________________________")
print (" ")
print ("Geometric Characteristics:")

table2 = [["Charac.","Result"],
["Ax",round(Ax,2)],
["Sx", round(Sx,2)],
["Sy", round(Sy,2)],
["Ix", round(Ix,2)],
["Iy", round(Iy,2)],
["Ixy",round(Ixy,2)],
["xt",round(xt,2)],
["yt",round(yt,2)],
["Ixt",round(Ixt,2)],
["Iyt",round(Iyt,2)],
["Ixyt",round(Ixyt,2)]]
print (tabulate(table2, tablefmt="fancy_grid",floatfmt=".2f",headers="firstrow", showindex= range(1,12)))