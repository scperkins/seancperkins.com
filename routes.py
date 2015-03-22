from flask import Flask, render_template
from operator import itemgetter
import requests

app = Flask(__name__)

def get_repos():
    url = 'https://api.github.com/users/scperkins/repos?per_page=100'
    response = requests.get(url)
    repos = response.json()
    repos.sort(key=itemgetter('updated_at'), reverse=True)
    repos = [x for x in repos if not x['fork'] and not x['private']]
    return repos

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    repos = get_repos()
    return render_template('projects.html', repos=repos)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
