from sympy import symbols, And, Or, Implies, satisfiable

john_likes = symbols("john_likes(peanuts)")
peanuts = symbols("peanuts")
alive = symbols("alive")
food = symbols("food")
eats = symbols("eats")
anil = symbols("anil")
harry = symbols("harry")

knowledge_base = And(
    Implies(food, john_likes),
    Or(peanuts, symbols("apple"), symbols("vegetable")),
    Implies(And(eats, alive), food),
    And(eats, alive),
    Implies(eats, eats)
)

print("Knowledge Base:")
print(knowledge_base)

john_likes_peanuts_check = satisfiable(knowledge_base.subs({peanuts: True}))
print("\nDoes John like peanuts?", john_likes_peanuts_check)
