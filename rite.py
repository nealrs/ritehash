# Use RiteTag API (http://ritetag.com/rest-api) to get list of similar hashtags & their viral potential.
# API Doc: http://docs.ritetag.apiary.io/
#
# Usage:   python rite.py <query term>
# Example: python rite.py hackathon
#
# Why did I made this? Because I'm a marketer / social manager and want to know which hashtags are most likely to get picked up/amplify my content. 
# Licensed under MIT License - 2014 - Neal Shyam [nealshyam.com | @nealrs]

import requests
from requests_oauthlib import OAuth1
import json
import sys

# Get your tokens & keys @ http://ritetag.com/developer/signup
ck = "consumer key"
cs = "consumer secret"
ot = "oauth token"
os = "oauth token secret"

if (len(sys.argv)>1):
	t = sys.argv[1]
else: 
	print "No query defined, defaulting to 'internet'"
	t = 'internet'

url = "http://ritetag.com/api/v2/ai/twitter/"+t
auth = OAuth1(ck, cs, ot, os)
r = requests.get(url, auth=auth)

print "query:",t
print "status:",r.status_code
print "data:\n"+json.dumps(r.json(), indent=4, sort_keys=True)
