sentence = input("Enter a sentence: ")
word_list = sentence.split()
word_tuple = tuple(word.upper() for word in word_list)

filename = "sentence_data.txt"
with open(filename, "w") as file:
    file.write("List: " + str(word_list) + "\n")
    file.write("Tuple: " + str(word_tuple) + "\n")

print(f"Data saved to {filename}")

print("\nReading back from file:")
with open(filename, "r") as file:
    content = file.read()
    print(content)