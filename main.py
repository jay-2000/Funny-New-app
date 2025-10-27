import random

subjects = [
    "cat", 
    "dog", 
    "teacher", 
    "bird", 
    "fish",
    "shahrukh",
    "Prime Minister Modi",
    "Virat Kohli",
    "A group of Monkeys",
    "Auto driver from delhi"
]

actions = [
    "ate",
    "slept",
    "jumped",
    "ran",
    "sang",
    "danced",
    "flew",
    "swam",
    "climbed",
    "hiked"
]

places_or_things = [
    "on the moon",
    "in the ocean",
    "under the bridge",
    "at the zoo",
    "in the park",
    "on the roof",
    "in the forest",
    "on the stage",
    "in the classroom",
    "at the beach"
]

#start the headline genrating

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" Aaj ki Breaking New: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\n Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

#print good bye message
print("\n Thanks for using the Breaking News Headline Generator. Goodbye!")
