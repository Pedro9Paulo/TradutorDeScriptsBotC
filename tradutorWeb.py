from flask import Flask, make_response, request
import json
import requests
app = Flask(__name__)

def traduz(script):

    arquivo_all = open("/home/pedro9paulo/all.json", "r", encoding="utf8")
    todosRaw = arquivo_all.read()
    todosList = todosRaw[2:-3].split(",\n  {")
    for i in range(1,len(todosList)):
        todosList[i] = "  {"+todosList[i]
    todos = {}
    for p in todosList:
        idi = p.find("_br")
        todos[p[15:idi]] = p

    try:
        cenario = "[\n"
        for p in script:
            if type(p) == type({}):
                # Copia o meta (nome, autor, etc...) do script sem mudar nada
                if p["id"] == "_meta":
                    cenario += "{"
                    for item in p:
                        if type(p[item]) == type(True):
                            cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
                        else:
                            cenario += '"' + item + '": "' + p[item] + '", '
                    cenario = cenario[:-2] + "},\n"
                else:
                    # Pega o id do Json no formato antigo
                    pid = p["id"].replace("_", "")
                    pid = pid.replace("-", "")
                    cenario += todos[pid] +",\n"
            else:
                # Pega o id fo Json no formato novo
                pid = p.replace("_", "")
                pid = pid.replace("-", "")
                cenario += todos[pid] +",\n"
        cenario = cenario[:-2]+"\n]"
        return cenario
    except Exception as erro:
        return erro



@app.route('/')
def form():
    return """
        <html>
            <head>
                <title> Tradutor BotC </title>
                <link rel="icon" type="imp/png" href="https://pedro9paulo.pythonanywhere.com/images/imp.png">
            </head>
            <body style="background-color:#210062;color:white;text-align:center">
                <h1> <img style="vertical-align:middle" src="https://pedro9paulo.pythonanywhere.com/images/librarian.png" width="90" height="100"> Tradutor de Cenários de Blood on the Clocktower <img style="vertical-align:middle" src="https://raw.githubusercontent.com/Pedro9Paulo/TradutorDeScriptsBotC/main/images/librarian.png" width="90" height="100"></h1>
                <br>
                <p> Envie o Json que deseja traduzir do seu computador: </p>
                <br>
                <form action="/tradutor_upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
                <br>
                <p> OU insira o endereço do link: </p>
                <br>
                <form action="/tradutor_link" method="post" enctype="multipart/form-data">
                    <input type="form" name="url" />
                    <input type="submit" />
                </form>
                <br>
                <br>
                <br>
                <p> Contribua para esse projeto também: </p>
                <p> <a href="https://github.com/Pedro9Paulo/TradutorDeScriptsBotC"> <img src="https://pedro9paulo.pythonanywhere.com/images/legion.png" width="90" height="100"> </a></p>
            </body>
        </html>
    """

@app.route('/tradutor_upload', methods=["POST"])
def tradutor_upload():
    request_file = request.files['data_file']
    if not request_file:
        return "Sem arquivo"

    try:
        script = json.load(request_file)
    except:
        return "ERRO: O Arquivo não é um Json válido"

    result = traduz(script)

    if type(result) == type("string"):

        response = make_response(result)
        response.headers["Content-Disposition"] = "attachment; filename="+request_file.filename
        return response
    else:
        return str(result)

@app.route('/tradutor_link', methods=["POST", "GET"])
def tradutor_link():
    request_url = request.form.get("url")
    request_file = requests.get(request_url)
    if not request_file:
        return "Sem arquivo"

    try:
        script = request_file.json()
    except:
        return "ERRO: O Arquivo não é um Json válido"
    result = traduz(script)

    if type(result) == type("string"):
        response = make_response(result)
        filename = ""
        try:
            filename = script[0]["name"] + ".json"
        except:
            filename = "cenario.json"
        response.headers["Content-Disposition"] = "attachment; filename="+filename
        return response
    else:
        return str(result)