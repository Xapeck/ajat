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
<<<<<<< HEAD
	app.run(host='192.168.100.103', port=1080)
=======
	app.run(host='192.168.100.103', port=1050)
>>>>>>> cfde5f30ae1ba001f7d58853a9ca9fb190e801bc
