def accepted(*list_name):
    dictionary_name = {}
    for i in list_name:
        dictionary_name.setdefault(i[0], []).append(i)
    return dictionary_name


print(accepted("Иван", "Мария", "Петр", "Илья"))
