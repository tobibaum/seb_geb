from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='.')

def make_page(img, _class="bottom-right"):
    return render_template("index.html", user_image=os.path.join(img_base, img),
                           img_class=_class)

img_base = '/static/imgs/'
@app.route('/')
def show_index():
    return make_page('sebvz.png', "top-left")

state = 0
state_engine = [['sebvz.png', 'biersuche', 'top-left'],
                ['sombrero.png', 'westmalle', 'bottom-right']
               ]

@app.route('/', methods=['POST'])
def my_form_post():
    global state
    global state_engine
    text = request.form['text']
    print(text)

    if text == state_engine[state][1]:
        state += 1
    if state > len(state_engine):
        return make_page('congrats.png')
    return make_page(state_engine[state][0], state_engine[state][2])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
