from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    favorite_color = ""
    if request.method == 'POST':
        favorite_color = request.form.get('color')
    return render_template('index.html', color=favorite_color)

if __name__ == '__main__':
    app.run(debug=True)
    