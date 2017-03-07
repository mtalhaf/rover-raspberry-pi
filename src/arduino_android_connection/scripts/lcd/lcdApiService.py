#!/usr/bin/env python
from flask import Flask, request, Blueprint
from lcdPublishers import *

#makes a lcd blueprint which can be used in the main API
lcd_api = Blueprint('lcd_api', __name__)

#added route which will print a message on the lcd
@lcd_api.route('/v1.0/lcd/print', methods=['GET'])
def printMessageOnLcd():
        message = request.args.get('message')
	lcd_printMessage(message)
	return "message printed"

