numbers = [4,5,6,11,15,20]
target = 15

for i in range(len(numbers) - 1):
    el_1 = numbers[i]
    try:
        idx_2 = numbers[i+1:].index(target - el_1)
    except:
        continue
    print([i, idx_2 + 1 +i] )