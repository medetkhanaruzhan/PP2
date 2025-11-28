import re

text = "IamTheOne"
result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)