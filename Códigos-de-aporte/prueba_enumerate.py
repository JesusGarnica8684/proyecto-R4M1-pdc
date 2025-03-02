org_chain = "abcde"
user_chain = "a11d1"

both = list(zip(org_chain, user_chain))
lista = []
for org, user in both:
    if org == user:
        print("iguales", org, user)
        lista.append(user)
    else:
        print("Diferentes", org, user)
print(lista)


    
