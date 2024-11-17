import random
import string

from kelime import kelime
from hangman_visual import lives_visual_dict

def get_valid_word(kelime):
    word=random.choice(kelime)
    while '-' in word or ' ' in word:
        word=random.choice(kelime)

    return word.upper()

def hangman():
    word=get_valid_word(kelime)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives=9


    while len(word_letters)>0 and lives>0:

        print("Kalan caniniz:",lives,"Kullandiginiz harfler:"," ".join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Şuanki Kelime'," ".join(word_list))

        user_letter = input("Harf tahmin edin:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print("Bu harf kelimede yok")
        elif user_letter in used_letters:
            print("Bu harfi söylediniz.Tekrar deneyin.")
        else:
            print("Geçerli karakter girmediniz")
    if lives==0:
        print("Kaybettin... kelime: ",word)
        print(lives_visual_dict[lives])
    else:
        print("Tebrikler",word," kelimesini tahmin ettin!!")

if __name__ == '__main__':
    hangman()



