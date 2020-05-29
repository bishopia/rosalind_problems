### --- Install python ---

# import this
from collections import Counter

### --- Variables and some arithmetic ---

a = 839
b = 822

c = a**2 + b**2

print(c)


### --- Strings and Lists ---

str = "EkcfdoK2ymrdY5vJcYHtPxa6z2fFalcipennismfdC5J6K6P3wJ4VR1JsaQ4RNZNhv8TrZsmJADGjYAbNs7EsyaKCKM82SYWrTMh9ycianeusz2F8glXgLAEpIeRbkvTsCLIpEVsHcJn3tMPZxMBPHkPjM4ltHUIujleNQcPMr9tBS3krBGZ3fdMW3."

start1 = 27
stop1 = 37
start2 = 102
stop2 = 108

#print sliced strings using above
print(
    f'{str[start1:stop1 + 1]} {str[start2:stop2 + 1]}')


### --- Conditions and Loops ---

startPos = 4719
endPos = 9208
# result = 0

# for x in range(startPos, endPos + 1):
#     if x % 2 != 0: #check if x is odd
#         result += x

result = sum(
    [x for x in range(startPos, endPos + 1) if x % 2 != 0]
    )

print(result)


### --- Working with Files ---

output = []

with open('input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 !=0]

with open('out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))


### --- Dictionaries ---

txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

#Generic approach
# wordCountDict = {}

# for word in txtStr.split(' '):
#     if word in wordCountDict:
#         wordCountDict[word] += 1
#     else:
#         wordCountDict[word] = 1

# print(wordCountDict)

#Optimized, pythonic approach using Counter from collections
wordCountDict = Counter(txtStr.split(' '))

for key, value in wordCountDict.items():
    print(key, value)
