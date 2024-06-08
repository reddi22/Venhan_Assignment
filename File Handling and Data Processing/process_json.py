import json

def process_json():
    try:
        with open(r'C:\Users\redda\Downloads\sample1.json''r') as file:
            jsonData = file.read()
            obj = json.loads(jsonData)
            print(obj['firstName'])
            print(obj)
    except FileNotFoundError:
        print('File not found')

process_json()