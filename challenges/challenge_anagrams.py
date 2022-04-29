# https://www.arquivodecodigos.com.br/dicas/
# 4157-python-exercicio-resolvido-de-python-strings-e-
# caracteres-verificar-se-duas-palavras-sao-anagramas-uma-
# da-outra-solucao-usando-dicionariohash-table.html


def is_anagram(first_string, second_string):
    # case sensitive
    first_string = first_string.lower()
    second_string = second_string.lower()
    # o primeiro passo é verificar se os comprimentos das duas
    # palavras são iguais
    if(len(first_string) != len(second_string)):
        return False

# agora criamos dois dictionaries para as frequencias de
# cada uma das palavras
    freq_p1 = {}
    freq_p2 = {}

# agora registramos as frequências de letras na primeira
# palavra
    for letra in first_string:
        # a letra já está no dicionário?
        if letra in freq_p1:
            freq_p1[letra] += 1  # aumenta a frequêcia desta letra
        else:
            freq_p1[letra] = 1  # ainda não estava no dicionário

# agora registramos as frequências de letras na segunda
# palavra
    for letra in second_string:
        # a letra já está no dicionário?
        if letra in freq_p2:
            freq_p2[letra] += 1  # aumenta a frequêcia desta letra
        else:
            freq_p2[letra] = 1  # ainda não estava no dicionário

# registradas as frequências de letras das duas palavras,
# chegou a hora de compararmos os dois dicionários
    for chave in freq_p1:
        # esta chave não está no segundo dicionário ou
        # possui valores diferentes?
        if chave not in freq_p2 or freq_p1[chave] != freq_p2[chave]:
            return False

    # se chegou até aqui então uma palavra é anagrama da outra
    return True
