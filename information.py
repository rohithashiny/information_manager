#Personal Information Manager (Basic Version)


name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")


hobbies_input = input("Enter your hobbies: ")
hobbies = [hobby.strip() for hobby in hobbies_input.split(",")]

print("Personal Information")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print("Hobbies:")
for i, hobby in enumerate(hobbies, start=1):
    print(f"  {i}. {hobby}")
print("==========================================")