from flask import Flask,render_template
from UserDAO import UserDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Bonjour, World!</p>"

@app.route("/users_old")
def show_users_old():
    html=""
    dao = UserDAO('formation.db')
    
    users = dao.findAll()
    for user in users:
        html+=f"""
        <tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
        """
    
    return f"<table>{html}</table>"

@app.route("/users")
def show_users():
    html=""
    dao = UserDAO('formation.db')
    users = dao.findAll()
    
    # from flask import Flask,render_template
    return render_template("users_list.html",users=users)