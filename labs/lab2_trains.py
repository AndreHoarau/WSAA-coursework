# Writing code that prints all the data of trains to the console and then only extracts trains with code d
# Author : Andre Hoarau
import requests 
import csv
from xml.dom.minidom import parseString
url = 'https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'

page = requests.get(url)
doc= parseString(page.content)
'''print(doc.toprettyxml())'''

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')

    for objTrainPositionsNode in objTrainPositionsNodes:

        # Get TrainCode properly (NOT using retrieveTags)
        traincodenode = objTrainPositionsNode.getElementsByTagName('TrainCode').item(0)

        if traincodenode and traincodenode.firstChild:
            traincode = traincodenode.firstChild.nodeValue.strip()
        else:
            traincode = ""

        '''traincode = traincodenode.firstChild.nodeValue.strip()
        trainlatnode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        trainlat = trainlatnode.firstChild.nodeValue.strip()
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)'''

        datalist = []

        # Keep your filter, but make it safe
        if traincode.startswith('D'):  

            for retieveTag in retrieveTags:

                datanode = objTrainPositionsNode.getElementsByTagName(retieveTag).item(0)

                # Some XML fields are empty → avoid crashes
                if datanode and datanode.firstChild:
                    value = datanode.firstChild.nodeValue.strip()
                else:
                    value = ""

                datalist.append(value)

            train_writer.writerow(datalist)
