# twitter-followers-tracker

Tracking my twitter followings, followers, and whether they surreptitiously change their handles or identities.

Repository inspired by @simonw's [disaster-scrapers](https://github.com/simonw/disaster-scrapers).

## Setup Notes
1. Obtain a [Twitter Developer account](https://developer.twitter.com/).
2. [Create a new Twitter application](https://developer.twitter.com/en/apps). The application does not need any
   additional settings, and requires Read-Only permissions of its users.
3. Generate and keep to hand Consumer API Keys (to authenticate the app), and an Access token & Access token secret (to
   authenticate against your own user account). All of these can be regenerated in the App's settings pages.
4. Add the following secrets from your Twitter app to the GitHub repository:

   | Name | Value (from Twitter app) |
   |------|--------------------------|
   | `TWITTER_CONSUMER_KEY` | Consumer API Key |
   | `TWITTER_CONSUMER_SECRET` | Consumer API Secret Key |
   | `TWITTER_ACCESS_TOKEN` | Access Token |
   | `TWITTER_ACCESS_SECRET` | Access Token Secret |

5. The script will be run automatically every hour, or on push to the `code` branch.
