from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def example_index():
    user = request.args.get('user')
    return "Hello Welcome: %s" % user


@app.route('/mypage')
def example_html():
    return '<h2> My Page </h2>'


@app.route('/profile/<user>')
def example_strings(user):
    return '<h1> Hi %s</h1>' % user


@app.route('/post/<int:post_id>')
def example_ints(post_id):
    return '<H1>This is the ID: %s </H1' % post_id


@app.route('/supported_methods', methods=['GET', 'POST'])
def example_methods():
    if request.method == 'GET':
        return '<h1> You are using Get </h1>'
    else:
        return '<h1> You are using Post method</h1>'


@app.route('/example/templates/<user>')
def example_templates(user):
    return render_template('profile.html', name=user)


@app.route('/example/bootstrap')
def example_bootstrap():
    return render_template('test_boot_strap.html')


@app.route('/example/bootstrap/navbar')
def example_bootstrap_navbar():
    return render_template('navbar_example.html')


if __name__ == '__main__':
    app.run()
