import os

# data = "demo_folder1"

# if os.path.exists(data):
#     # os.remove
#     os.remove("F:/IMS/devops03/python/os/demo_folder1/appp.txt")
#     os.rmdir(data)
#     os.mkdir(data)
# else:
#     os.mkdir(data)

response = os.environ["database_endpoint"]

response = response.split(";")
print(response[-2])

# print(os.environ["PATH"][0])
