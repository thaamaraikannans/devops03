import json

myDict = {
    "user": [
        {
            "name": "Thaamarai Kannan",
            "age" : 18,
            "location": "CBE",
            "role": "Technical Trainer",
            "domain" : ["AWS", "DevOps"],
            
        },
        {
            "name" : "mukesh",
            "age": 15,
            "location": "CBE",
            "role": "student",
            "domain": ["DevOps"],
            
        }
            ]
}


data = json.dumps(myDict)

print(type(data))