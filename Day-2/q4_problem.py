names = input("Enter names separated by spaces: ").split()
names.sort()
names_tuple = tuple(names)
with open("names_data.txt", "w") as f:
    f.write(str(names) + "\n")
    f.write(str(names_tuple) + "\n")
with open("names_data.txt", "r") as f:
    print(f.read())
