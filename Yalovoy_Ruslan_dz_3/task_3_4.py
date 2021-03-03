def thesaurus_adv(*list_name):
    dictionary_name = {}
    for i in list_name:
        dictionary_name.setdefault(i[i.index(' ') + 1],
                                   {}).setdefault(i[0], []).append(i)

    return dictionary_name


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева"))
