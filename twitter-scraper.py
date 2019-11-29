from scraper import Scraper, DeltaScraper
import os
import twitter

class Twitter(DeltaScraper):
    owner = "IgnoredAmbience"
    repo = "twitter-followers-tracker"
    committer = {"name": "twitter-checker", "email": "none@example.com"}

    record_key = "id_str"
    show_changes = True
    noun = "user"

    def __init__(self, twitter, github_token):
        self.api = twitter
        super().__init__(github_token)

    def display_record(self, user):
        return f'  {user["screen_name"]} ({user["id_str"]})'

    def display_changes(self, old_user, new_user):
        changes = []

        key = 'screen_name'
        #for key in old_user:
        prev = old_user[key]
        next = new_user.get(key)
        if prev != next:
            changes.append("{}: {} => {}".format(old_user['str_id'], prev, next))
        #endfor

        return "\n".join(changes)

class Friends(Twitter):
    filepath = 'friends.json'

    def fetch_data(self):
        return list(map(lambda x : x.AsDict(), self.api.GetFriends(skip_status=True)))

class Followers(Twitter):
    filepath = 'followers.json'

    def fetch_data(self):
        return list(map(lambda x : x.AsDict(), self.api.GetFollowers(skip_status=True)))

if __name__ == "__main__":
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token is None:
        Scraper.test_mode = True

    api = twitter.Api(consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
                      consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
                      access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
                      access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

    friends = Friends(api, github_token)
    friends.scrape_and_store()

    followers = Followers(api, github_token)
    followers.scrape_and_store()
