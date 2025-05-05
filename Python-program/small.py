print("🔍 WEBSITE URL CHECKER 🔍")
url = input("\nEnter a website URL: ")

if url.startswith("https://"):
    print("🔐 This website uses HTTPS (secure)")
elif url.startswith("http://"):
    print("👀 This website uses HTTP (not secure)")
else:
    print("❌ This doesn't look like a complete URL")



print("🏃 STEP COUNTER 🏃")
daily_goal = int(input("🤷‍♂️ What is your daily step goal? "))
current_steps = int(input("✨ How many steps have you taken today? "))

remaining = daily_goal - current_steps
if remaining > 0:
    print(f"💪 You need {remaining} more steps to reach your goal!")
else:
    print(
        f"🎉 Congratulations! You've exceeded your goal by {-remaining} steps!")



print("📢 TEXT CAPITALIZER 📢")
text = input("🤷‍♂️ Enter some text: ")
print("✨ 1. UPPERCASE")
print("👀 2. lowercase")
print("🎉 3. Title Case")
print("🚀 4. Sentence case")

choice = input("Choose a format (1-4): ")

if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())



print("📝 CHARACTER TYPE CHECKER 📝")
char = input("Enter a single character: ")

if char.isalpha():
    print("This is a letter.")
elif char.isdigit():
    print("This is a digit.")
else:
    print("This is a special char.")





print("📊 GRADE CALCULATOR 📊")
scores = []

while True:
    score = input("Enter a test score (or 'done'): ")
    if score.lower() == "done":
        print("👋 Goodbye")
        break

    scores.append(float(score))
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.1f}")
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    else:
        print("Grade: D or F")



import random

print("🔤 WORD SCRAMBLER 🔤")

while True:
    word = input("\nEnter a word to scramble (or 'quit'):")
    if word.lower() == "quit":
        print("👋 Goodbye!")
        break

    # "everyone" => ["e","v","e","r","y","o","n","e"]
    # shuffle => ["y","v","e","r","e","o","n","e"] => join => yvereone
    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")




import random

print("🎶 MUSIC RECOMMENDER 🎶")

genres = {
    "rock": ["AC/DC", "Queen", "Led Zeppelin"],
    "pop": ["Taylor Swift", "Ed Sheeran", "Ariana Grande"],
    "hip-hop": ["Kendrick Lamar", "Drake", "J. Cole"],
}

choice = input("What genre do you like? (rock/pop/hip-hop): ")

if choice not in genres:
    print("😭 Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")




import random

first_parts = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
last_parts = ["rider", "walker", "hunter",
              "seeker", "dancer", "keeper", "singer"]

print("✨ FANTASY NAME GENERATOR ✨")

count = int(input("How many names do you want? "))

for _ in range(count):
    first_name = random.choice(first_parts)
    last_name = random.choice(last_parts)
    print(f"{first_name}{last_name}")




print("🔄 REVERSE NAME GENERATOR 🔄")

while True:
    name = input("\nEnter a name: ")

    if not name:
        break

    reversed_name = name[::-1]
    print(f"Your reversed name is: {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name.title()}")

    answer = input("\nTry another name? (y/n): ")
    if answer != "y":
        break






print("🔤 VOWEL COUNTER 🔤")

# Simple syntax
while True:
    text = input("\nEnter some text (or 'quit'): ")

    if text.lower() == "quit":
        print("👋 Goodbye!")
        break

    vowel_count = 0

    for letter in text.lower():
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    print(f"That text has {vowel_count} vowels!")


# Advanced syntax

while True:
    text = input("\nEnter some text (or 'quit'): ")

    if text.lower() == "quit":
        print("👋 Goodbye!")
        break

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels!")





import random

print("🎮 COIN FLIP GAME 🎮")
print("Guess heads or tails ✨")


while True:
    guess = input("\nEnter your guess (heads/tails): ").lower()

    if guess != "heads" and guess != "tails":
        print("❌ Please enter 'heads' or 'tails' ❌")
        continue  # what continue does? it goes back to the start of the loop

    flip = random.choice(["heads", "tails"])

    print(f"\n🪙 Coin shows {flip}")

    if guess == flip:
        print("You won! You guessed correctly. 🎉")
    else:
        print("😢 Sorry, wrong guess. Try again! 🍀")

    again = input("\n🔄 Play again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
        break




import random

print("👩‍🍳 RANDOM RECIPE GENERATOR 👩‍🍳")

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]


while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another one? (y/n): ").lower().startswith("y"):
        print("👋 Goodbye!")
        break



print("vowels")



while True:
   text= input("Enter a word(or quit): ").lower()
   if text == "quit":
      print("👋 Goodbye!")
      break
   
   count = 0

   for i in text:
      if i in "aeiou":
         count += 1

   print(f"Number of vowels: {count}") 
   
    