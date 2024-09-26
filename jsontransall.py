import json
import os
import tradutor
f = open("ptbr/all.json", encoding="utf-8")
todos = tradutor.getTodos(f)
for name in os.listdir("ingles"):
	f = open("ingles/"+name, encoding="utf-8")
	cenario = tradutor.montaJson(f, todos)
	if type(cenario) == type("String"):
		f = open("ptbr/"+name, "w", encoding="utf-8")
		f.write(cenario)
		f.close()
	else:
		print("O script " + name + " tem o defeito: " + str(cenario))