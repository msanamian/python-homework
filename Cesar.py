eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

goal = input('Что вы хотите - шифровать или дешифровать текст? \n').lower()
step = int(input('Какой шаг хотите сделать? Укажите в числе \n'))
text = input('Введите текст? \n')


def cesar_encrypt(text , step):

    encrypt_text = ''
    for letter in range(len(text)):
        if text[letter] in eng_upper_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с шифрованием до 90
            if num_unicode + step <= 90:
                new_letter = chr(num_unicode+step)
                encrypt_text += new_letter
            
            #если не укладываемся с шифрованием до 90
            else:
                new_letter = chr((step -(90 - num_unicode + 1)) + 65)
                encrypt_text += new_letter

        #если у нас есть разные символы
        elif text[letter] not in eng_lower_alphabet or text[letter] not in eng_upper_alphabet or text[letter] not in rus_lower_alphabet or rus_upper_alphabet:
                encrypt_text += text[letter]

    return encrypt_text

def cesar_decrypt(text, lng, step):
    pass

print(cesar_encrypt(text, step))