import re

lis = ['[ACE:SRS:10] [ACE:SRS:100] [ACE:SRS:1000] [ACE:SRS:110]', '[ACE:SRS:2]', \
       '[ACE:SRS:5]', '[ACE:SRS:6] [AID:SRS:1] [AID:SRS:10]', '[AID:SRS:2]', \
       '[BOLUS:SRS:1] [BOLUS:SRS:12]', '[BOLUS:SRS:2] [BOLUS:SRS:5] [BOLUS:SRS:6]', \
       '[PUMP:HRD:100] [PUMP:HRD:1000] [PUMP:HRD:105]', '[PUMP:HRD:3330]', \
       '[PUMP:HRD:3350] [PUMP:HRS:100]', '[PUMP:HRS:1000] [PUMP:HRS:103]', \
       '[PUMP:HRS:105]', '[ACE:SRS:1]']

indexList = []
ind = 0

fList = ['ACE', 'ACE', 'AID', 'AID', 'BOLUS', 'BOLUS', 'PUMP', 'PUMP', 'PUMP', 'PUMP']
sList = ['SRS', 'SRS', 'SRS', 'SRS', 'SRS', 'SRS', 'HRD', 'HRD', 'HRS', 'HRS']
thList = ['10', '1', '1', '2', '12', '5', '100', '105', '100', '103']


for i in range(len(fList)):
    #indexList.clear()
    ind = 0
    for tTag in lis:  # Trailing Tags List may be a problem when many trailing tags found.
        #indexList.clear()
        #for l in tTag:
        tTag = tTag.split("] ")
        for item in tTag:
            if fList[i] in item and sList[i] in item and re.search(r'\b(' + thList[i] + r')\b', item):
                print("*" + item)
                indexList.append(ind)
        ind = ind + 1
    #print(indexList)
    ##print(fList[i] + ":" + sList[i] + ":" + thList[i] + "\t\t" + lis[i])
    print(fList[i] + ":" + sList[i] + ":" + thList[i])
print(indexList)

'''
for l in lis:
    l = l.split("] ")
    for item in l:
        print(item)
'''
