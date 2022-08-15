files = ['1.txt', '2.txt', '3.txt']

data = {}
for file in files:
    with open(file, encoding='utf-8') as f:
        line = f.read().split('\n')
        data[len(line)] = file, '\n'.join(line)

with open('sort_files.txt', 'w', encoding='utf-8') as f:
    for line, content in sorted(data.items()):
        f.write(str(line) + '\n' + content[0] + '\n' + content[1])