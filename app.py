from flask import Flask, request, render_template, flash, abort, url_for

from utils import import_data, get_candidate_by_name, get_candidate_by_skill, get_candidate_by_id

app = Flask(__name__)
app.secret_key = 'ss63kdhGs8u192_dmnksMM93'


@app.route('/')
def home_page():
    if staff := import_data():
        return render_template('list.html', items=staff)
    flash('JSON file with candidates not found')
    return render_template('list.html', items=[])


@app.route('/candidate/<int:uid>')
def candidate_page(uid):
    if uid < 1:
        abort(400, 'Invalid ID')
    if staff := import_data():
        if uid > len(staff) + 1:
            abort(404, f"Candidate {uid} doesn't exist")
        candidate = get_candidate_by_id(staff, uid)
        return render_template('card.html', person=candidate, skills=', '.join(candidate.skills))
    flash('JSON file with candidates not found')
    return render_template('card.html', person=None, skills='')


@app.route('/search/<name>')
def name_page(name):
    if staff := import_data():
        people = get_candidate_by_name(staff, name)
        if people:
            return render_template('search.html', items=people, num=len(people))
        abort(404, f'Name {name} not found')
    return render_template('search.html', items=[], num=0)


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
