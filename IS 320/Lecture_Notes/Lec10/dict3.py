scores = {}

# key = name of student, value = score

name = "Stewie G."
score = 99
# insert
scores[name] = score

name = "Peter G."
score = 21
# insert
scores[name] = score

name = "Lois G."
score = 82
# insert
scores[name] = score

name = "Chris G."
score = 19
# insert
scores[name] = score

name = "Hayley"
score = 0
# insert
scores[name] = score

line = '-' * 23
print(line)
print(f'|{"Name":10s}|{"Score":^10s}|') 
print(line)
for name in scores:
    score = scores[name]
    print(f'|{name:<10s}|{score:^10d}|')
print(line)

# left <    right >     ^ center    justified ^^^

