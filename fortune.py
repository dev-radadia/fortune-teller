def main():
    print("Welcome to Dev Radadia's Fortune Teller (21JE0298)")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("Your fortune: Great things await you, Dev! Keep smiling.")
    elif mood == "sad":
        print("Your fortune: Tough times don't last, but tough people like you do.")
    elif mood == "neutral":
        print("Your fortune: Balance brings peace. Embrace the calm.")
    else:
        print("Sorry, I can't predict fortunes for that mood.")

if __name__ == "__main__":
    main()