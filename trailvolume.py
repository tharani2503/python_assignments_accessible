####stlfile=open("C:/Users/vinothd/PYTHON/assignments/myTet.stl")
####
####for eachline in stlfile:
####    if 'normal' in eachline:
####        a=eachline.split()
####        b=a[2:]
####        normal=[float(components) for components in b]
####        n1,n2,n3=normal
####        N=((n1**2)+(n2**2)+(n3**2))**0.5
####        unitnormal=[nc/N for nc in normal]
####        print(unitnormal)

        
stlfile=open("C:/Users/vinothd/PYTHON/assignments/cyls.stl")
points=[]
areas=[]
##f=xi
volume=[]
for eachline in stlfile:
    if 'normal' in eachline:
        a=eachline.split()
        b=a[2:]
        normal=[float(components) for components in b]
        n1,n2,n3=normal
        N=((n1**2)+(n2**2)+(n3**2))**0.5
        un=[nc/N for nc in normal] ## unit normal
##        print(unitnormal)
    
    if 'vertex' in eachline:
      a=eachline.split()
      b=a[1:]               ## packing needed elements from a list
      c=[float(coordinates) for coordinates in b]
      points.append(c)
     
        
    
    if len(points)==3:
      p1,p2,p3=points       ##unpacking

      a=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5
      b=((p3[0]-p2[0])**2+(p3[1]-p2[1])**2+(p3[2]-p2[2])**2)**0.5
      c=((p1[0]-p3[0])**2+(p1[1]-p3[1])**2+(p1[2]-p3[2])**2)**0.5
      s=(a+b+c)/2
      area=(s*(s-a)*(s-b)*(s-c))**0.5 ##calculating area
      areas.append(area)
      x=(p1[0]+p2[0]+p3[0])/3
      y=(p1[1]+p2[1]+p3[1])/3
      z=(p1[2]+p2[2]+p3[2])/3
      F=[x/3,y/3,z/3]
      
####      F=[(x/3)+(y**2)*(z**5),(y/3)+(z**2)*(x**5),(z/3)+(x**2)*(y**5)]   ##defining the vector field
      v1=(F[0]*un[0]+F[1]*un[1]+F[2]*un[2])*area ## calculating volume
      volume.append(v1)
##      print(points)
      points.clear() ## clearing the list so that the len becomes 0
      un.clear()
##print(areas)
print(sum(areas))
##print(v1)
print(sum(volume))
