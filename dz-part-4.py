user_enter = input("Enter some words with space: ").split()

for i, word in enumerate(user_enter, 1):
    if len(word) <= 10:
        print(i, word)
    else:
        print(i, word[:10])

# print(i, word) if len(word) <= 10 else print(i, word[:10]
