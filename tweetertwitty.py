import tweepy

auth = tweepy.OAuth1UserHandler(
  'Xd*********iU', 'guRt**************Etyi7QycMT', '2170396651-*************K0aEYa', 'b*************'
)

api = tweepy.API(auth)
user = api.get_user(screen_name="Twitter")

print(user.name)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.TweepError as e:
    if 'Rate limit exceeded' in e.reason:
      time.sleep(1000)
    else:
      raise
# generous bot
for follower in tweepy.Cursor(api.followers).items():


