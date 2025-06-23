def main():
    from utils.time_greeting import get_greeting

    greeting = get_greeting()
    print(greeting)

    while True:
        user_input = input("Entrez quelque chose (ou 'exit' pour quitter) : ")
        if user_input.lower() == 'exit':
            print("Au revoir")
            break
        # palindrome check
        if user_input.lower() == user_input.lower()[::-1]:
            print("Bien dit !")
        print(f"Vous avez dit : {user_input}")

if __name__ == "__main__":
    main()