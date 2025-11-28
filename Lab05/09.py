import re

text = "LetMeLoveYouLikeIUsedTo"
pattern = r"([A-Z])"
result = re.sub(pattern, r" \1", text).strip()
print(result)