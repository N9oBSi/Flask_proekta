from flask import render_template, request, redirect, url_for
from flask import current_app as app

def home_page():
    return render_template('home.html')

def events():
    # Importing mysql here to avoid circular import
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, text, date FROM tasks ORDER BY date")
    events = cur.fetchall()
    cur.close()
    event_list = [{'id': event[0], 'text': event[1], 'date': event[2].isoformat()} for event in events]

    return render_template('events.html', events=event_list)

def add_event():
    from app import mysql
    if request.method == 'POST':
        event_text = request.form['text']
        event_date = request.form['date']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (text, date) VALUES (%s, %s)", (event_text, event_date))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('events'))
    
    return render_template('add_event.html')

def edit_event(event_id):
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, text, date FROM tasks WHERE id = %s", [event_id])
    event = cur.fetchone()
    cur.close()
    if event:
        event_data = {'id': event[0], 'text': event[1], 'date': event[2].isoformat()}
        return render_template('edit_event.html', event=event_data)
    return redirect(url_for('events'))

def update_event(event_id):
    from app import mysql
    if request.method == 'POST':
        event_text = request.form['text']
        event_date = request.form['date']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tasks SET text = %s, date = %s WHERE id = %s", (event_text, event_date, event_id))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('events'))

def delete_event(event_id):
    from app import mysql
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", [event_id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('events'))

def privacy():
    data = {
        'children': ['Mitko', 'Ivancho', 'Gosho'],
        'tracking_technologies': ['Camera', 'GPS', 'Microphone']
    }
    return render_template('privacy.html', data=data)
