import json
f = open("ptbr/all.json", encoding="utf-8")
todosRaw = f.read()
todosList = todosRaw[2:-2].split(",\n  {")
for i in range(1,len(todosList)):
	todosList[i] = "  {"+todosList[i]
todos = {}
for p in todosList:
	idi = p.find("_br")
	todos[p[15:idi]] = p
name = input()
f = open(name+".json")
script = json.load(f)
f.close()
cenario = "[\n"
for p in script:
	if p["id"] == "_meta":
		cenario += "{"
		for item in p:
			cenario += '"' + item + '": "' + p[item] + '", ' 
		cenario = cenario[:-2] + "},\n"
	else:
		cenario += todos[p["id"]] +",\n"
f = open("ptbr/"+name+".json", "w", encoding="utf-8")
f.write(cenario[:-2]+"\n]")
f.close()



