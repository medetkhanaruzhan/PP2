import re

text = "im_trying_not_to_let_go"
pattern = r"_([a-z])"

def repl(match):
    return match.group(1).upper()

result = re.sub(pattern, repl, text)
print(result)