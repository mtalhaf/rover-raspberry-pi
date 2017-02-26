#!/usr/bin/env python
from flask import Flask, request
import rospy
from movement.movementApiService import movement_api
from lcd.lcdApiService import lcd_api

#starting flask with the name
app = Flask(__name__)

#The following code registers the different resources available to the API
app.register_blueprint(movement_api)
app.register_blueprint(lcd_api)

#initiates the node and runs the Flask API on the raspbery Pi
if __name__ == '__main__':
        rospy.init_node('RoverApiService', anonymous=True, log_level=rospy.INFO, disable_signals=True)
	app.run(host='0.0.0.0')

