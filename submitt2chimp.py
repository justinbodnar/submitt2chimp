# -*- coding: utf-8 -*-
from submittable_api_client.submittable_api_client import SubmittableAPIClient

##################
# basic workflow #

# API information
SubmittableAPIToken = 'REMOVED'
Client = SubmittableAPIClient(username="books@etruscanpress.org", apitoken=SubmittableAPIToken)

# get list of submitters
submitters = Client.submitters(page=1, per_page=200)
print( str( submitters.count ) + " submitters loaded into memory" )

#print list of emails
for item in submitters.items:
    print( item.email )

# get MailChimp mailing list for comparison

# for each in recent submitters list
  # check if email exists in mailing list
  # if it does not exist
    # add to email list

# wait (?)
# we could always just set up a cron job
