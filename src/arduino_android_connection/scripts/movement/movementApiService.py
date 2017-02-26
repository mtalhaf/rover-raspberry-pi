#!/usr/bin/env python
from flask import Flask, request, Blueprint
from movementPublishers import *

movement_api = Blueprint('movement_api', __name__)

@movement_api.route('/v1.0/movement/moveforward', methods=['GET'])
def moveRobotForward():
        movement_moveForward()
	return "robot moving"

