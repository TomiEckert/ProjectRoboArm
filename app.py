from flask import Flask
from flask import request
import time
import subprocess
import servos
import ai

app = Flask(__name__)

def change_address(text):
  ip = subprocess.check_output(["hostname", "-I"])
  ip = str(ip).replace("b'", "")
  ip = str(ip).replace(" \\n'", "")
  if len(str(ip).split(" ")):
    ip = str(ip).split(" ")[1]
  result = text.replace('<|IP|>', ip)
  return result

@app.route("/")

def web_interface():
  html = open("index.html")
  response = html.read().replace('\n', '')
  response = change_address(response)

  html.close()
  return response

@app.route("/set_coordinates")

def set_coordinates():
  coords = request.args.get("coords")
  xCoord = coords.split(":")[0]
  yCoord = coords.split(":")[1]
  values = ai.getValues(xCoord, yCoord)
  servos.set_elbow(values[0])
  servos.set_shoulder(values[1])
  servos.set_base(values[2])

@app.route("/set_servo1")

def set_servo1():
  speed = request.args.get("speed")
  print( "Received " + str(speed))
  servos.set_grabber(speed)
  return "Received " + str(speed)

@app.route("/set_servo2")

def set_servo2():
  speed = request.args.get("speed")
  print( "Received " + str(speed))
  servos.set_elbow(speed)
  return "Received " + str(speed)

@app.route("/set_servo3")

def set_servo3():
  speed = request.args.get("speed")
  print( "Received " + str(speed))
  servos.set_shoulder(speed)
  return "Received " + str(speed)

@app.route("/set_servo4")

def set_servo4():
  speed = request.args.get("speed")
  print ("Received " + str(speed))
  servos.set_base(speed)
  return "Received " + str(speed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181, debug=True)
