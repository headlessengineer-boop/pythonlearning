lister = ["Вітаю", "Привіт", "Добрий день", "Привіт", "Вітаю", "Хелоу"]

new_list = []

for index, word in enumerate(lister):
    if word not in new_list:
        new_list.append(word)
        print(index, word)