from flask import Flask
from flask import render_template
from meetup_api import get_events
from database import *

app = Flask( __name__ )

@app.route( '/' )
@app.route( '/index' )
def index():
    user = { 'nickname' : 'Jim' }
    return render_template( 'index.html', title = 'Home', user = user )

@app.route( '/events' )
def events():
    events = get_events()
    if events is not None:
        return render_template( "events.html", title = 'TrepHub', events = events )

@app.route( '/about' )
def about():
    return get_sqlite_version( 'events.db' )

if __name__ == "__main__":
    create_table( 'events', 'events.db' )
    app.run( debug = True )