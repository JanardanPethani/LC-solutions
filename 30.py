def substringWithConcatenationOfAllWords(s, words):
    word_len = len(words[0])
    permut_len = len(words) * word_len

    curr = 0
    res = []

    while curr < len(s):
        temp = words.copy()
        word = s[curr : curr + word_len]
        try:
            word_idx = temp.index(word)
        except:
            word_idx = -1
        if word_idx >= 0 and (curr + permut_len) <= len(s):
            print(curr, curr + permut_len, s[curr : curr + permut_len])

            for i in range(curr, curr + permut_len, word_len):
                if s[i : i + word_len] in temp:
                    temp.remove(s[i : i + word_len])
            if len(temp) == 0:
                res.append(curr)
        curr += 1

    return res


s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
print(substringWithConcatenationOfAllWords(s, words))
