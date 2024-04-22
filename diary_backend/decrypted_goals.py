data = []

with open("data.txt", "r") as f:
    Lines = f.readlines()
    for line in Lines:
        data += [line.strip()]
