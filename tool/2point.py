import os
import string
import time
from datetime import date

# Function definitions
# Encrypt the normal position numbers into Bend-Tech's weird encryption
def encrypt(num) :
    numList = list(str(num))
    encryptedDigits = []
    numLen = len(numList)

    if numLen == 1 :
        digit = int(numList[0])

        if (digit >= 0) and (digit <= 6) :
            encryptedDigits.append(str(digit + 3))
        elif (digit == 7) :
            encryptedDigits.append(":")
        elif (digit == 8) :
            encryptedDigits.append(";")
        elif (digit == 9) :
            encryptedDigits.append("<")

    elif numLen == 2 :
        for i in numList :
            digit = int(numList[i])

            if (digit >= 0) and (digit <= 6) :
                encryptedDigits.append(str(digit + 3))
            elif (digit == 7) :
                encryptedDigits.append(":")
            elif (digit == 8) :
                encryptedDigits.append(";")
            elif (digit == 9) :
                encryptedDigits.append("<")
        
        encryptedDigits.sort(reverse=True)

    elif numLen == 3:
        for i in numList : 
            digit = int(numList[i])

            if i == 2 :
                if (digit >= 0) and (digit <= 7) :
                    encryptedDigits.append(str(digit + 2))
                elif (digit == 8) :
                    encryptedDigits.append(":")
                elif (digit == 9) :
                    encryptedDigits.append(";")
            elif i == 1 :
                if (digit >= 0) and (digit <= 6) :
                    encryptedDigits.append(str(digit + 3))
                elif (digit == 7) :
                    encryptedDigits.append(":")
                elif (digit == 8) :
                    encryptedDigits.append(";")
                elif (digit == 9) :
                    encryptedDigits.append("<")
            elif i == 0 :
                if (digit >= 0) and (digit <= 6) :
                    encryptedDigits.append(str(digit + 3))
                elif (digit == 7) :
                    encryptedDigits.append(":")
                elif (digit == 8) :
                    encryptedDigits.append(";")
                elif (digit == 9) :
                    encryptedDigits.append("<")
            
        encryptedDigits.sort(reverse=True)

    encryptedNum = "".join(encryptedDigits)

    return(encryptedNum)

# Format inputs to the proper .btax format
def formatter(p1Split, p2Split, mat, die, name) :
    # Header template
    headerTemplate = """Bend-Tech Assembly: DocType:BTF
Interface: Assembly
Version: 7.10.23.0
Comma Format: False
Assembly Settings; [35]
 Name: NAME
 DieName: DIE
 MaterialName: MAT
 BackImage: 
 Date: DATE
 LastModified: DATE
 AutoLineMode: True
 AutoZoom: True
 DisplayAsCut: True
 DisplayHelpText: True
 DisplayThickness: True
 OverwriteMaster: False
 PromptNames: False
 ShowHoleFlags: False
 DisplayStyle: 0
 TriStartType: 2
 Units: 0
 AutoSave: {7}
 DimArrowType: {4}
 DimToleranceDistance: {6}
 DisplayQuality: {5}
 PickPointSize: {6}
 BackColor: -1
 DimDimColor: -16777216
 DimExtColor: -16777216
 DimTextColor: -16777216
 HelpTextColor: -9868951
 NewPPColor: -16744448
 DimArrowLength: {4}
 DimArrowWidth: {712}
 DimExtOffset: {3}
 DimExtStandoff: {3}
 DimLineWidth: {4}
 DimTextSize: {5}
 TriStarScale: {4}"""

    # Header formatting
    mdy = date.today().strftime("%m/%d/%y")
    header = (((headerTemplate.replace("DATE", mdy)).replace("MAT", mat)).replace("DIE", die)).replace("NAME", name)

    # Points template
    pointsTemplate = """
PickPoint; [7]
 ID: {3}
 Display: True
 Color: -16744448
 Point; 
  X: {P1X}
  Y: {P1Y}
  Z: {P1Z}
PickPoint; [7]
 ID: {3}
 Display: True
 Color: -16744448
 Point; 
  X: {P2X}
  Y: {P2Y}
  Z: {P2Z}
"""

    # Point encryption (Rules: see README.md)

    # Points formatting
    points = (((((pointsTemplate.replace("P1X", encrypt(p1Split[0]))).replace("P1Y", encrypt(p1Split[1]))).replace("P1Z", encrypt(p1Split[2]))).replace("P2X", encrypt(p2Split[0]))).replace("P2Y", encrypt(p2Split[1]))).replace("P2Z", encrypt(p2Split[2]))

    # Write final file
    btax = open(name + ".btax", "a")
    btax.write(header + points)
    btax.close()

# Take point inputs from cmd
def addPoint(point) :
    # Split string
    pointSplit = point.split(",")

    # Print sections to console
    print("Point: X:" + pointSplit[0] + " Y:" + pointSplit[1] + " Z:" + pointSplit[2] + " added")
    
    return(pointSplit)

# Add a gui soon
def gui() :
    return

# Run
name = input("Enter project name:")

mat = input("Enter material: ")
die = input("Enter die: ")

time.sleep(0.5)

p1 = input("Enter point 1 location in \"X,Y,Z\" format: ")
p2 = input("Enter point 2 location in \"X,Y,Z\" format: ")

formatter(addPoint(p1), addPoint(p2), mat, die, name)