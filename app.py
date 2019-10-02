# Tyttöjen kouluajat.

from flask import Flask 
import os 
import socket 

app = Flask(__name__) 

@app.route("/") 
def ajat():
    html = "<h3>Inan Taksiajat (2.9.-11.10.2019)</h3>" \
	"<b>MA: 8:15 - 13:40<br/>TI: 7:25 - 13:35<br/>KE: 8:15 - 12:20<br/>TO: 7:45 - 13:45<br/>PE: 7:25 - 13:25</b><br/>" \
           "<b>Hostname:</b> {hostname}<br/>" 
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
