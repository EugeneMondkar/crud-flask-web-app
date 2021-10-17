from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'This_is_my_secret_key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'toor'
app.config['MYSQL_DB'] = 'crud'


mysql = MySQL(app)


@app.route('/')
def index():

    cursor = mysql.connection.cursor()
    cursor.execute('select * from students')
    data = cursor.fetchall()

    return render_template("index.html", students=data)

@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        flash("Added student successfully.")

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cursor = mysql.connection.cursor()
        cursor.execute('insert into students (name, email, phone) values (%s, %s, %s)', (name, email, phone))
        mysql.connection.commit()

        return redirect(url_for('index'))

@app.route('/delete/<string:student_id>', methods=['GET'])
def delete(student_id):
    
    flash("Student has been deleted successfully")

    cursor = mysql.connection.cursor()
    cursor.execute('delete from students where id=%s', (student_id,))
    mysql.connection.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():

    if request.method == 'POST':

        flash("Updated student information successfully.")

        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cursor = mysql.connection.cursor()
        cursor.execute('update students set name=%s, email=%s, phone=%s where id=%s', (name, email, phone, id))
        mysql.connection.commit()

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)