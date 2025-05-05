# inspiration code for Python Unit Testing Project
import math

def surfaceArea():
    pass

def volume(radius):  # <-- Add 'radius' here!
    return (4/3) * math.pi * radius ** 3

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    vol = volume(radius)
    print("Volume:", vol)

if __name__ == '__main__':
    prompt()
