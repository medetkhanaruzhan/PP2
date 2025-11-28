import re

text_to_match = "Cause it's too cold for you here and now, so let me hold both your hands in the holes of my sweater."

pattern = r"[ ,.]"
result = re.sub(pattern, ":", text_to_match)
print(result)