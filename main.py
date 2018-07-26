import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.ext import ndb
from models import user_info

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

#To check if a user is logged in
def LoginStuff():
    user = users.get_current_user()
    if user:
        #user is logged in
        user_info_list =  user_info.query(user_info.userid == user.user_id()).fetch()

log_url = users.create_logout_url('/')
logout = {
    'log_url': log_url,
}
#also a part of it to see if a user is logged in ^

class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #user is logged in
            log_url = users.create_logout_url('/')
            log_message = 'Sign out'
            user_info_list =  user_info.query(user_info.userid == user.user_id()).fetch()
        else:
            #user not logged in
            log_url = users.create_login_url('/')
            log_message = "Sign in"

        template = jinja_environment.get_template('home.html')
        variables = { 'user': user,
                     'log_url' : log_url,
                     'log_message' : log_message}
        self.response.out.write(template.render(variables))

class StartGamePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template2 = jinja_environment.get_template('story.html')
            self.response.out.write(template2.render(logout))
        else:
            template = jinja_environment.get_template('home.html')
            self.redirect('/')
            self.response.out.write(template.render())
        LoginStuff()

class AboutPage(webapp2.RequestHandler):
    def get(self):
        template3 = jinja_environment.get_template('about.html')
        self.response.out.write(template3.render())

class Leaderboard(webapp2.RequestHandler):
    def get(self):
        template4 = jinja_environment.get_template('leaderboard.html')
        self.response.out.write(template4.render())

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/start', StartGamePage),
    ('/about', AboutPage),
    ('/leaderboard', Leaderboard),
], debug=True)
