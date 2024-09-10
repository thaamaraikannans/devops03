# a = "kannan"

# # if a:
# #     print(a)
# while a:
#     print(a)
#     a = 0


number = int(input('Enter a number: '))
total = 0
# iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))
print('The sum is', total)