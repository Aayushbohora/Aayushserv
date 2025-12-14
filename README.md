Aayushserv

Aayushserv is a super simple Python library to create a local server for HTML login forms and basic POST/GET requests. Perfect for beginners learning backend basics without Flask or Django.

🚀 Installation

Install with pip:

pip install aayushserv


Works locally on your machine. No additional dependencies required.

💻 Basic Usage
Python Server
from aayushserv import AayushLogin

# Create server object
app = AayushLogin()

# Define login route
@app.route("/login")
def login(form):
    # Access form fields directly
    print(f"{form.username} has logged in")            # Terminal output
    app.save("info.txt", f"{form.username} | {form.password}")  # Save to file
    return f"<h2>Welcome {form.username}!</h2>"

# Run the server
app.run()


✅ Copy & Paste directly into your Python file

HTML Form (login.html)
<!DOCTYPE html>
<html>
<body>
<h2>Login</h2>
<form action="http://127.0.0.1:5000/login" method="post">
    <input type="text" name="username" placeholder="Username" required><br><br>
    <input type="password" name="password" placeholder="Password" required><br><br>
    <input type="submit" value="Login">
</form>
</body>
</html>


✅ Copy this into an HTML file and open in a browser

⚙️ How It Works

AayushLogin() → Creates the server object

@app.route("/path") → Listens for GET or POST requests

form.username / form.password → Access submitted HTML form data

app.save(filename, data) → Save any string to a file

app.run() → Starts the server (default: http://127.0.0.1:5000)

Terminal prints login info, saves it in info.txt, and responds to the browser.

✨ Features

Easy syntax for beginners

Handles HTML form submissions

Saves data to a file or prints to terminal

Works locally without external dependencies

Perfect for learning backend basics

📌 Notes

Only works on your local machine

For production or internet-facing servers, consider Flask, Django, or FastAPI

Ensure HTML form action matches your server URL

📂 Example Output

Terminal:

Aayush has logged in


info.txt:

Aayush | mypassword123


Browser:

Welcome Aayush!
