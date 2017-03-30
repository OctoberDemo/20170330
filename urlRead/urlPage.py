import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://tieba.baidu.com/p/4892010310")
print html
