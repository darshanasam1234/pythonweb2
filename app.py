from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Hello {name}! Your email address is {email}."
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
