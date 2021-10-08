from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import logging
      
# in case if facing issues with pip: curl https://bootstrap.pypa.io/get-pip.py | python3
import mysql.connector  # pip3 install mysql-connector-python
import requests  
      
import time
import sys
try:
        r = requests.post('http://graph.facebook.com/')
        print("Returning a kind of token as a result of a Facebook API test call " + r.json()['error']['fbtrace_id'])
except:
        print(
            "well ok something happened with your internet connection ")
      
      
try:
        db = mysql.connector.connect(
            host="",
            user="admin",
            passwd="15doramu15",
            database="database-2",
        )
class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length']) 
        request_data = self.rfile.read(content_length).decode('utf-8') 

        select_data = json.loads(request_data)

        records = []
        if select_data["last_records_count"] == 1:
            if select_data["id"]:
                records = mysql.connector.select_records_from_db(connection, cursor, select_data["last_records_count"], select_data["id"])
        else:
            records = mysql.connector.select_records_from_db(connection, cursor, select_data["last_records_count"])

        if len(records) == 0:
            self.wfile.write(bytes(json.dumps({'Error': "No such record in database"}), "utf8"))
            mysql.connector.rollback(connection, cursor)
            return

        results = []
        for row in records:
            results.append(dict({'id': row[0], 
                                 'birth': row[1], 
                                 'name': row[2], 
                                 'species': row[3], 
                                 'role': int(row[4]), 
                                 'sex': row[5]}))

        self.wfile.write(bytes(json.dumps(results, indent=2), "utf8"));


    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length']) 
        request_data = self.rfile.read(content_length).decode('utf-8') 

        insert_data = json.loads(request_data)

        if insert_data["birth"] and insert_data["name"] and insert_data["species"] and insert_data["role"] and insert_data["sex"]:
            count = mysql.connector.insert_record_to_db(connection, cursor, 
                                                     insert_data["birth"], 
                                                     insert_data["name"], 
                                                     insert_data["species"], 
                                                     insert_data["role"], 
                                                     int(insert_data["sex"]))
            if count < 1:
                self.wfile.write(bytes("Incorrect data fields", "utf8"))
                mysql.connector.rollback()
                return
            else:
                self.wfile.write(bytes("Written successfully", "utf8"))
                return
        else:
            self.wfile.write(bytes("Empty date fields", "utf8"))
            return

    def do_PUT(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length']) 
        request_data = self.rfile.read(content_length).decode('utf-8') 

        update_data = json.loads(request_data)
        if update_data["id"] and update_data["birth"] and update_data["name"] and update_data["species"] and update_data["role"] and update_data["sex"]:
            count = mysql.connector.update_records_from_db(connection, cursor, 
                                                     update_data["id"],
                                                     update_data["birth"], 
                                                     update_data["name"], 
                                                     bool(update_data["species"]), 
                                                     update_data["role"], 
                                                     int(update_data["sex"]))
            if count < 1:
                self.wfile.write(bytes("Incorrect data fields", "utf8"))
                mysql.connector.rollback()
                return
            else:
                self.wfile.write(bytes("Written successfully", "utf8"))
                return
        else:
            self.wfile.write(bytes("Empty date fields", "utf8"))
            return

    def do_DELETE(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length']) 
        request_data = self.rfile.read(content_length).decode('utf-8') 
        delete_data = json.loads(request_data)
        if delete_data["id"]:
            count = postgres_api.delete_records_from_db(connection, cursor, delete_data["id"])
            if count < 1:
                self.wfile.write(bytes("Incorrect data fields", "utf8"))
                mysql.connector.rollback()
            else:
                self.wfile.write(bytes("Written successfully", "utf8"))
        else:
            self.wfile.write(bytes("Empty id field", "utf8"))



def run(server_class=HTTPServer, handler_class=HandleRequests, port=8081):
    server_address = ('172.18.0.5', port)
    httpd = server_class(server_address, handler_class)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

def isBlank (my_string):
    if not my_string:
        return False
    return True


if __name__ == '__main__':


    if len(argv) == 2:
        port = int(argv[1])
        run(port)
except:
        print("something went wrong")
      
