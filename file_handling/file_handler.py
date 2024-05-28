from io import TextIOWrapper


fin: TextIOWrapper = open("input.txt")
fout: TextIOWrapper = open("output.txt", mode="w")

data: str = fin.read(4)
data2: list[str] = fin.readlines()
# or: data2: list[str] = list(fin)

number_of_char = fout.write(data)
fout.writelines(data2)

print(data)
print(data2)
print(number_of_char)

fin.close()
fout.close()
