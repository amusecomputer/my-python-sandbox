mood = input("How are you feeling today? ")

with open("mood_log.txt", "a") as file:
    file.write(mood + "\n")

print("Mood saved!")
