from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_page = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deployment Status - Version 3</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #00bcd4, #3f51b5);
                color: #fff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(8px);
                max-width: 600px;
                animation: fadeIn 1.2s ease-in-out;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 15px;
            }
            p {
                font-size: 1.2rem;
                line-height: 1.6;
            }
            .version-badge {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 18px;
                background-color: #ff9800;
                color: white;
                font-weight: bold;
                border-radius: 25px;
                font-size: 1rem;
            }
            footer {
                margin-top: 30px;
                font-size: 0.9rem;
                color: #ddd;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Deployment Successful!</h1>
            <p>Updated <strong>Version 5</strong> has been successfully deployed using an automated <strong>CI/CD pipeline</strong> through <strong>Google Cloud Platform (GCP)</strong>.</p>
            <span class="version-badge">Version 3</span>
            <footer>
                <p>© 2025 CI/CD Automated Deployment | Flask + GCP</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
