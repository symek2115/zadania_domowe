# zadanie 1
a = "Python 2023"
b = "Python 2023"
c = "Python 2023"
# a
print(a == b)
print(b == c)
# b
print(type(a), hex(id(a)))
print(type(b), hex(id(b)))
print(type(c), hex(id(c)))

# zadanie 2
a = input("wprowadz liczbe 1: ")
b = input("wprowadz liczbe 2: ")

c = input("podaj co chcesz zrobic: ")

if c=="+":
    print(int(a)+int(b))
elif c=="-":
    print(int(a)-int(b))
elif c == "*":
    print (int(a)*int(b))
elif c == "/":
    print (int(a)/int(b))
# zadanie 3
for i in range(1,4):
    pytanie1 = ""
    odpowiedz1 = ""
    odpowiedz2 = ""
    odpowiedz3 = ""
    if i==1:
            pytanie1 = "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?: "
            odpowiedz1 = "1. oglądanie telewizji/filmow/seriali"
            odpowiedz2 = "2. czytanie ksiazek/czasopism"
            odpowiedz3 = "3. sluchanie muzyki"
    elif i == 2:
            pytanie1 = "W jakich okolicznościach czytasz książki najczęściej?: "
            odpowiedz1 = "1. podczas podróży"
            odpowiedz2 = "2. w czasie wolnym (po pracy, na urlopie)"
            odpowiedz3 = "3. podczas pracy/nauki (to ich element)"
    elif i == 3:
          pytanie1 = "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?: "
          odpowiedz1 = "1. chęć poszerzenia wiedzy"
          odpowiedz2 = "2. czytanie mnie relaksuje/odpręża"
          odpowiedz3 = "3. fakt, że czytanie jest modne"
    print(pytanie1)
    print(odpowiedz1)
    print(odpowiedz2)
    print(odpowiedz3)
    answer = input("wybierz odpowiedz (1,2,3): ")

