from flask import Flask

app = Flask(__name__)

@app.route("/")
def login():
    return "첫 화면인 로그인 페이지"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")