import json

file=open("example.json","r")

data=json.load(file)
print(data)

file.close()

