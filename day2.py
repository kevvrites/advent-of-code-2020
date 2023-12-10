f = open("day2input.txt")
lines = f.readlines()

def check_valid1(min, max, letter, password):
    count = 0
    for l in password:
        if l == letter:
            count += 1
    if count < min or count > max:
        return False
    return True

valid_passwords = 0
for line in lines:
    restriction = line.split(':')[0].split(' ')
    min = int(restriction[0].split('-')[0])
    max = int(restriction[0].split('-')[1])
    letter = restriction[1]
    password = line.split(':')[1].strip()
    if check_valid1(min, max, letter, password):
        valid_passwords += 1

print(valid_passwords)


