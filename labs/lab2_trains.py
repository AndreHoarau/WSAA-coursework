# Writing code that prints all the data of trains to the console and then only extracts trains with code d
# Author : Andre Hoarau
import requests 
import csv
from xml.dom.minidom import parseString
url = 'https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'

page = requests.get(url)
doc= parseString(page.content)
'''print(doc.toprettyxml())'''

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    trainlatnode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlat = trainlatnode.firstChild.nodeValue.strip()
    print (trainlat)
