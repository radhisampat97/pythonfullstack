# Example for Assignment operator
##x=20
##y=10
##z=5

#Different assignment methods
##x,y,z = 20,10,5

##Addition assignment operator

x, y, z = 20, 10, 5
print("x: ", x)
print("x identity: ", id(x))
print("y: ", y)
print("y identity: ", id(y))
print("z: ", z)
print("z identity: ", id(z))
print()
z += x
print("z identity: ", id(z))
print("Will add x and z and will store its result in z: ", z)

# Subtraction assignment operator
x, y, z= 20, 10, 5
z -= x
print("will subtract z from x and will store its result in z: ", z)
##

#Multiplication Assignment operator
x, y, z = 20, 10, 5
z *= x
print("Will multiply x with z and will store its result in z: ", z)

#Division Assignment operator
x, y, z = 20, 10, 5
z /= x
print("Will divide z by x and will store its result in z: ", z)

#Modulus Assignment operator
x, y, z = 20, 10, 5
z %= x
print("Will divides z by x and will store its result inz: ", z)

#Exponential assignment operator
x, y, z = 20,10, 5
print("Will perform power value of y for z and will store its result in z: ", z)

#Floor Division assignment operator
x, y, z = 20, 10, 5
z//=y
print("Will perform floor division and will store its result in z: ", z)
