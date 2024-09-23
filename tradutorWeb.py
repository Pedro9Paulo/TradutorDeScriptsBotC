from flask import Flask, make_response, request
import json
import urllib
app = Flask(__name__)

def traduz(script):
    arquivo_ref = open("ptbr/all.json", encoding="utf-8")
    todosRaw = arquivo_ref.read()
    todosList = todosRaw[2:-2].split(",\n  {")
    for i in range(1,len(todosList)):
        todosList[i] = "  {"+todosList[i]
    todos = {}
    for p in todosList:
        idi = p.find("_br")
        todos[p[15:idi]] = p
        arquivo_ref.close()


    cenario = "[\n"
    for p in script:
        if type(p) == type({}):
            if p["id"] == "_meta":
                cenario += "{"
                for item in p:
                    if type(p[item]) == type(True):
                        cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
                    else:
                        cenario += '"' + item + '": "' + p[item] + '", ' 
                cenario = cenario[:-2] + "},\n"
            else:
                cenario += todos[p["id"].replace("_", "")] +",\n"
        else:
            cenario += todos[p.replace("_", "")] +",\n"
    return cenario[:-2]+"\n]"


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>Tradutor de Scripts</h1>

                <form action="/tradutor_upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
                <form action="/tradutor_link" method="post" enctype="multipart/form-data">
                    <input type="form" name="url" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/tradutor_upload', methods=["POST"])
def tradutor_upload():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    script = json.load(request_file)
    result = traduz(script)

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename="+request_file.filename
    return response

@app.route('/tradutor_link', methods=["POST", "GET"])
def tradutor_link():
    request_url = request.form.get("url")
    request_file = urllib.request.urlopen(request_url)
    print(request_file)
    if not request_file:
        return "No file"
    
    script = json.load(request_file)
    result = traduz(script)

    response = make_response(result)
    filename = ""
    try:
        filename = script[0]["name"] + ".json"
    except:
        filename = "cenario.json"
    response.headers["Content-Disposition"] = "attachment; filename="+filename
    return response