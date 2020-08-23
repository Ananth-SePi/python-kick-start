# if, this multiple elif statements substitutes the switch statement found in other languages.

input_variable = int(input("Please enter a number from 0 to 2"))

if input_variable < 0 or input_variable > 2:
    print('Invalid input')
elif input_variable == 1:
    print('Go left')
elif input_variable == 2:
    print('Go right')
else:
    print('Go straight')

# for

languages = ['Tamil', 'English', 'Telugu', 'French']

for language in languages:
    print(language, len(language))

# list of languages that I know
for index in range(len(languages)):
    print(index + 1, languages[index])

# else clauses on loops
# this clause executes only when the loop terminates running through all the elements or condition fails

# prime number
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
