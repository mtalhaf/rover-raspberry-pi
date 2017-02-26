#!/usr/bin/env python
from flask import Flask, request, Blueprint
#from printMessage import lcd_printMessage

movement_api = Blueprint('movement_api', __name__)

@movement_api.route('/v1.0/movement/moveforward', methods=['GET'])
def moveRobotForward():
        #message = request.args.get('message')
	#lcd_printMessage(message)
	return "robot moving"

