from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    
    return "Updated Version 3 Deployed Successfully via CI/CD through GCP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
