#create class to pass variable x,y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# check point q lies on line segment pr  
def onLine(p, q, r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
           q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False
 
def dir(p, q, r):
     
    val = ((q.y - p.y) * (r.x - q.x)) - ((q.x - p.x) * (r.y - q.y))
   
    if (val > 0):       # Clockwise orientation
        return 1
    elif (val < 0):     # Counterclockwise orientation
        return 2
    else:               # Colinear orientation
        return 0
    
def doIntersect(p1,q1,p2,q2):
    
    d1 = dir(p1, q1, p2)
    d2 = dir(p1, q1, q2)
    d3 = dir(p2, q2, p1)
    d4 = dir(p2, q2, q1)
    
    
    #case1
    if ((d1 != d2) and (d3 != d4)):
        return True
 
    #case2
 
    # p1 , q1 and p2 are colinear
    # P2 lies on line p1,q1
    if ((d1 == 0) and onLine(p1, p2, q1)):
        return True
 
    # p1 , q1 and q2 are colinear
    # P2 lies on line p1,q1
    if ((d2 == 0) and onLine(p1, q2, q1)):
        return True
 
    # p2 , q2 and p1 are colinear
    # P2 lies on line p1,q1
    if ((d3 == 0) and onLine(p2, p1, q2)):
        return True
 
    # p2 , q2 and q1 are colinear
    # q1 lies on line p1,q1
    if ((d4 == 0) and onLine(p2, q1, q2)):
        return True
 
    # none of the cases
    return False

#it will check if points intersect , dir,then check point is online or not   
def IsInside(poly,n,p):
   
    if (n < 3):
        return False
   
    extreme=Point(10000,p.y)
   
    count=0
    i=0

    while i < n:
       
        next = (i+1)%n
        if(i == n - 1):
            next = 0
        if (doIntersect(poly[i],poly[next],p,extreme)):
            if (dir(poly[i], p, poly[next]) == 0):
                return onLine(poly[i], p, poly[next])
            count += 1    
        i= next
       
        if i == 0:
            break
   
    ischeckInside = False
   
    if count%2 != 0:
        ischeckInside = True
       
    return ischeckInside

# Driver program to test above functions:

#case1

poly=[]
poly.append(Point(1,0))
poly.append(Point(8,3))
poly.append(Point(8,8))
poly.append(Point(1,5))

#point which lies inside or outside
p = Point(3 , 5)

#Length of polygon
n=len(poly)

#case2

# poly = []
# poly.append(Point(-3,2))
# poly.append(Point(-2,-0.8))
# poly.append(Point(0,1.2))
# poly.append(Point(2.2,0))
# poly.append(Point(2,4.5))

# #point which lies inside or outside
# p = Point(0, 0)

# #Length of polygon
# n=len(poly)

print(IsInside(poly,n,p))