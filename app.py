from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static')

# Configure MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'events_scheduler'
mysql = MySQL(app)

# Import routes after initializing the app and mysql
from controllers.home_controller import home_page, privacy, events, add_event, delete_event, edit_event, update_event

app.add_url_rule('/', 'home', home_page)
app.add_url_rule('/privacy', 'privacy', privacy)
app.add_url_rule('/events', 'events', events)
app.add_url_rule('/events/new', 'new_event', add_event, add_event, methods=['GET', 'POST'])
app.add_url_rule('/events/delete/<int:event_id>', 'delete_event', delete_event, methods=['POST'])
app.add_url_rule('/events/<int:event_id>/edit', 'edit_event', edit_event, methods=['GET'])
app.add_url_rule('/events/<int:event_id>/edit', 'update_event', update_event, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
