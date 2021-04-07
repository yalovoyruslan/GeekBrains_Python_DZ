tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

# while len(tutors) > len(klasses):
#     klasses.append('None')
print(klasses)
# b = ((tutors[i], klasses[i]) if  for i in range(len(tutors)))

b = [(el, klasses[i]) if i < len(klasses)
     else (el, None) for i, el in enumerate(tutors)]

c = [(el, klasses[i]) for i, el in enumerate(tutors) if i < len(klasses)]

# a = [b[j] for j in range(len(b))]
print(b)
x = 1
while x == len(tutors)+1:
    print(next(b))
