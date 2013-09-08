import sys
from lib import XenAPI

cached_host = None
session = None
api = None

def get_API_session(host, username, password):
  session = XenAPI.Session("http://%s" % host)
  try:
    session.xenapi.login_with_password(username, password)
  except Exception, e:
    msg = "Could not login to API session. Error: %s" % str(e)
    print msg
    raise Exception(msg)
  return session

def connect(host, username="root", password="xenroot"):
  global cached_host, session, api
  cached_host = host
  session = get_API_session(host, username, password)
  api = session.xenapi
  print "You now have the following objects to play with:"
  print "session - an API session object for %s." % host
  print "api - an API dispatcher for %s." % host

def usage():
  print "Usage: %s <hostname> <username> <password>" % sys.argv[0]

if __name__ == "__main__":
  print ""
  if len(sys.argv) < 2:
    usage()
  else:
    args = sys.argv[1:]
    connect(*args)
