def main():
    first_string = input("Informe a primeira palavra: ")
    second_string = input("Informe a segunda palavra: ")

    if(is_anagram(first_string, second_string)):
        print("As duas palavras são anagramas")
    else:
        print("As duas palavras não são anagramas")

    if __name__ == "__main__":
        main()