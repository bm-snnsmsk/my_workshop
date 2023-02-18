html_doc = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1 id="header">Pyhton kursu</h1>
<h2 id="altbaslik">BeautifulSoup Dersi</h2>
    <div class="alt">
        <ul>
            <li>menu1</li><li>menu2</li>
            <li>menu3</li>
        </ul></div>
        
<h2 id="altbaslik">Web Dersi</h2>
    <div class="alt">
        <ul>
<li><a href="google.com">php</a></li>
<li><a href="python.org">python</a></li>
<li><a href="https://youtube.com">java</a></li>
        </ul>
    </div>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify() ## içeriği düzenli olarak verir
result = soup.title ## <title>Document</title>
result = soup.head ## <head> <meta charset="utf-8"/> <meta content="IE=edge" http-equiv="X-UA-Compatible"/> <meta content="width=device-width, initial-scale=1.0" name="viewport"/> <title>Document</title> </head>
result = soup.body ## <body><div class="alt"><ul><li>menu1</li><li>menu2</li><li>menu3</li></ul></div><div class="alt"><ul><li><a href="#">php</a></li><li><a href="#">python</a></li><li><a href="#">java</a></li></ul></div></body>
result = soup.title.name
result = soup.title.string 

result = soup.h1 
result = soup.h1.name 
result = soup.h1.string 

result = soup.find_all("h2")
result = soup.find_all("div")[1]
result = soup.find_all("div")[1].ul.find_all("li")
result = soup.find_all("div")[1].ul.find_all("li")[1].string

result = soup.div.findChild()

result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all("a")

result = soup.find_all("a")
for i in result :
    print(i.get("href")) 







print(result)
