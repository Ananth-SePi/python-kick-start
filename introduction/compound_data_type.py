# list

languages = ['Tamil', 'English', 'Telugu', 'French', 'Russian', 'Hebrew', 'Spanish']
# indexes       0          1         2         3          4         5          6
#              -7         -6        -5        -4         -3        -2         -1

# print list
print(languages)
print(languages[0])
print(languages[3])

# negative index
print(languages[-2])

# sub list
print(languages[3:6])
print(languages[:-4])

# adding elements to existing list
languages = languages + ['Malayalam', 'Thai', 'Japanese']
print(languages)

# length of the list
print(len(languages))

# group update or delete
languages[2:5] = ['French', 'Russian']
print(languages)
languages[6:8] = []
print(languages)
