import re

my_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

value = "24611EAAAAD"

response = re.search(my_pattern, value)

print(re.split(r"[A]", value))
print(response)