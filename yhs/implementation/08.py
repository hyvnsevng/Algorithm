def ascii_to_char(asc_list):
    string = str()
    for asc in asc_list:
        string += chr(asc)
    return string


S = input()

alphabet = []
number = []

for letter in S:
    if letter.isalpha():
        alphabet.append(ord(letter))
    else:
        number.append(int(letter))

alphabet.sort()
sorted_alphabet = ascii_to_char(alphabet)

print(sorted_alphabet+str(sum(number)))
