
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary['asjn'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     # print("That is not a key")
#     print(error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height is not over 3 meters.")

bmi = weight / height ** 2
print(bmi)