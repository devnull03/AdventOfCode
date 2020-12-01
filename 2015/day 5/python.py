try:
    with open('input.txt') as file:
        l = list(map(lambda x:x.rstrip('\n'), file.readlines()))
except:
    with open('day 5\\input.txt') as file:
        l = list(map(lambda x:x.rstrip('\n'), file.readlines()))

# It contains at least three vowels (aeiou only)

# It contains at least one letter that appears twice in a row, 
# like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

# It does not contain the strings ab, cd, pq, or xy, 
# even if they are part of one of the other requirements.

print(l)
