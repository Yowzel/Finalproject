from google.appengine.ext import ndb

class story_user(ndb.Model):
    user_nick =  ndb.StringProperty(required=True)
    user_email =  ndb.StringProperty(required=True)
    userid =  ndb.StringProperty(required=True)
    adventurecount = ndb.IntegerProperty(required=False)
    lives = ndb.IntegerProperty(required=False)
