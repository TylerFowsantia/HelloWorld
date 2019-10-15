tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<':
        count += 1
    else:
        count += 0

print("There are {} tags".format(count))