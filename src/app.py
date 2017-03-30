from libs.bottle import route, request, run, static_file
import json

"""
@route('/api/activities')
def activities():
    activities = allActivities()
    jsonActivities = []
    for activity in activities:
        jsonActivities.append(activity.__dict__)
    return { "activities" : jsonActivities }
"""


@route('/')
def server_static():
    return static_file('index.html', root='./public', mimetype="text/html")

run(host='localhost', port=10078)
