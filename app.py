from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    
    return "Updated version 7 Deployed Successfully via CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
