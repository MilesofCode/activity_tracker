from flask import render_template, flash, redirect, url_for
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
    form = TrackerForm()
    table = form.name.data
    data_to_insert = {"date": form.date.data,
                      "calories": form.calories.data,
                      "push_ups": form.push_ups.data,
                      "sit_ups": form.sit_ups.data,
                      "pull_ups": form.pull_ups.data,
                      "miles_ran": form.miles_ran.data
                      }
    if form.validate_on_submit():
        insert_data(data_to_insert, table)
        return redirect(url_for('index'))
    return render_template('tracker.html',  title='Tacker', form=form)