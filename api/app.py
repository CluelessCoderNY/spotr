from flask import Flask, request, jsonify


# init app
app = Flask(__name__)

# run server
if __name__ == "__main__":
    app.run(debug=True)
