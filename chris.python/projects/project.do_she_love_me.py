import random

she_love_me = random.choice([True, False])
she_hate_me = random.choice([True, False])

if she_love_me and she_hate_me:
    print("She love you and she hate you bro. Sounds tricky.")
elif she_love_me and not(she_hate_me):
    print("She love you my dude, go get her!")
elif not(she_love_me) and she_hate_me:
    print("She hate you bro :( ... better luck next time.")
else:
    print("She don't love you or hate you my guy. Keep trying!")