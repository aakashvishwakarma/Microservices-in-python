from flask import Flask, jsonify , render_template #jsonify use to convert any object into json object
import socket
application = app = Flask(__name__)

#function to fetch hostname and ip of the running machine
def fetchdetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    # print("Hostname :  ",host_name)
    # print("IP : ",host_ip)
    return str(hostname), str(host_ip)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/health")
def health():
    return jsonify(
        status = "up"
    )
@app.route("/details")
def details():
    hostname, ip = fetchdetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)