from flask import Flask, render_template
from flask import request
import requests
import json


app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    myfile = open("index.html",mode = 'r')
    page   = myfile.read()
    myfile.close()
    return page

@app.route('/select_query/')
def select_query():
    data = request.args

    id = data.get('id')
    last_records_count = data.get('last_records_count')
    json_str = json.dumps({'id': id, 'last_records_count': int(last_records_count)})

    response = requests.get(url="http://21.3.52.168:8081", data=json_str)
    return str(utils.build_html_doc(response.json()))

@app.route('/insert_query/')
def insert_query():
    data = request.args

    birth = data.get('birth')
    name = data.get('name')
    species = data.get('species')
    role = data.get('role')
    sex = data.get('sex')

    json_str = json.dumps({
            "birth": birth,
            "name": name,
            "species": species,
            "role": int(role),
            "sex": int(sex)
        })
    print(json_str)
    response = requests.post(url="http://21.3.52.168:8081", data=json_str)
    return str(response.content)

@app.route('/update_query/')
def update_query():
    data = request.args

    id = data.get('id')
    birth = data.get('birth')
    name = data.get('name')
    species = data.get('species')
    role = data.get('role')
    sex = data.get('sex')

    json_str = json.dumps({
            "birth": birth,
            "name": name,
            "species": species,
            "role": int(role),
            "sex": int(sex)
        })
    print(json_str)
    response = requests.put(url="http://21.3.52.168:8081", data=json_str)
    return str(response.content)

@app.route('/delete_query/')
def delete_query():
    data = request.args

    id = data.get('id')
    json_str = json.dumps({
            "id": id
        })
    print(json_str)
    response = requests.delete(url="http://21.3.52.168:8081", data=json_str)
    return str(response.content)

if __name__ == "__main__":
    app.run(host="192.168.0.212",port="8082");

