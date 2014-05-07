import httplib
import json
#import datetime
import urllib

def get_events():
    conn = httplib.HTTPConnection( "api.meetup.com" )
    args = { 'key' : '442f3a1b5a6a37464b2f1a57326c3752', 'group_urlname' : 'Coders-Hackers-Founders' }
    encoded_args = urllib.urlencode( args )
    conn.request( "GET", '/2/events.json/?' + encoded_args )
    
    res = conn.getresponse()
    
    if res.status == 200:
        result = res.read()
        j = json.loads( result )
        return j['results']

def load_events():
    pass

if __name__ == '__main__':
    get_events()    