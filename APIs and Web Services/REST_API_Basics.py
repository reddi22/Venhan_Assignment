# Importing the Flask and Jsonify 
from flask import Flask, jsonify

#Creating the Flask instance
app = Flask(__name__)

#Defining 
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    message = f"Hello, {name}!"
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)