import sqlite3

from flask import app, g

from chirpr import app

def get_all_chirps():
    conn = get_db()
    return conn.execute('''
        SELECT c.id, c.body, c.datetime, u.handle
        FROM chirp c, user u
        WHERE c.user_id = u.id
    ''').fetchall()

    
def chirp(post_id, post_body, handle):
    conn = get_db()
    conn.execute('INSERT INTO follow (post_id, post_body, handle) VALUES (:post_id, :post_body, handle)',
                {'post_id': post_id, 'post_body': post_body, 'handle': handle})
    
def delete_chirp(chirp_id):
    conn = get_db()
    conn.execute('DELETE FROM chirp WHERE id = :id', {'id': chirp_id})
    conn.commit()


def get_all_users():
    conn = get_db()
    return conn.execute('SELECT id, handle, admin FROM user').fetchall()
    
    
def follow_user(lead_id, follow_id):
    conn = get_db()
    conn.execute('INSERT INTO follow (lead_id, follow_id) VALUES (:lead_id, :follow_id)',
                {'lead_id': lead_id, 'follow_id': follow_id})
    conn.commit()
    

def get_all_followers():
    conn = get_db()
    return conn.execute('SELECT lead_id, follow_id FROM follow').fetchall()
    

def get_user_by_handle(handle):
    conn = get_db()
    return conn.execute('SELECT id, handle, password FROM user WHERE handle=:handle', {'handle': handle}).fetchone()
    

def delete_user(user_id):
    conn = get_db()
    conn.execute('DELETE FROM user WHERE id = :id', {'id': user_id})
    conn.commit()


def unfollow_user(user_id):
    conn = get_db()
    conn.execute('DELETE FROM follow WHERE lead_id = :lead_id', {'lead_id': user_id})
    conn.commit()
    

def add_user(handle, password):
    conn = get_db()
    conn.execute('INSERT INTO user (handle, admin, password) values (:handle, :admin, :password)',
                {'handle': handle, 'admin': 0, 'password': password})
    conn.commit()


def get_db():
    if not hasattr(g, 'chirpr.db'):
        g.conn = connect_db()
    return g.conn


def connect_db():
    conn = sqlite3.connect('data/chirpr.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'conn'):
        g.conn.close()
