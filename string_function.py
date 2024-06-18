name = "maulik parikh"
print(name.capitalize())
print(name.center(20,'#'))

# chcracter occurence

print(name.count(' ',11,13))

print(name[7:11])  # get substring

print(name.title())
print(name.swapcase())
print(name.zfill(20))  # fill with zeros
print(name.ljust(20,'#'))  # left justify
print(name.rjust(20,'#'))  # right justify
print(name.find('l'))
print(name.index('l'))
print(name.rfind('l'))
print(name.rindex('l'))
print(name.startswith('m'))
print(name.endswith('h'))
print(name.split(' '))  # split string
print(name.isalnum())
print(name.replace('maulik', 'arpit'))

print(name.translate(str.maketrans('m', 'a')))
print(name.translate(str.maketrans('m', 'a', ' ')))

print(name.upper())
print(name.lower())

print(name.strip())

###############  fsring  ########################

a = 'hi'
b = 'student'
c = 45

print(a+' '+b)

# fstring

print(a+' '+b+' '+str(c))

print(f"{a} => {b} => {c}")

price = 4500

# print('price of my cloth is '+str(price))
print(f'price of my cloth is {price:.3f}')

m = 12
n = 13

print(f"Sum of m and n is {m+n}")

value = 3400

print('expensive') if value>3200 else print('cheep')  # if else in one line

print(f'price is very { 'expensive' if value>3200 else 'cheep' }')

salary = 1200000

print(f'my salary is {salary:,} rs')