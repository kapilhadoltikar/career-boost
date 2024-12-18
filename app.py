from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template("user.html", username=username, password=password)
    return render_template("login.html")
    # if not username or password:
    #     return render_template("error.html")


@app.route("/user", methods=["GET", "POST"])
def user():
    return render_template("user.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        return render_template("user.html", name=name, email=email, password=password, repassword=repassword)
    return render_template("register.html")
        # if not name or email or password or repassword:
        #     return render_template("error.html")
        # return render_template("user.html")




if __name__ in '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)