from tabulate import tabulate
configuration = {"uno":"letras",
                 "dos":"ambas",
                 "tres":3}
tabla = tabulate(configuration.items(), headers=["configuracion"], tablefmt="grid")
print(tabla)