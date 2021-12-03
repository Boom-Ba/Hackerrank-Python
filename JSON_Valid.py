import json
def validateJsonText(jsonText):
    try:
        s=json.loads(jsonText)
        print(s)

    except Exception as e:
        raise e
    return True
json_string = '{ "name":"John ", "age":30 ,"car":"None"}'
print(validateJsonText(json_string))

def validateJsonFile(jsonFile):
    try:
        s=json.load(jsonFile)

    except Exception as e:
        raise e
    return True

with open ("input.json") as f:
    print("Validate Json File result: ",validateJsonFile(f))