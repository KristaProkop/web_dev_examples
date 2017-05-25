
from flask import Flask, redirect, render_template, request

from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')

@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends) 

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit', methods=['GET'])
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': friend_id}
    friend = mysql.query_db(query, data)
    mysql.query_db(query, data)
    return render_template('friends.html', friend=friend)


@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
    data =  {'id': friend_id, 'first_name': request.form['first_name'], 'last_name':  request.form['last_name'], 'email': request.form['email']
    }
    friends = mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)




# 