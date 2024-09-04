eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

goal = input('Что вы хотите - шифровать или дешифровать текст? \n').lower()
step = int(input('Какой шаг хотите сделать? Укажите в числе \n'))
text = input('Введите текст? \n')

#шифровать, то есть шагать вперед
def cesar_encrypt(text, step):

    encrypt_text = ''

    for letter in range(len(text)):
        #65-90
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

        #97-122
        if text[letter] in eng_lower_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с шифрованием до 122
            if num_unicode + step <= 122:
                new_letter = chr(num_unicode+step)
                encrypt_text += new_letter
            
            #если не укладываемся с шифрованием до 122
            else:
                new_letter = chr((step -(122 - num_unicode + 1)) + 97)
                encrypt_text += new_letter

        #1040-1071
        if text[letter] in rus_upper_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с шифрованием до 1071
            if num_unicode + step <= 1071:
                new_letter = chr(num_unicode+step)
                encrypt_text += new_letter
            
            #если не укладываемся с шифрованием до 1071
            else:
                new_letter = chr((step -(1071 - num_unicode + 1)) + 1040)
                encrypt_text += new_letter

        #1072-1103
        if text[letter] in rus_lower_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с шифрованием до 1103
            if num_unicode + step <= 1103:
                new_letter = chr(num_unicode+step)
                encrypt_text += new_letter
            
            #если не укладываемся с шифрованием до 1103
            else:
                new_letter = chr((step -(1103 - num_unicode + 1)) + 1072)
                encrypt_text += new_letter

        #если у нас есть разные символы
        elif text[letter] not in eng_lower_alphabet and text[letter] not in eng_upper_alphabet and text[letter] not in rus_lower_alphabet and text[letter] not in rus_upper_alphabet:
                encrypt_text += text[letter]

    return encrypt_text

#дешифровать, то есть шагать назад
def cesar_decrypt(text, step):

    decrypt_text = ''

    for letter in range(len(text)):
        #65-90
        if text[letter] in eng_upper_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с дешифрованием до 65 при вычитании
            if num_unicode - step >= 65:
                new_letter = chr(num_unicode-step)
                decrypt_text += new_letter
            
            #если не укладываемся с дешифрованием до 65
            else:
                new_letter = chr(90-(step-(num_unicode-65))+1)
                decrypt_text += new_letter
        
       #97-122
        if text[letter] in eng_lower_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с дешифрованием до 97 при вычитании
            if num_unicode - step >= 97:
                new_letter = chr(num_unicode-step)
                decrypt_text += new_letter
            
            #если не укладываемся с дешифрованием до 97
            else:
                new_letter = chr(122-(step- (num_unicode-97))+1)
                decrypt_text += new_letter

       #1040-1071
        if text[letter] in rus_upper_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с дешифрованием до 1040 при вычитании
            if num_unicode - step >= 1040:
                new_letter = chr(num_unicode-step)
                decrypt_text += new_letter
            
            #если не укладываемся с дешифрованием до 1040
            else:
                new_letter = chr(1071-(step- (num_unicode-1040))+1)
                decrypt_text += new_letter
        
        #1072-1103
        if text[letter] in rus_lower_alphabet:
            #определить номер в таблице
            num_unicode = ord(text[letter])
            
            #если укладываемся с дешифрованием до 1072 при вычитании
            if num_unicode - step >= 1072:
                new_letter = chr(num_unicode-step)
                decrypt_text += new_letter
            
            #если не укладываемся с дешифрованием до 1072
            else:
                new_letter = chr(1103-(step- (num_unicode-1072))+1)
                decrypt_text += new_letter

        elif text[letter] not in eng_lower_alphabet and text[letter] not in eng_upper_alphabet and text[letter] not in rus_lower_alphabet and text[letter] not in rus_upper_alphabet:
                decrypt_text += text[letter]

    return decrypt_text

if goal == 'дешифровать':
    print(cesar_decrypt(text, step))

else:
    print(cesar_encrypt(text, step))

