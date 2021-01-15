def abbreviate(S):
    if S.strip() == "":
        return '\n'
    line = ""
    for word in S.strip().split(' '):
        word = word[0].upper() if len(word) == 1 else word[0].upper() + word[1:]
        for char in word:
            if not char.islower():
                line += char
    return line

for line in open("input.txt", "r"):
    print(abbreviate(line))
