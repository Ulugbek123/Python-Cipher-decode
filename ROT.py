#Designed and made by Ulugbek Iskandarov,
#To be used only for education purpose. 


def alpha(cipherText):
    #Calls the define as alpha
    alphabet='abcdefghijklmnopqrstuvwxyz'
    #This is the alphabet our cipher will use for ROT 13
    #Lowercases all the Higher case words into LowerCase
    cipherText = cipherText.lower()

    #Goes through 26 times
    for i in range (0,26):
        plainText=''
        position=0
        for letter in cipherText:
            if letter not in alphabet:
                shiftedLetter=letter
            else:
                position =alphabet.index(letter)

                shiftedIndex = (position + i)%26    #26 char
                shiftedLetter=alphabet[shiftedIndex]

                plainText=plainText+shiftedLetter


        print("ROT13  shift of",i,'the message is\n\n',plainText,'\n')




def all(cipherText):
    alphabet='''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''

    #cipherText='Uryyb Jbeyq'

    cipherText = cipherText.lower()
    print(cipherText)
    for i in range (0,94):
        plainText=''
        position=0
        for letter in cipherText:
            if letter not in alphabet:
                shiftedLetter=letter
            else:
                position =alphabet.index(letter)

                shiftedIndex = (position + i)%94
                shiftedLetter=alphabet[shiftedIndex]

                plainText=plainText+shiftedLetter


        print("ROT47 shift of",i,'the message is\n\n',plainText,'\n')


def dec(cipherText):
    alphabet='0123456789'

    #cipherText='Uryyb Jbeyq'

    cipherText = cipherText.lower()
    print(cipherText)
    for i in range (0,10):
        plainText=''
        position=0
        for letter in cipherText:
            if letter not in alphabet:
                shiftedLetter=letter
            else:
                position =alphabet.index(letter)

                shiftedIndex = (position + i)%10
                shiftedLetter=alphabet[shiftedIndex]

                plainText=plainText+shiftedLetter


        print("ROT 5 shift of",i,'the message is\n\n',plainText,'\n')






something=input('Choose 1-3: ')
if something=='1':
    string=(input('Input Cipher Text: '))
    alpha(string)
    #ROT13
if something=='2':
    string=(input('Input Cipher Text: '))
    all(string)
    #ROT47

if something=='3':
    string=(input('Input Cipher Text: '))
    dec(string)
    #ROT5



print(something)
