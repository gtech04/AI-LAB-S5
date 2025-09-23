from sympy import symbols, And, Or, Not, Implies, satisfiable

rain = symbols("rain")
hagrid = symbols("hagrid")
dumbledore = symbols("dumbledore")

knowledge_base = And(
    Implies(Not(rain), hagrid),
    Not(And(hagrid, dumbledore)),
    Or(hagrid, dumbledore),
    dumbledore
)

print("Knowledge Base:")
print(knowledge_base)

is_satisfiable = satisfiable(knowledge_base)
print("\nIs the knowledge base satisfiable?", is_satisfiable)

hagrid_check = satisfiable(knowledge_base.subs({hagrid: True}))
print("\nDid Harry visit Hagrid?", hagrid_check)

rain_check = satisfiable(knowledge_base.subs({rain: True}))
print("Did it rain today?", rain_check)
