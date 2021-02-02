#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:

    # autre solution
    is_pair = len(string) % 2 == 0

    return is_pair


    # autre solution
    """ if len(string) % 2 == 0:
        return True

    return false 
    """ 


def remove_third_char(string: str) -> str:
    return string[0:2] + string[3:]

# Équivalent de ce qui est érit dans la définition de la fonction:
# replace_char("bonjour" , "o", "z") -> bznjzur

def replace_char(string: str, old_char: str, new_char: str) -> str: #sans utiliser la fonction replace
   # for char in string:
    for i in range(len(string)):
        if string[i] == old_char:
            string = string[:i] + new_char + string[i + 1:]

    return string



def get_number_of_char(string: str, char: str) -> int: # sans utiliser .count
    num_char = 0
    for i in string:
        if i == char:
            num_char += 1

    return num_char


def get_number_of_words(sentence: str, word: str) -> int: #vérifier les symboles de ponctuation (ou les enlever) pour le .split
                                                          #et si un mot est contenu dans un autre (ne fonctionne pas pour le dernier caractère)
    num_words = 0
    sentence_splited = sentence.split() #si on ne spécifie pas de caractère, ça utilise par défaut l'espace
                                        # -> retourne une liste
    for mot in sentence_splited:
        if mot == word
        num_words += 1

    return num_words

# autre solution

def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")

    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
