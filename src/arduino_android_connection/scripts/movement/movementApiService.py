#!/usr/bin/env python
from flask import Flask, request, Blueprint
from movementPublishers import *

#makes a movement blueprint which can be used in the main API
movement_api = Blueprint('movement_api', __name__)

#added route which will move the rover forward
@movement_api.route('/v1.0/movement/moveforward', methods=['GET'])
def moveRobotForward():
        movement_moveForward()
	return "robot moving forward"

#added route which will move the rover backward
@movement_api.route('/v1.0/movement/movebackward', methods=['GET'])
def moveRobotBackward():
        movement_moveBackward()
	return "robot moving backward"

#added route which will turn the rover left
@movement_api.route('/v1.0/movement/turnleft', methods=['GET'])
def turnRobotLeft():
        movement_turnLeft()
	return "robot turning left"

#added route which will turn the rover right
@movement_api.route('/v1.0/movement/turnright', methods=['GET'])
def turnRobotRight():
        movement_turnRight()
	return "robot trning right"

