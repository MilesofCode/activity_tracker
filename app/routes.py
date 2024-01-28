from flask import render_template, redirect, url_for
from app.init import app
from app.forms import LoginForm, TrackerForm
from app.models import *


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            if username not in list_table():
                create_table(username)
            else:
                return redirect(url_for('index'))
            return redirect(url_for('index'))
        return render_template('login.html',  title='Create_DB', form=form)
    except:
        return redirect(url_for('index'))


@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    # need a list of tuples for dynamic select field in form
    ids = []
    for i in range(0, len(list_table())):
        ids.append(i)
    table_list = [(ids[i], list_table()[i]) for i in range(0, len(list_table()))]

    form = TrackerForm()
    form.name.choices = table_list
    data_to_insert = {"date": form.date.data,
                      "calories": form.calories.data,
                      "push_ups": form.push_ups.data,
                      "sit_ups": form.sit_ups.data,
                      "pull_ups": form.pull_ups.data,
                      "miles_ran": form.miles_ran.data
                      }
    if form.validate_on_submit():
        table = table_list[form.name.data][1]
        insert_data(data_to_insert, table)
        return redirect(url_for('index'))
    return render_template('tracker.html', title='Tracker', form=form)
