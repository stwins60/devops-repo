from flask import Flask, jsonify
from flask_cors import CORS
from routes import api_bp
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
