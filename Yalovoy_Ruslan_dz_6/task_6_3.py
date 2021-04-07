import json

with open('users.txt', 'r', encoding='utf-8') as f_users:
    with open('hobby.txt', 'r', encoding='utf-8') as f_hobby:
        dict_users = {}
        for line in f_users:
            user = line.strip().replace(',', ' ')
            hobby = f_hobby.readline().strip().replace(',', ', ')
            if hobby == '':
                hobby = None
            dict_users[user] = hobby
print(dict_users)
with open("users_dictionary.json", "w", encoding="UTF-8") as f:
    json.dump(dict_users, f, ensure_ascii=False)