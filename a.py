user_input = input("enter a sentence or a word:")
search_character = input("enter  a search character:")

print(user_input)
count = 0
for i in user_input:
    if i == search_character:
        count = count + 1
print(count)