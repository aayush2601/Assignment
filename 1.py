text = list()
filename = 'text.txt'
with open (filename) as fin:
        for line in fin:
                text.append(line.strip())

print(text)
