###Author: Vinoth D

stlfile=open("C:/Users/vinothd/PYTHON/assignments/myTet.stl")
points=[]
areas=[]
for eachline in stlfile:
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
      area=(s*(s-a)*(s-b)*(s-c))**0.5
      areas.append(area)
      points.clear()         ## clearing the list so that the len becomes 0
print(areas)
print(sum(areas))
