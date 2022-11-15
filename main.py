#from __future__ import annotations   # For version 3.8
import docx
from docx import Document
from docx.shared import RGBColor
import re
import xlwings

#dictionary that holds the tags as keys and the file where they are found as a valueError
docFile = {"HRD":"HDS_new_pump.docx", "HRS":"HRS_new_pump.docx", "HTP":"HTP_new_pump.docx", "HTR":"HTR_new_pump.docx", \
           "PRS":"PRS_new_pump.docx", "RISK":"RiskAnalysis_Pump.docx", "SDS":"SDS_New_pump_x04.docx", \
           "ACE":"SRS_ACE_Pump_X01.docx", "BOLUS":"SRS_BolusCalc_Pump_X04.docx", "SRS":"SRS_DosingAlgorithm_X03.docx", \
           "SVAL":"SVaP_new_pump.docx", "SVATR":"SVaTR_new_pump.docx", "UT":"SVeTR_new_pump.docx", "URS":"URS_new_pump.docx"}

#location of file path directory
filePath = "C:/Users/steph/OneDrive/Desktop/Docs_Project/"
docFileList = list(docFile.keys())                  # This is a list of all main tags found in each document
leadingTags = []                                            #list of leading tags
trailingTags = []                                          #list of trailing tags
relationalLeadingTags = []
tagDescriptions = []
uniqueParentTags = []


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def GetText(filename):                      # Opens the document and places each paragraph into a list and grabs data paragraph from file
    doc = docx.Document(filename)
    fullText = [] #creates blank list
    for para in doc.paragraphs:
        fullText.append(para.text)
    fullText = [ele for ele in fullText if ele.strip()]   # Eliminates empty paragraphs
    return fullText                                        #a list of all document content


def GetLeadingTags():                    # Returns list of getting tags
    for tag in docFileList:             # Tags are used to open the corresponding file
        textList = GetText(filePath + docFile[tag])
        index = 0
        ind = []
        for t in textList:
            if tag == "BOLUS" or tag == "ACE":      #SRS has 3 additional tags which are BOLUS, AID, ACE
                if re.search('.*[:\s]' + "SRS" + '[:\s]', t): #This block the same as the else block
                    ind.append(index)
                    #tt = t
                    tagDescriptions.append(t)
                    y = re.findall('\S*[:\s]' + "SRS" + '[:\s]\S*', t)
                    leadingTags.append(y[0])
                    index = index + 1
            # print(ind)
            else:
                if re.search('.*[:\s]' + re.escape(tag) + '[:\s]', t):
                    ind.append(index)
                    #tt = t
                    tagDescriptions.append(t)
                    y = re.findall('\S*[:\s]' + re.escape(tag) + '[:\s]\S*', t)
                    #print(y[0])
                    leadingTags.append(y[0])
                    index = index + 1
            #print(ind)
        leadTagsAndDescriptions = [leadingTags,tagDescriptions]

    return leadTagsAndDescriptions

def GetTrailingTags():                     # Returns only valid child tags
    for tag in docFileList:             # Tags are used to open the corresponding file
        textList = GetText(filePath + docFile[tag])
        unique_tags = []
        index = 0
        ind = []
        for t in textList:
            if tag == "BOLUS" or tag == "ACE":
                if re.search('.*[:\s]' + "SRS" + '[:\s]', t):
                    ind.append(index)
                    tt = t
                    y = re.findall('[\[{].+[\]}]', t)
                    if len(y) != 0:
                        unique_tags.append(y[0])
                        trailingTags.append(y[0])
                index = index + 1
                # print(ind)
            else:
                if re.search('.*[:\s]' + re.escape(tag) + '[:\s]', t):
                    ind.append(index)
                    tt = t
                    y = re.findall('[\[{].+[\]}]', t)
                    if len(y) != 0:
                        unique_tags.append(y[0])
                        trailingTags.append(y[0])
                index = index + 1
            #print(ind)
    return trailingTags


def GetRelLeadTags():                          #call function and stitch them together
    leadTagsList = GetLeadingTags()
    for tag in leadTagsList[0]:
        if re.search('[:\s]'+ "RISK" + '[:\s]',tag) or re.search('[:\s]'+ "URS" + '[:\s]',tag):
            pass
        else:
            relationalLeadingTags.append(tag)
    return relationalLeadingTags

def GetUniqueParentTags():
    trailingTagsList = GetTrailingTags()
    for tags in trailingTagsList:
        tags = tags.replace('[',"").replace(']',"")
        tags = tags.split()
        for item in tags:
            uniqueParentTags.append(item)
    uniqueTags = list(set(uniqueParentTags))
    uniqueParentTags.remove('{NA}')
    uniqueParentTags.remove('{PASS}')
    uniqueParentTags.remove('{FAIL}')
    return uniqueTags

leadTags = GetLeadingTags()[0]
print(leadTags)
DescriptionTagsList = GetLeadingTags()[1]
print(DescriptionTagsList)
trailingTagsList = GetTrailingTags()
print(trailingTagsList)
parentTagsList = GetUniqueParentTags()
print(parentTagsList)