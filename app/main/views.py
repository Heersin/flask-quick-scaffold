from flask import render_template, redirect, request, url_for, flash
from .forms import ClientForm
from . import main, mychart
import os
from app.models import Client


@main.route('/')
def root():
    return redirect(url_for('main.index'))

@main.route('/index')
def index():
    return render_template('main/new_index.html')


@main.route('/report/<mode>', methods=['GET', 'POST'])
def report(mode):
    REMOTE_HOST="https://pyecharts.github.io/assets/js"
    liquid = mychart.liquid.render_embed()
    parallel = mychart.parallel.render_embed()
    heatmap = mychart.heatmap.render_embed()
    print(os.getcwd())
    
    
    if request.method == 'POST':
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        if mode == '1':
            return render_template('main/new_report.html',chart=liquid, host=REMOTE_HOST)
        elif mode == '2':
            return render_template('main/new_report.html',chart=parallel, host=REMOTE_HOST)
        elif mode == '3':
            return render_template('main/new_report.html',chart=heatmap, host=REMOTE_HOST)
        else:
            return render_template('errors/404.html')
    else:
        return render_template('errors/404.html')

