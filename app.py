from flask import Flask 
import os 
import socket 

app = Flask(__name__) 

@app.route("/") 
def ajat():
    html = "<html><head><meta name="""viewport""" content="""width=device-width, initial-scale=1"""></head><STYLE type="""text/css"""> \
    BODY { text-align: center}
    BODY { font-size:140%;}
    </STYLE><body><h3>Inan Taksiajat (2.9.-11.10.2019)</h3>" \
    "<b>MA: 8:15 - 13:40<br/>TI: 7:25 - 13:35<br/>KE: 8:15 - 12:20<br/>TO: 7:45 - 13:45<br/>PE: 7:25 - 13:25</b><br/></body>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='1080', debug=True)
