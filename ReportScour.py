from audioop import add
import os
import pathlib
import re 
megaList = []
path = "P:\Crystal Reports"
f = open(".\Results.txt", "w")

def exploreFolder(folderPath):
    internalFolders = os.listdir(folderPath)
    for item in internalFolders:
        itemPath = (folderPath + "\\" + item)
        if os.path.isdir(itemPath):
            exploreFolder(itemPath)
        elif pathlib.Path(itemPath).suffix == ".rpt":
            megaList.append(itemPath)
        elif pathlib.Path(itemPath).suffix == ".rrd":
            rrd(itemPath)

def rrd(itemPath):
    try:   
        o = open(itemPath, 'r')
        rrdLine = ((o.readline()))
        while rrdLine:
            rrdLine = ((o.readline()))
            if( rrdLine != ''):
                interpret(rrdLine,itemPath)
            o.close
    except Exception as e:
        print("ERROR" + itemPath + "\n" + e)
          
def interpret(rrdLine,itemPath):
    name = "name"
    type = "type"
    output = "outputPath"
    reportPath ="reportPath"
    
    if ("EmailReport" in rrdLine):
        type = "EmailReport"
        output = re.search('recip=(.+)subj=', (rrdLine)).group(1)
        output = output.replace("&", "")

    elif ("SaveReport" in rrdLine):
        type = "SaveReport"
        output = re.search('saveas=(.+)&export', (rrdLine)).group(1)
    
    name1 = (rrdLine.split("?"))[0] 
    name = re.search('ort(.+)=', (name1)).group(1)
    reportPath = (name1.split("]="))[1]
    
    addLine = (f"{itemPath}^{reportPath}^{type}^{name}^{output}")
    megaList.append(addLine)

exploreFolder(path)
for ele in megaList:
    f.write(ele + "\n")