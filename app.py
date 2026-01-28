from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza el archivo index.html ubicado en templates/
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)