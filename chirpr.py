from flask import Flask, request, g, render_template, redirect, url_for, flash, session

import db_access

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin/users')
def users():
    user_list = db_access.get_all_users()
    return render_template('admin/users.html', users=user_list)


@app.route('/admin/user/delete/<user_id>')
def delete_user(user_id):
    db_access.delete_user(user_id)
    return redirect(url_for('users'))


@app.route('/admin/user/add', methods=['POST'])
def add_user():
    handle = request.form.get('handle')
    password = request.form.get('pass')
    hand = db_access.get_user_by_handle(handle)
    if hand:
        # TODO don't check twice!
        if handle in hand:
            flash('Username already taken!', 'danger')
            return render_template('index.html')
    
    if len(password) <= 5:
        flash('Password must be 6 characters!', 'danger')
        return render_template('index.html')
    else:
        flash('You were successfully logged in', 'success')
        db_access.add_user(handle, password)
        return redirect(url_for('users'))
    return render_template('index.html')


@app.route('/admin/chirps')
def chirps():
    chirp_list = db_access.get_all_chirps()
    return render_template('admin/chirps.html', chirps=chirp_list)


@app.route('/admin/chirp/delete/<chirp_id>')
def delete_chirp(chirp_id):
    db_access.delete_chirp(chirp_id)
    return redirect(url_for('chirps'))


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
