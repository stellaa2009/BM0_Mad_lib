import random
story = random.randrange(1,2)

adj = input("Enter an adjective:")
noun = input("Enter a noun:")
emo = input("Enter an emotion:")
verb = input("Enter a verb (past tense):")
	if story == 1:
		print(f"Today when I got on the train I saw a {adj} {noun}. I was so {emo} that I {verb}.")
	else :
		print(f"I had a really {adj} day today. I got a 1 on the {noun} I made for art class. My teacher was so {emo} at me, that she {verb}")