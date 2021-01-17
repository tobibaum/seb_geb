from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='.')

img_base = '/static/imgs/'
def make_page(img, _class="bottom-right", h=1000):
    return render_template("index.html", user_image=os.path.join(img_base, img),
                           img_class=_class, height=h)


state = 0
state_engine = [['sebvz.png', 'biersuche', 'top-left'],
                ['clue6.jpeg', 'crew republic foundation 11', 'bottom-right'],
                ['caesar.jpeg', 'vier vogel pils', 'bottom-right'],
                ['clue3.jpeg', 'schildkröte', 'bottom-right'],
                ['clue4.jpeg', 'hoegaarden', 'bottom-right'],
                ['4walls.png', 'maskenpflicht', 'bottom-right'],
                ['clue5.jpeg', 'strammer max', 'bottom-right'],
                ['sombrero.png', 'westmalle', 'bottom-right'],
                ['iduna.jpeg', 'dolden sud', 'bottom-right', 500],
               ]

@app.route('/')
def show_index():
    global state
    state = 0
    return make_page('sebvz.png', "top-left")

@app.route('/', methods=['POST'])
def my_form_post():
    global state
    global state_engine
    text = request.form['text']

    if state < len(state_engine) and text.lower() == state_engine[state][1]:
        state += 1
        print('state: %d'%state)

    if state >= len(state_engine):
        return make_page('congrats.png')

    if len(state_engine[state]) > 3:
        return make_page(state_engine[state][0], state_engine[state][2], h=state_engine[state][3])
    else:
        return make_page(state_engine[state][0], state_engine[state][2])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
