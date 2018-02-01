import urllib.request
import re
from collections import Counter
try:
    with urllib.request.urlopen("http://www.qq.com/") as doc:
        html = doc.read()
        html_gbk = html.decode('gbk')
        html_split = re.split(r"\W+",html_gbk)
        print(Counter(html_split).most_common(10))
        print(html_split)
except:
    print("error")