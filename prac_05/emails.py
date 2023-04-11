name_to_email = {}
email = input("Email: ")
while email != "":
    temp = email.split("@")
    tup = temp[0].split(".")
    name = ""
    for item in tup:
        name = name + " " + item
    name = name.title()

    choice = input(f"Is your name {name} ? (Y/N)").upper()
    if choice == "N" or choice == "NO":
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")
print("\n")
for keys, value in name_to_email.items():
    print(f"{keys} ({value})")
