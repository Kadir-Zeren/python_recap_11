sayi = 5
while sayi:
    print('I love Python1')
    sayi -= 1

flag = True
times = 0
while flag:
    print('I love Python' )
    times +=1
    if times == 10:
        flag = False

number = 0
while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6')

my_list=["a", "b", "c", "d", "e"]
a = 0
while a < len(my_list):
    print('square of {} is : {}' .format(a, a ** 2))
    a+=1

'123' . isdigit()

# yas = input('Yasinizi giriniz : ')
# while not yas.isdigit():
#     print('Girdigin ifade yas olamaz')
#     yas = input('Yasinizi giriniz : ')
# print('Evet girdigin deger yasin olabilir.')

# yas = input('Yasinizi giriniz : ')
# flag = True
# while flag:
#     if yas.isdigit():
#         print('Evet girdigin deger yasin olabilir.')
#         flag = False
# else:
#     print('Girdigin ifade yas olamaz')
#     yas = input('Yasinizi giriniz : ')

# age = input("Enter your age please : ")
# while not age. isdigit():
#     print ("You entered incorrectly!")
#     age = input("Enter your age please : ")
# print("Great! You enter valid input : ", age)

# sayi = 50
# print("Let's play a game")
# while True:
#     girdi = int(input('Tuttugum sayiyi tahmin et : '))
#     if girdi == sayi:
#         print('Tebrik ederim Bildin')
#         break
#     elif girdi<sayi:
#         print('Biraz arttir')
#     else:
#         print('biraz azalt')

# sayi = 50
# print("Let's play a game")
# tahmin_sayisi = 1
# while tahmin_sayisi < 6:
#     girdi = int(input('Tuttugum sayiyi tahmin et : '))
#     if girdi == sayi:
#         print('Tebrik ederim Bildin')
#         break
#     elif girdi<sayi:
#         print('Biraz arttir')
#     else:
#         print('biraz azalt') 
#     print(tahmin_sayisi , 'kez tahmin ettiniz')
#     if tahmin_sayisi == 5:
#         print('Butun haklarini kullandin')
#     tahmin_sayisi+=1


# answer = 28
# question = 'What a two-digit number am I thinking of?'
# print ("Let's play the guessing game!")

# while True:
#     guess = int(input(question))
#     if guess < answer:
#         print('Little higher')
#     elif guess > answer :
#         print('Little lower')
#     else: # guess == answer
#         print('Are you a MINDREADER !!! ')
#         break

# cumle = input('Bir cumle yaziniz : ')
# kelimeler = cumle.split()
# print(kelimeler)
# sayac = 0
# en_uzun = 0
# uzunluk = len(kelimeler)
# while sayac < uzunluk:
#     if len(kelimeler[sayac])>en_uzun:
#         en_uzun = len(kelimeler[sayac])
#     sayac+=1
# print('En uzun kelimenin harf sayisi', en_uzun)

import random
sayi = random.randint(1,100)
print(sayi)

random.randint(1,10)

for i in [1, 2, 3, 4, 5] :
    print(i)


seasons = ['spring' , 'summer' , 'autumn' , 'winter ' ]
for season in seasons :
    print(season)

seasons = ['spring', 'summer', 'autumn', 'winter']
for mevsim in seasons:
    print(mevsim)


names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]

names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
for name in names:
    print('Hello', name)

names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
for i in names:
    print("hello", i)

listem = []
for i in range(1,6):
    listem. append(i)
print(listem)

numbers = []
for i in range(1, 6):
    numbers. append(i)
print(numbers)

course = 'clarusway'
for i in course :
    print(i)

text = 'Clarusway'
for harf in text:
    print(harf)


# text = 'Clarusway'
# for harf in text:
#     print(harf, end=" ")

text = 'Clarusway'
uzunluk = len(text)
kelime = ''
for i in range(uzunluk):
    if i != uzunluk-1:
        kelime =kelime + text[i] + "-"
    else:
        kelime += text[i]
print(kelime)

# text = 'Clarusway'
# sayac = 0
# for i in text:
#     sayac+=1
#     if sayac < len(text) :
#         i = i + '-'
#     print(i, end= '')

print('-'. join(text))

text = 'abc' 
text += 'd'
text
text = text + 'e'
text

text = text + 'f' + '-'
text
text += ('g' + '-')
text

# word = input("Give me a word :")
# count = 0
# for i in word:
#     count += 1
#     if count < len(word) :
#         i = i + "-"
#     print(i, end="")

user = {
"name": "Daniel",
"surname": "Smith",
"age": 35
}

for attribute in user:
    print(attribute)

user = {
'name' : 'Daniel',
'surname' : 'Smith',
'age' :35
}

for i in user. values():
    print(i)

# user = {
# "name": "Daniel",
# "surname": "Smith",
# "age": 35
# }

# for i in user. values():
#     print(i, end=" ")

user = {
"name": "Daniel",
"surname": "Smith",
"age": 35
}
 
for key, value in user. items():
    print (key, ":", value)

listem = [(1,2),(3,4),(4,5)]
for i, j in listem:
    print(i,j)

listem = [(1,2,3),(3,4,44),(4,5,55)]
for i, j,k in listem:
    print(i,j,k)
    
user = {
"name": "Daniel",
"surname": "Smith",
"age": 35
}

for key, value in user. items():
    print (key,":", value)

for i, j in user.items():
    print(i,j)


for i, j in user.items():
    print(f'{i:<10} : {j:>10}')

# times = int(input("How many times should I say 'I love you'"))
# for i in range(times):
#     print('I love you')

# sayi = int(input('Bir sayi giriniz : '))
# for i in range(11):
#     print(f'{sayi}X{i} = {sayi*i}')

# nmbr = int(input('enter a number between 1-10'))
# for i in range(11):
#     print('{}x{} = '.format(nmbr, i), nmbr * i)

b = list(range(11))
print(b)

a = set(range(0,10))
print(a)

c = tuple(range(11))
print(c)

print(range(5)) # it will not print the numbers in sequence
print(*range(5)) # '*' separates its elements

print(range(5))
type(range(5))
print(*range(5))

print(*range(5,25,2))

list(range(1,20,3))

print(*('separate'))

print(*range(10,0,-2))

list(range(10,0,-1))

list(range(10,0,-2))

text = ['one' , 'two' , 'three' , 'four' , 'five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)

liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4]
list(zip(liste1,liste2))

liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4]
liste3 = [10,20,30,40]
list(zip(liste1,liste2,liste3))

liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4,5,6,7,8,9,10]
liste3 = [10,20,30,40,50,60]
list(zip(liste1,liste2, liste3))

liste1 = ['a', 'b', 'c', 'd']
liste2 = [1,2,3,4,5,6,7,8,9,10]
liste3 = [10,20,30,40,50,60]
set(zip(liste1,liste2,liste3))

text = ['one', 'two', 'three', 'four', 'five' ]
numbers = [1, 2, 3, 4, 5]
for yazi, sayi in zip(text, numbers):
    print(sayi , ':', yazi)

tekler = []
ciftler = []
for i in range(10):
    if i %2 == 0:
        ciftler.append(i)
else:
    tekler.append(i)
print('cift sayilar listesi', ciftler)
print('tek sayilar listesi', tekler)

evens = []
odds = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
else:
    odds.append(n)
print(evens)
print (odds)