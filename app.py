from flask import Flask  # Import Flask framework
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Welcome to the Fun Web App!</h1>"  # Define a simple web page
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Start Flask web server