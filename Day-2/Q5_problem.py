numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
maximum = max(numbers)
minimum = min(numbers)
with open("minmax_data.txt", "w", encoding="utf-8") as f:
    f.write(str(numbers) + "\n")
    f.write("Max: " + str(maximum) + "\n")
    f.write("Min: " + str(minimum) + "\n")
with open("minmax_data.txt", "r", encoding="utf-8") as f:
    print(f.read())
