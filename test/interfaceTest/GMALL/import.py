import re

# class super(object):
#     def build(self):
#         print(re.match('www', 'www.runoob.com'))
#
#
# super().build()

print(re.match('com', 'comwww.runcomoob').group())
print(re.match('com', 'Comwww.runcomoob', re.I).group())
