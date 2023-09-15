import os
import string
import time
from datetime import date
import tkinter as tk

# Function definitions

# GUI
def initializeGUI():
    gui = tk.Tk()

    gui.geometry("500x250")

    frame = tk.Frame(gui)
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame2 = tk.Frame(canvas)

    nameLabel = tk.Label(frame2, text="Input project name")
    nameInput = tk.Text(frame2, height=1, width=50, bg="light cyan")

    dieLabel = tk.Label(frame2, text="Input default die")
    dieInput = tk.Text(frame2, height=1, width=50, bg="light cyan")

    matLabel = tk.Label(frame2, text="Input default material")
    matInput = tk.Text(frame2, height=1, width=50, bg="light cyan")

    amountLabel = tk.Label(frame2, text="Input amount of points")
    amountInput = tk.Text(frame2, height=1, width=50, bg="light cyan")

    amount = amountInput.get("1.0", "end-1c")

    inputs = []

    if amount != "":
        for a in range(int(amount)):
            pointLabel = tk.Label(frame2, text=("Input Point " + str(a + 1) + " in X,Y,Z format"))
            pointInput = tk.Text(frame2, height=1, width=50, bg="light cyan")

            pointLabel.pack()
            pointInput.pack()

            inputPoint = pointInput.get("1.0", "end-1c")

            inputs.append(inputPoint)

    nameLabel.pack()
    nameInput.pack()
    dieLabel.pack()
    dieInput.pack()
    matLabel.pack()
    matInput.pack()
    amountLabel.pack()
    amountInput.pack()

    canvas.create_window((0, 0), window=frame2, anchor="nw")

    tk.mainloop()

# Format inputs to the proper .btax format
def formatter(amount, point, mat, die, name) :
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
 ID: IDPLACEHOLDER
 Display: True
 Color: -16744448
 Point; 
  X: {}
  Y: {}
  Z: {}"""

    # Points string init
    points = ""

    # Template array init
    templates = []

    for t in range(amount):
        newTemplate = pointsTemplate.format(str(t) + "X", str(t) + "Y", str(t) + "Z")
        templates.append(newTemplate)

    for p in range(amount):
        locs = point[p].split(",")

        templates[p] = ((str(templates[p]).replace((str(p) + "X"), locs[0]))).replace((str(p) + "Y"), locs[1]).replace((str(p) + "Z"), locs[2])

        points += templates[p]

    # Write final file
    btax = open(name + ".btax", "a")
    btax.write(header + points)
    btax.close()

# Console script
if __name__ == "__main__":
    gui = input("Use GUI?: Y/n " )

    if(gui.lower() == "n"):
        print("Bend-Tech Automation Tool\nAuthor: Connor De Leo\nVersion 0.1\n")
        
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

        formatter(amount, points, mat, die, name)

        print("File creation successful. Please check root directory.")
    elif(gui.lower() == "y"):
        initializeGUI()
    else:
        exit("N/A")