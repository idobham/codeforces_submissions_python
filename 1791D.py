def distinct_splits (num, str1):
    right = {}
    for char in str1:
        if char not in right:
            right[char] = 1
        else:
            right[char] += 1

    right_distinct = len(right)
    left = {}
    left_distinct = 0
    maximum = 0
    for i in range (len(str1) - 1):
        char = str1[i]
        if char not in left:
            left_distinct += 1
        left[char] = left.get(char, 0) + 1
        right[char] -= 1
        if right[char] == 0:
            right_distinct -= 1
        if right_distinct + left_distinct > maximum:
            maximum = right_distinct + left_distinct

    return maximum
    #TLE ON TEST 3
    #combined = []
    #for i in range (1, len(str1)):
    #    right_word = str1[i:]
    #    left_word = str1[:i]
    #    combined.append(len(set(left_word)) + len(set(right_word)))
    #return max(combined)

times = int(input())
for i in range(times):
    print(distinct_splits(input(), input()))