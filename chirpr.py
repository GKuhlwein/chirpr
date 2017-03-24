from flask import Flask, request, g, render_template, redirect, url_for, flash, session

import db_access

app = Flask(__name__)


@app.route('/')
def index():
    if 'handle' in session:
        return redirect(url_for('chirps'))
    return render_template('index.html')


@app.route('/admin/users')
def users():
    user_list = db_access.get_all_users()
    following_list = db_access.get_all_followers()
    USERname = session['handle']
    logged = session['log']
    return render_template('admin/users.html', following=following_list, users=user_list, USERname=USERname, logged=logged)

    
@app.route('/admin/user/delete/<user_id>')
def delete_user(user_id):
    db_access.delete_user(user_id)
    handle = session['handle']
    user = db_access.get_user_by_handle(handle)
    if user:
        return redirect(url_for('users'))
    else:    
        return redirect(url_for('sign_out'))

        
@app.route('/admin/user/unfollow_user/<user_id>')
def unfollow_user(user_id):
    db_access.unfollow_user(user_id)
    handle = session['handle']
    user = db_access.get_user_by_handle(handle)
    return redirect(url_for('users'))

        
@app.route('/in/user/follow/<user_id>')
def follow_user(user_id):
    following = db_access.get_all_followers()
    handle = session['handle']
    lead_id = user_id
    user = db_access.get_user_by_handle(handle)
    follow_id = user['id']
    db_access.follow_user(lead_id, follow_id)
    return redirect(url_for('users'))
        

@app.route('/out')
def sign_out():
    del session['handle']
    del session['log']
    flash('Logged Out', 'success')
    return render_template('index.html')    
    
@app.route('/admin/user/sign_in', methods=['POST'])
def sign_in():
    handle = request.form.get('handle2')
    password = request.form.get('pass3')
    user = db_access.get_user_by_handle(handle)
    logged = False
    if user and password == user['password']:
        session['handle'] = handle
        logged = True
        session['log'] = logged
        flash('Login successful! Welcome ', 'success')
        return redirect(url_for('chirps'))
    else:
        flash('Incorrect username or password!', 'danger')
        return render_template('index.html')
   
    
@app.route('/admin/user/add', methods=['POST'])
def add_user():
    handle = request.form.get('handle')
    password = request.form.get('pass')
    password2 = request.form.get('pass2')
    hand = db_access.get_user_by_handle(handle)
    session['handle'] = handle
    logged = False
    if hand:
        flash('Username already taken!', 'danger')
        return render_template('index.html')
    
    if len(password) <= 5:
        flash('Password must be 6 characters!', 'danger')
        return render_template('index.html')
    else:
        if password == password2:
            flash('Login successful! Welcome ', 'success')
            db_access.add_user(handle, password)
            logged = True
            session['log'] = logged
            return redirect(url_for('chirps'))
        elif password != password2:
            flash('Passwords didn\'t match!', 'danger')
            return render_template('index.html')


@app.route('/in/chirp')
def chirp():
    USERname = session['handle']
    logged = session['log']
    db_access.chirp(post_id, post_body, handle)
    return render_template('admin/chirps.html', logged=logged, USERname=USERname)
    
            
@app.route('/in/chirps')
def chirps():
    USERname = session['handle']
    logged = session['log']
    chirp_list = db_access.get_all_chirps()
    return render_template('admin/chirps.html', chirps=chirp_list, logged=logged, USERname=USERname)


@app.route('/in/chirp/delete/<chirp_id>')
def delete_chirp(chirp_id):
    db_access.delete_chirp(chirp_id)
    return redirect(url_for('chirps'))


if __name__ == '__main__':
    app.secret_key = 'super_secret'
    app.run(debug=True)
