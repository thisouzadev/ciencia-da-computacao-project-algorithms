#  daniel me deu uma ajuda e tornou meu codigo mais simples


def is_anagram(first_string, second_string):
    # case sensitive
    first_string = first_string.lower()
    second_string = second_string.lower()
    # o primeiro passo é verificar se os comprimentos das duas
    # palavras são iguais
    if(len(first_string) != len(second_string)):
        return False

    for letter in first_string:
        if letter not in second_string:
            return False

        second_string = second_string.replace(letter, "", 1)

        if second_string == "":
            return True
