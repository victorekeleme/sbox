from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import threading
import asyncio

from core import handler
import concurrent.futures



app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

class BasicForm(FlaskForm):
    ids = StringField("ID",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/search",methods =['POST','GET'])
def main():
    form = BasicForm()

    if request.method == 'POST':
        try:
            magnet_link = str(request.form['ids'])
            #queue = []
            #queue.append(magnet_link)

            print(f"Inside flask function: {threading.current_thread().name}")
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(handler(magnet_link))
            print(result)     
            return result
        except:
            KeyError = 'ids'
    
    return render_template("/index.html", form = form)





if __name__ == "__main__":
    app.run(debug=True)