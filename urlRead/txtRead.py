def readTxt(url):
    with open(url, 'r') as f:
        content = f.read()
    return content


txt = readTxt('G:\demo.txt')
print txt
