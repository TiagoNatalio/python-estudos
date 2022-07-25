import myjson

json =  '{ "name":"John", "age":30, "city":"New York"}'

jsonToDict = myjson.tranformDict(json)
print(jsonToDict)