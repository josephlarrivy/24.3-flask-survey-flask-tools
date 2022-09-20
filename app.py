from flask import Flask, request, render_template

app = Flask(__name__)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

from surveys import satisfaction_survey as survey





responses = []

@app.route('/')
def start_page():
    return render_template('/start_page.html', survey=survey)









if __name__ == '__main__':
    app.run()