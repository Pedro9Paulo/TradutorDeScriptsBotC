import json
import os
for name in os.listdir("oldingles"):
	f = open("oldingles/"+name)
	try:
		script = json.load(f)
		f.close()
		cenario = "["
		for p in script:
			if p["id"] == "_meta":
				cenario += "{"
				for item in p:
					if type(p[item]) == type(True):
						cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
					else:
						cenario += '"' + item + '": "' + p[item] + '", ' 
				cenario = cenario[:-2] + "},"
			else:
				cenario += '"'+ p["id"] +'",'
	except Exception as erro:
		print("O script " + name + " tem o defeito: " + str(erro))

	f = open("ingles/"+name, "w", encoding="utf-8")
	f.write(cenario[:-1]+"]")
	f.close()