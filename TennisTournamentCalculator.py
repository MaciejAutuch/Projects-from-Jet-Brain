n = int(input())
g = 0
names_list = []

while g < n:
    person = input()
    names_list.append(person)
    g += 1

winners = [name.split()[0] for name in names_list if name.split()[1] == "win"]

print(winners)
print(len(winners))