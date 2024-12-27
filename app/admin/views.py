from flask import render_template, redirect, url_for, jsonify, request
from flask_login import login_user, login_required
import markdown
from . import admin
from ..model import db, Admin, Article
from ..forms import Login, ArticleForm

@admin.route('/', methods=['GET', 'POST'])
def admin_home():
    form=Login()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        admin=Admin.query.filter_by(name = username).first_or_404()
        if admin.verify_password(password):
            login_user(admin)       #user successfully login
            return redirect(url_for('admin.verify'))
    return render_template('/admin/login.html', login_form=form)

@admin.route('/verify', methods=['GET','POST'])
@login_required
def verify():
    articles=Article.query.all()
    form=ArticleForm()
    if form.validate_on_submit():
        title=form.title.data
        desc=form.textarea.data
        html = markdown.markdown(desc)
        try:
            #hide only can have two value '' or '1'(digit)
            id = int(form.hide.data)
            arti=Article.query.get(id)
            arti.name = title
            arti.markdown_text = desc
            arti.html_text = html
        except ValueError as e:
            arti=Article(name = title, markdown_text = desc, html_text = html)
            db.session.add(arti)
        db.session.commit()
        return redirect(url_for('.verify'))
    return render_template('admin/home.html', article=articles, form=form)

@admin.route('/artinfo', methods=['POST'])
def info():
    id = request.get_json()
    article = Article.query.get(id)
    if article is None:
        #article not exits
        pass
    return jsonify(article.to_json())

@admin.get('/del')
def delete():
    title=request.args.get('title')
    target = Article.query.filter_by(name = title).first_or_404()
    db.session.delete(target)
    db.session.commit()
    return redirect(url_for('.verify'))

@admin.get('/not')
def four():
    return render_template('404.html')