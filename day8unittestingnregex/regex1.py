#pip install regex
import regex as re
text = " in FY2021 Q1 was $4.85 billion. vehicles in FY2021 S1 was $8 billion"
pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches = re.findall(pattern, text)
print(matches)

