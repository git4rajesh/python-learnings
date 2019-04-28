from flask import Flask, render_template

app = Flask(__name__)

@app.route('/artifacts/')
def display_artifacts():
    artifacts = {'Rally': 'Feature', 'ProjectPlace': 'WorkSpace',
                     'Planview': 'Project'}

    return render_template('dict_template.html', dict_artifact = artifacts)

@app.route('/navbar/')
def display_navbar():
    return render_template('nav_template.html')


if __name__ == '__main__':
    app.run(debug=True)
