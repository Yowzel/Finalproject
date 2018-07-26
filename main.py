import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.ext import ndb
from models import story_user

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

#To check if a user is logged in
def LoginStuff():
    user = users.get_current_user()
    if user:
        #user is logged in
        story_user_list =  story_user.query(story_user.userid == user.user_id()).fetch()

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
            story_user_list =  story_user.query(story_user.userid == user.user_id()).fetch()
            if len(story_user_list)<1:
                test = story_user(user_nick= user.nickname(), user_email= user.email(), userid= user.user_id(), adventurecount = 0)
            else:
                test = story_user_list[0]
            test.put()
        else:
            # story_user = story_user(key = key, nickname = user.nicname(), email = user.email())
            #user not logged in
            log_url = users.create_login_url('/')
            log_message = "Sign in"

        template = jinja_environment.get_template('home.html')
        variables = { 'user': user,
                     'log_url' : log_url,
                     'log_message' : log_message}
        self.response.out.write(template.render(variables))
    #     userstuff = story_user.query().fetch()
        # def get(self):
        #     # pagecount = 0
        #     user = users.get_current_user()
        #     if user:
        #         #user is logged in
        #         log_url = users.create_logout_url('/')
        #         log_message = 'Sign out'
        #         story_user_list =  story_user.query(story_user.userid == user.user_id()).fetch()
        #         if len(story_user_list)<1:
        #             test = story_user(user_nick= user.nickname(), user_email= user.email(), userid= user.user_id())
        #         else:
        #             test = story_user_list[0]
        #         # test.pagecount +=1
        #         # test.put()
        #         # pagecount = test.pagecount
        #     else:
        #         #user not logged in
        #         log_url = users.create_login_url('/')
        #         log_message = "Sign in"
        #     template = jinja_environment.get_template('home.html')
        #     variables = { 'user': user,
        #                      'log_url' : log_url,
        #                      'log_message' : log_message}
        #     self.response.out.write(template.render(variables))
        #     userstuff = story_user.query().fetch()

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

    def post(self):
        user = users.get_current_user()
        hello =  story_user.query(story_user.userid == user.user_id()).fetch()[0]
        if self.request.get('page2_1'):
            hello.adventurecount = 1
            hello.put()
        elif self.request.get('page2_2'):
            hello.adventurecount = 100
            hello.put()

class AboutPage(webapp2.RequestHandler):
    def get(self):
            user = users.get_current_user()
            if user:
                #user is logged in
                log_url = users.create_logout_url('/')
                log_message = 'Sign out'
                story_user_list =  story_user.query(story_user.userid == user.user_id()).fetch()
            else:
                #user not logged in
                log_url = users.create_login_url('/')
                log_message = "Sign in"
            variables = { 'user': user,
                         'log_url' : log_url,
                         'log_message' : log_message}
            template3 = jinja_environment.get_template('about.html')
            self.response.out.write(template3.render(variables))

class Leaderboard(webapp2.RequestHandler):
    def get(self):
        template4 = jinja_environment.get_template('leaderboard.html')
        self.response.out.write(template4.render())

class SavedPage(webapp2.RequestHandler):
    def post(self):
        print("hello world")


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/start', StartGamePage),
    ('/saved', SavedPage),
    ('/about', AboutPage),
    ('/leaderboard', Leaderboard),
], debug=True)
