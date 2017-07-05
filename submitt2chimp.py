# -*- coding: utf-8 -*-


from submittable_api_client.submittable_api_client import SubmittableAPIClient
from mailchimp3 import MailChimp
import config as cfg

# API information

SClient = SubmittableAPIClient(username=cfg.SubmittableUsername, apitoken=cfg.SubmittableAPIToken)
MCClient = MailChimp(cfg.MailChimpUsername, cfg.MailChimpAPIToken)


# get list of submitters
#submitters = Client.submitters(page=1, per_page=200)
#print( str( submitters.count ) + " submitters loaded into memory" )

#print list of emails
#for item in submitters.items:
#    print( item.email )

# get MailChimp mailing list for comparison

for each in MCClient.lists.members.all(cfg.MailChimpMailingListID, get_all=True, fields="members.email_address")['members']:
	print( each )

# for each in recent submitters list
  # check if email exists in mailing list
  # if it does not exist
    # add to email list

# wait (?)
