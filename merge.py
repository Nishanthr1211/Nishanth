'''
import dictionary as m
print(m.a.values())

import platform
a=platform.system()
print(a)

x=dir(platform)
print(x)

from module1 import add
add(8,5,6)



from dictionary import a
print(a["name"])
'''
import datetime
x=datetime.datetime.now()
print(x)

print(x.year)
print(x.time())
print(x.date())
print(x.strftime("%A"))
