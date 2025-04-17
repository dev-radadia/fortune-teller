# fortune.py (v1.1)

import random

def main():
    print("Welcome to Dev Radadia's Fortune Teller (21JE0298)")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "Your fortune: Great things await you, Dev! Keep smiling.",
            "Your fortune: Your happiness will light up someone's day."
        ],
        "sad": [
            "Your fortune: The rain will pass, and the sun will shine again.",
            "Your fortune: You're stronger than you think. Stay hopeful."
        ],
        "neutral": [
            "Your fortune: Steady minds make smart choices. Good things are on the way.",
            "Your fortune: Keep going. You're doing just fine."
        ],
        "stressed": [
            "Your fortune: Take a deep breath. Peace is within reach.",
            "Your fortune: Even storms run out of rain. You're getting there."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("Sorry, I can't predict fortunes for that mood.")

if __name__ == "__main__":
    main()
