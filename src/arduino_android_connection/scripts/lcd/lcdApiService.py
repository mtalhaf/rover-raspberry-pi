#!/usr/bin/env python
from flask import Flask, request, Blueprint
from lcdPublishers import *

lcd_api = Blueprint('lcd_api', __name__)

@lcd_api.route('/v1.0/lcd/print', methods=['GET'])
def printMessageOnLcd():
        message = request.args.get('message')
	lcd_printMessage(message)
	return "message printed"

