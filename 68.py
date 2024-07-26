"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20

op = []
line = []

for i in range(len(words)):
    if len(" ".join(line)) + len(" " + words[i]) > maxWidth:
        # print(line)
        op.append(" ".join(line))
        line = []
    line.append(words[i])
op.append(" ".join(line))
print(op)

for idx, string_line in enumerate(op):
    remaining_ch = maxWidth - len(string_line)
    temp_lst = string_line.split(" ")
    space_available = len(temp_lst) - 1
    # print("remaining_ch", remaining_ch, "chr_count", chr_count, "temp_lst", temp_lst)
    if remaining_ch > 0:
        if idx == len(op) - 1 and space_available:
            op[idx] = op[idx] + " " * (remaining_ch - space_available)
            continue
        if space_available == 0:
            op[idx] = op[idx] + " " * remaining_ch
            continue
        if space_available > 0:
            assidned_space = remaining_ch % space_available
            if assidned_space == 0:
                op[idx] = (" " * (remaining_ch // space_available)).join(temp_lst)
            else:
                op[idx] = (" " * (remaining_ch // space_available)).join(temp_lst)
                first_space_idx = op[idx].find(" ")
                op[idx] = (
                    op[idx][:first_space_idx]
                    + " " * (assidned_space)
                    + op[idx][first_space_idx:]
                )

print(op)
