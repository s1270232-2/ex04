import random
heads = 0
tails = 0

print("Who are you?")
name = input("> ")
print(f"Hello,{name}")

print("Tossing a coin...")

for i in range(3):
    num = random.randint(0,1)
    if (num % 2 == 0):
        print(f"Round {i + 1}: Head")
        heads += 1
    else:
        print(f"Round {i + 1}: Tail")
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")
