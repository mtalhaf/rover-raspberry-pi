#!/usr/bin/env python
from flask import Flask, request, Blueprint
from movementPublishers import *

movement_api = Blueprint('movement_api', __name__)

@movement_api.route('/v1.0/movement/moveforward', methods=['GET'])
def moveRobotForward():
        movement_moveForward()
	return "robot moving forward"

@movement_api.route('/v1.0/movement/movebackward', methods=['GET'])
def moveRobotBackward():
        movement_moveBackward()
	return "robot moving backward"

@movement_api.route('/v1.0/movement/turnleft', methods=['GET'])
def turnRobotLeft():
        movement_turnLeft()
	return "robot turning left"

@movement_api.route('/v1.0/movement/turnright', methods=['GET'])
def turnRobotRight():
        movement_turnRight()
	return "robot trning right"

