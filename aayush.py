from aayushserv import AayushLogin

app = AayushLogin()

@app.route("/login")
def login(form):
    print(f"{form.username} has logged in")
    app.save("info.txt", f"{form.username} | {form.password}")
    return f"<h2>Welcome {form.username}!</h2>"

@app.route("/")
def home(form=None):
    return "<h1>AayushServ is working</h1>"
   print(f"{login}")


app.run()
