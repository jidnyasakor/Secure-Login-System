from flask import Flask,render_template,request,redirect,session,url_for,flash
import sqlite3
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.secret_key="secret123"

bcrypt=Bcrypt(app)

# Database setup
def init_db():
    conn=sqlite3.connect("database.db")
    c=conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")

# Register
@app.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        # Basic validation
        if len(username)<3:
            flash("Username too short")
            return redirect("/register")

        if len(password)<6:
            flash("Password minimum 6 characters")
            return redirect("/register")

        hashed=bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        try:
            conn=sqlite3.connect("database.db")
            c=conn.cursor()

            # Parameterized query prevents SQL Injection
            c.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username,hashed)
            )

            conn.commit()

            flash("Registration successful")
            return redirect("/login")

        except:
            flash("User already exists")

        finally:
            conn.close()

    return render_template("register.html")

# Login
@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        conn=sqlite3.connect("database.db")
        c=conn.cursor()

        c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
        )

        user=c.fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(
            user[2],
            password
        ):

            session["user"]=username
            return redirect("/dashboard")

        flash("Invalid credentials")

    return render_template("login.html")

# Protected page
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user"]
    )

# Logout
@app.route("/logout")
def logout():

    session.pop("user",None)

    flash("Logged out")
    return redirect("/login")


if __name__=="__main__":
    app.run(debug=True)