import re

result = dir(re)

str = "sinan sian ann sinnnnnan _ - ? * ? = + ^ '  sinnnan şimşek @ $xz 123456 - q"

result = re.findall("s", str)
result = re.split("s", str)
result = re.sub("s","SSS", str)

result = re.search("nan", str)
result = re.search("nan", str).span()
result = re.search("nan", str).start()
result = re.search("nan", str).end()
result = re.search("nan", str).group()
result = re.search("nan", str).string

result = re.findall("[abcsn]", str)
result = re.findall("[0-356]", str)
result = re.findall(".", str)
result = re.findall("...", str)
result = re.findall("^inan", str)
result = re.findall("^sinan", str)
result = re.findall("q$", str)
result = re.findall("sin*an", str)
result = re.findall("sin+an", str)
result = re.findall("sin?an", str)
result = re.findall("sin{2}", str)
result = re.findall("sin{2,3}", str)
result = re.findall("(a|b|c)n", str)
result = re.findall("\$xz", str)
result = re.findall("\Asin", str)
result = re.findall("q\Z", str)
result = re.findall("\bsin", str)
result = re.findall("sin\b", str)
result = re.findall("sin\B", str)
result = re.findall("\Bsin", str)
result = re.findall("\d", str)
result = re.findall("\D", str)
result = re.findall("\s", str)
result = re.findall("\S", str)
result = re.findall("\w", str)
result = re.findall("\W", str)



print(result)