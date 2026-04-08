try:
    with open("Sample.txt", "rt") as f1:
        print(f1.read())

except FileNotFoundError as e:
    print("File Sample.txt was not found.")

