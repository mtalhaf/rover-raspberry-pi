from flask import Flask
from printMessage import lcd_printMessage
app = Flask(__name__)

@app.route('/v1.0/lcd/print', methods=['GET'])
def printMessageOnLcd():
	lcd_printMessage("Hello from api")

if __name__ == '__main__':
	app.run(debug=True)

