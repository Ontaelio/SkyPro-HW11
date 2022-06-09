from flask import Flask, request, render_template

from utils import import_data, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def home_page():
    if staff := import_data():
        return render_template('list.html', items=staff)
    return 'File not found'


@app.route('/candidate/<int:uid>')
def candidate_page(uid):
    if uid < 1:
        return 'Incorrect ID'
    if staff := import_data():
        if uid > len(staff) + 1:
            return f"Candidate {uid} doesn't exist"
        return render_template('card.html', person=staff[uid - 1], skills=', '.join(staff[uid - 1].skills))
    return 'File not found'


@app.route('/search/<name>')
def name_page(name):
    if staff := import_data():
        people = get_candidate_by_name(staff, name)
        if people:
            return render_template('search.html', items=people, num=len(people))
        return f'Name {name} not found'
    return 'File not found'


@app.route('/skills/<skill>')
def skills_page(skill):
    if staff := import_data():
        people = get_candidate_by_skill(staff, skill)
        if people:
            return render_template('skill.html', items=people, skill=skill, num=len(people))
        return f'Skill {skill} not found'
    return 'File not found'


if __name__ == '__main__':
    app.run()
