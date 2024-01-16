import tweepy

auth = tweepy.OAuth1UserHandler(
  'Xd*********iU', 'guRt**************Etyi7QycMT', '2170396651-*************K0aEYa', 'b*************'
)

api = tweepy.API(auth)
user = api.get_user(screen_name="Twitter")

print(user.name)