#!/usr/bin/python3 

hydras = {4 : 1}

step = 1
while len(hydras) > 0:
    min_hydra = min(hydras)

    if min_hydra == 1:
        step += hydras[min_hydra]
        hydras.pop(min_hydra)
        continue

    hydras[min_hydra] -= 1
    if hydras[min_hydra] == 0:
        hydras.pop(min_hydra)
    if min_hydra != 1:
        hydras[min_hydra - 1] = step + 1

    step += 1

print(step - 1)
