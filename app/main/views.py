from flask import render_template
from ..model import Article
from . import  bp

@bp.route('/')
def home():
    articles = Article.query.all()
    for index, article in enumerate(articles):
        txt = Article.only_txt(article.html_text)
        if len(article.html_text) > 100:
            articles[index].txt = txt[:100]+'...'
        else:
            articles[index].txt = txt
    return render_template('index.html', articles=articles)

@bp.get('/blog/<int:id>')
def show(id):
    article=Article.query.get(id)
    return render_template('blog.html', article = article)
