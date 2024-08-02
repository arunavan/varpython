

import re



text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern, text)
print(matches)

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern, text)
print(matches)



text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches)




text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''

pattern = '\$([0-9\.]+)'
matches = re.findall(pattern, text)
print(matches)



text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'

matches = re.findall(pattern, text)
print(matches)



text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 ljh lsj a 123 was $4.85 billion. Same number for FY2020 Q4 was $8 billion
'''
pattern = 'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'

matches = re.search(pattern, text)
print(matches)



