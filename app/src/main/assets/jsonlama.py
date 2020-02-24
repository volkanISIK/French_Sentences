import json

f = open("sadece_cumleler.txt","r",encoding="utf8")
line = f.readline()
counter = 1 
data = []
while line:
    cumle = {}
    cumle['no'] = counter
    if ")" in line:
        counter = counter + 1 
        cumle['fr'] = line 
        line = f.readline()
        cumle['en'] = line 
        data.append(cumle)
        #print(data)
    line = f.readline()

with open('test.json', 'w') as outfile:
    json.dump(data, outfile)