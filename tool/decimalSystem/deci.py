from datetime import date
import csv
import decimal

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Global Vars
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

pointsTemplate = """
PickPoint; [7]
 ID: IDPLACEHOLDER
 Display: True
 Color: -16744448
 Point; 
  X: {}
  Y: {}
  Z: {}"""

# Function definitions

# GUI
def fileOutGui(mat, die, name, points, filename):
    # Header formatting
    mdy = date.today().strftime("%m/%d/%y")
    header = (((headerTemplate.replace("DATE", mdy)).replace("MAT", mat)).replace("DIE", die)).replace("NAME", name)

    # Template array init
    templates = []
    pointOut = ""

    for t in range(len(points)):
        newTemplate = pointsTemplate.format(str(t) + "X", str(t) + "Y", str(t) + "Z")
        templates.append(newTemplate)

    for p in range(len(points)):
        templates[p] = ((str(templates[p]).replace((str(p) + "X"), (points[p])[0]))).replace((str(p) + "Y"), (points[p])[1]).replace((str(p) + "Z"), (points[p])[2])
        pointOut += templates[p]

    # Write final file
    btax = open(name + ".btax", "a")
    btax.write(header + pointOut)
    btax.close()

    showinfo(title="Complete", message=("A new Bend-Tech Project File has been created from the supplied " + str(filename) + "\nPlease check the root directory."))

def fileReader(filename):
    lines = []

    with open(filename, "r") as handler:
        reader = csv.reader(handler, delimiter=',')
        for row in reader:
            lines.append(row)
    
    mat = (lines[0])[0]
    die = (lines[0])[1]
    name = (lines[0])[2]

    lines.remove(lines[0])

    points = lines

    fileOutGui(mat, die, name, points, filename)

def selectFile():
    filetypes = (('Comma Separated Value', '*.csv'), ('All file types', '*.*'))

    filename = fd.askopenfilename(title="Open file", initialdir="/", filetypes=filetypes)
    
    fileReader(filename)

def initializeGUI():
    root = tk.Tk()
    root.title("Bend-Tech Automation")
    root.resizable(False, False)
    root.geometry('500x250')

    openBtn = ttk.Button(root, text="Open Point File", command=selectFile)
    openBtn.pack(expand=True)

    root.mainloop()

# Encrypt decimal inputs
def encryptDeci(deci):
    positive = True

    if (deci < 0):
        positive = False
        deci = abs(deci)
    else:
        positive = True
    
    deciString = (str(deci)).split(".")
    deciDigits = len(deciString[1])

    if (int(deciString[0]) == 0):
        if deciDigits == 1:
            deciPoints = int(deciString[1])

            match deciPoints:
                case 1:
                    deci = "312"
                case 2:
                    deci = "412"
                case 3:
                    deci = "512"
                case 4:
                    deci = "612"
                case 5:
                    deci = "712"
                case 6:
                    deci = "812"
                case 7:
                    deci = "912"
                case 8:
                    deci = ":12"
                case 9:
                    deci = ";12"
                case _:
                    exit("Bad digit, exiting. [L161]")
        elif deciDigits == 2:
            deciPoints = list(deciString[1])

            match int(deciPoints[1]):
                case 1:
                    deci = "3202"
                case 2:
                    deci = "4202"
                case 3:
                    deci = "5202"
                case 4:
                    deci = "6202"
                case 5:
                    deci = "7202"
                case 6:
                    deci = "8202"
                case 7:
                    deci = "9202"
                case 8:
                    deci = ":202"
                case 9:
                    deci = ";202"
                case _:
                    exit("Bad digit, exiting. [L185]")
        elif deciDigits == 3:
            deciPoints = list(deciString[1])
            
            match int(deciPoints[2]):
                case 1:
                    deci = "32102"
                case 2:
                    deci = "42102"
                case 3:
                    deci = "52102"
                case 4:
                    deci = "62102"
                case 5:
                    deci = "72102"
                case 6:
                    deci = "82102"
                case 7:
                    deci = "92102"
                case 8:
                    deci = ":2102"
                case 9:
                    deci = ";2102"
                case _:
                    exit("Bad digit, exiting. [L207]")
        else:
            exit("Decimal has too many places! Keep points under three.")
    else:
        exit("Decimal not <1, exiting.")

    return deci

# Format inputs to the proper .btax format
def formatter(amount, point, mat, die, name):
    # Header formatting
    mdy = date.today().strftime("%m/%d/%y")
    header = (((headerTemplate.replace("DATE", mdy)).replace("MAT", mat)).replace("DIE", die)).replace("NAME", name)

    # Template array init
    templates = []

    # Point out string init
    pointsOut = ""

    for t in range(amount):
        newTemplate = pointsTemplate.format(str(t) + "X", str(t) + "Y", str(t) + "Z")
        templates.append(newTemplate)

    for p in range(amount):
        deci1 = (decimal.Decimal(point[p].split(",")[0])).as_tuple().exponent
        deci2 = (decimal.Decimal(point[p].split(",")[1])).as_tuple().exponent
        deci3 = (decimal.Decimal(point[p].split(",")[2])).as_tuple().exponent
        decis = [deci1, deci2, deci3]

        if (decis[0] < 0) or (decis[1] < 0) or (decis[2] < 0):
            encrypted = ["","",""]
            locs = point[p].split(",")

            if (decis[0] < 0):
                encrypted[0] = encryptDeci(float(locs[0]))
            else:
                encrypted[0] = locs[0]
            
            if (decis[1] < 0):
                encrypted[1] = encryptDeci(float(locs[1]))
            else:
                encrypted[1] = locs[1]
            
            if (decis[2] < 0):
                encrypted[2] = encryptDeci(float(locs[2]))
            else:
                encrypted[2] = locs[2]
            
            templates[p] = ((str(templates[p]).replace((str(p) + "X"), encrypted[0]))).replace((str(p) + "Y"), encrypted[1]).replace((str(p) + "Z"), encrypted[2])

            pointsOut += templates[p]
        else:
            locs = point[p].split(",")

            templates[p] = ((str(templates[p]).replace((str(p) + "X"), locs[0]))).replace((str(p) + "Y"), locs[1]).replace((str(p) + "Z"), locs[2])

            pointsOut += templates[p]

    # Write final file
    btax = open(name + ".btax", "a")
    btax.write(header + pointsOut)
    btax.close()

# Console script
if __name__ == "__main__":
    gui = input("Use GUI?: Y/n " )

    if(gui.lower() == "n"):
        print("Bend-Tech Automation Tool\nAuthor: Connor De Leo\nVersion 1.1\n")
        
        name = input("Please input the project name: ")

        die = input("Please input the default die: ")
        mat = input("Please input the default material: ")

        print("\nGeneral selections completed...\n")
        
        amount = int(input("Please enter the amount of points to be added: "))

        points = []
        for i in range(amount):
            current = input("Please input point number " + str(i + 1) + "'s X,Y,Z values: ")
            points.append(current)
        
        print("\nPoint selection completed...\n")

        print("MAT:" + mat + " DIE:" + die + " NAME:" + name + "\n")
        formatter(amount, points, mat, die, name)

        print("File creation successful. Please check root directory.")

    elif(gui.lower() == "y"):
        initializeGUI()
    else:
        exit("N/A")