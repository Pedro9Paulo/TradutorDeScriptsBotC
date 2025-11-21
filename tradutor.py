import json
import os

# Função que lê o arquivo "f" com todos os papéis traduzidas e devolve um dicionário com as personagem indexado pelo id
def getTodos(f):
	todosRaw = f.read()
	todosList = todosRaw[2:-3].split(",\n  {")
	for i in range(1,len(todosList)):
		todosList[i] = "  {"+todosList[i]
	todos = {}
	for p in todosList:
		idi = p.find("_br")
		todos[p[15:idi]] = p
	f.close()
	return todos

# Função que a partir de um Json em inglês "f" e do dicionário com todos os papéis traduzidos "todos" monta um Json traduzido
def montaJson(f, todos, travellers):
	try:
		script = json.load(f)
		f.close()
		cenario = "[\n"
		viajantes = False
		for p in script:
			if type(p) == type({}):
				# Copia o meta (nome, autor, etc...) do script sem mudar nada
				if p["id"] == "_meta":
					cenario += "{"
					for item in p:
						if type(p[item]) == type(True):
							cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
						elif type(p[item]) == type([]):
							n = len(p[item])
							if n != 0:
								cenario += '"' + item + '": ' + "["
								for i in range(n):
									cenario += '"' + p[item][i] + '", '
								cenario = cenario[:-2] + "], "
						else:
							cenario += '"' + item + '": "' + p[item] + '", ' 
					cenario = cenario[:-2] + "},\n"
				else:
					# Pega o id do Json no formato antigo
					pid = p["id"].replace("_", "")
					pid = pid.replace("-", "")
					cenario += todos[pid] +",\n"
					# Cheque de se há viajantes no cenário
					if pid in travellers:
						viajantes = True
			else:
				# Pega o id do Json no formato novo
				pid = p.replace("_", "")
				pid = pid.replace("-", "")
				cenario += todos[pid] +",\n"
				# Cheque de se há viajantes no cenário
				if pid in travellers:
					viajantes = True
		if not viajantes:
			for vid in travellers:
				cenario += todos[vid] +",\n"
		cenario = cenario[:-2]+"\n]"
		return cenario
	except Exception as erro:
		return erro
