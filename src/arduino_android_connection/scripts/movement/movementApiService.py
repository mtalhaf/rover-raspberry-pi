#!/usr/bin/env python
from flask import Flask, request
#from printMessage import lcd_printMessage
app = Flask(__name__)

@app.route('/v1.0/movement/moveforward', methods=['GET'])
def moveRobotForward():
        #message = request.args.get('message')
	#lcd_printMessage(message)
	return "robot moving"

if __name__ == '__main__':
	app.run(host='0.0.0.0')

