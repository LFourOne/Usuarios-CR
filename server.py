from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

app.secret_key = "Shhhh, stay quiet!"

@app.route("/")
def index():
    return redirect ("/users")

@app.route("/users", methods=["GET"])
def read():
    users = User.get_all()
    return render_template("read.html", users=users)

@app.route("/user/new", methods=["POST", "GET"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    else:
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        User.save(data)
        return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)