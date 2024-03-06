from Point import Point

P=Point(8045,6936,497,1768,9739)
Q=Point(1539, 4742,497,1768,9739)
R=Point(4403,5202,497,1768,9739)

X=Point(5323, 5438,497,1768,9739)

print(Point.add([P,P,Q,R]))
print(Point.negate(P))
print(Point.multiply(1337,X))