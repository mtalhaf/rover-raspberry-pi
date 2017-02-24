#!/usr/bin/env python
from flask import Flask, request
from printMessage import lcd_printMessage
app = Flask(__name__)

@app.route('/v1.0/lcd/print', methods=['GET'])
def printMessageOnLcd():
        message = request.args.get('message')
	lcd_printMessage(message)
	return "message printed"

if __name__ == '__main__':
	app.run(debug=True)

