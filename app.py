from flask import Flask, render_template
from flask_cors import CORS
from models import db
from config import Config

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(Config)
db.init_app(app)

CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})

app.register_blueprint(user_bp)
app.register_blueprint(mfa_bp)
app.register_blueprint(deepseek_bp)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT, debug=True)
