def match_words(words):
    ca = 0
    ba = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ca += 1
            ba.append(word)
    print ("list of words with first and last character same\n",ba)
    return ca

count = match_words(['applllea','bahaf','pop','sgdg','47284','9261'])
print("number of words first and last character same:",count)

num = [23,43623,645,6,56,75,5]
print("the first value is num ",num[0],num[-1])