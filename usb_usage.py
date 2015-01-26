#!/usr/bin/env python

import requests
import re
import time

url="http://www.vodafone.com.eg/data/usbEntry.do?lang=en"


r = requests.get(url)

m = re.compile("\>(\d.*)\ (MB|GB)\<")
used, remaining = m.findall(r.content)

if 'GB' in used[1]:
    print time.strftime('%X'), float(used[0]) * 1000
else:
    print time.strftime('%X'), float(used[0])
