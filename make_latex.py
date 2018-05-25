#!/usr/bin/env python

"""USAGE: make_latex.py -ARGS"""
"""Description: -ADD DESCRIPTION HERE!-"""

__author__ = "Andrey Miroshnikov"
__copyright__ = "Copyright (C) 2018 Andrey Miroshnikov"
__license__ = "GPL"
__date__ = "Mon 30/04/2018 19:14:32 GMT-08"
__version__ = "1.0.0"
__maintainer__ = "Andrey Miroshnikov"
__email__ = "abc@def.lolz"
__status__ = "Development"
__credits__ = "ADD PEOPLE TO CREDIT"

#------------Imports------------
import sys
import os
#------------Defines------------

#------------Variables------------
numSections = 5
titleString = "EECS170C - Simulation Lab 2"
authorString = "Andrey Miroshnikov"
numID = "38672455"
progName = "sim2"
#------------Functions------------
def writeStr(file, printString):
    for i in range(0, len(printString)):
        file.write(printString[i]+"\n")
def printStr(printString):
    for i in range(0, len(printString)):
        print(printString[i])
        
def preparePre(titleString, authorString, stringID):
    STRING = ("\\usepackage{amsmath}", "\\usepackage[]{graphicx}", "\graphicspath{ {images/} }",
               "\DeclareGraphicsExtensions{.pdf, .png}", "\\usepackage{float}",
               "\\usepackage{titling}", "\setlength{\droptitle}{-15em}", "\\title{"+titleString+"}",
               "\date{}", "\\author{"+authorString+",  ID No "+stringID+"}")
    return STRING
        
def prepareMain(numSections):
    STRING = ["\documentclass[11pt]{article}", "\input{preamble}", "\\begin{document}",
               "\maketitle{}"]
    for i in range(1, numSections+1):
        STRING.append("    \include{section"+str(i)+"}")
    STRING.append("    \section{Conclusion}")
    STRING.append("\end{document}")
    return (STRING)

def prepareSect(sectionNum):
    STRING = ["\section{"+str(sectionNum)+"}", "\subsection{1}", "%--------------------------------------"]
    # temp = makeFigure(sectionNum)
    # for index in range(0, len(temp)):
        # STRING.append(temp[index])
    # STRING.append("This is some test text")
    # STRING.append("\subsection{2}")
    # STRING.append("%--------------------------------------")
    # temp = makeTable(sectionNum)
    # for index in range(0, len(temp)):
        # STRING.append(temp[index])
    # temp = makeEqAlign(sectionNum)
    # for index in range(0, len(temp)):
        # STRING.append(temp[index])
    # STRING.append("\subsection{3}")
    # STRING.append("%--------------------------------------")
    # temp = makeEqSplit(sectionNum)
    # for index in range(0, len(temp)):
        # STRING.append(temp[index])
    # STRING.append("This is some more test text")
    return (STRING)
    
def makeFigure(sectionNum):
    return ("\\begin{figure}[H]", "    \\begin{center}", "        \includegraphics[scale=0.5]{sec_"+str(sectionNum)+"_1}",
            "    \end{center}", "    \caption{sec_"+str(sectionNum)+"_1}", "    \label{sec_"+str(sectionNum)+"_1}", "\end{figure}")
def makeTable(sectionNum):
    return ("\\begin{table}[H]", "    \center", "    \caption{test1}",
            "    \\begin{tabular}{| c | c | c | c |}", "        \hline",
            "        Lo & la $V_{DS}$ & chu & ugweduyg\\\\", "        \hline",
            "        Lo & la $V_{DS}$ & chu & ugweduyg\\\\", "        \hline",
            "    \end{tabular}", "    \label{table:sec_"+str(sectionNum)+"_1}", "\end{table}")
def makeEqAlign(sectionNum):
    return ("\\begin{align}", "V_{DS}=V_{GS}-V_{t0}",
            "\label{sec_"+str(sectionNum)+"_1}", "\end{align}")
def makeEqSplit(sectionNum):
    return ("\\begin{align}", "\\begin{split}", "h[n] &= c_1\delta[n]+c_2\delta[n-1]+c_2\delta[n-3]+c_1\delta[n-4]\\\\",
            "&= [c_1\; c_2\; 0\; -c_2\; -c_1]", "\end{split}", "\label{sec_"+str(sectionNum)+"_1}", "\end{align}")
#------------MAIN------------
#Create preamble.tex
PRE_STRING = preparePre(titleString, authorString, numID)
#Main.tex
MAIN_STRING = prepareMain(numSections)

#Sections
SECT_STRING = []
for index in range(1, numSections+1):
    temp = prepareSect(index)
    SECT_STRING.append(temp)
#Conclusuions

#Print
# printStr(PRE_STRING)
# printStr(MAIN_STRING)
# for index in range(1, numSections+1):
    # printStr(SECT_STRING[index])
#Write to File
if not os.path.exists(progName):
    os.makedirs(progName)
    os.makedirs(progName+"/images")
    file = open(progName+"/preamble.tex", "w+")
    writeStr(file, PRE_STRING)
    file.close()
    file = open(progName+"/main.tex", "w+")
    writeStr(file, MAIN_STRING)
    file.close()
    for index in range (0, numSections):
        file = open(progName+"/section"+str(index+1)+".tex", "w+")
        writeStr(file, SECT_STRING[index])
        file.close()
else:
    print("Project folder already exists!")