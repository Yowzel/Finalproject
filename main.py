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


class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #user is logged in
            log_url = users.create_logout_url('/')
            log_message = 'Sign out'
            user_info_list =  user_info.query(user_info.userid == user.user_id()).fetch()
            if len(user_info_list)<1:
                test = user_info(user_nick= user.nickname(), user_email= user.email(), userid= user.user_id(), pagecount= 0)
            else:
                test = user_info_list[0]
            test.pagecount +=1
            test.put()
            pagecount = test.pagecount
        else:
            #user not logged in
            log_url = users.create_login_url('/')
            log_message = "Sign in"

        template = jinja_environment.get_template('home.html')
        variables = { 'user': user,
                     'log_url' : log_url,
                     'log_message' : log_message}
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', LoginPage),
], debug=True)
