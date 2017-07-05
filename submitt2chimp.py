# -*- coding: utf-8 -*-


from submittable_api_client.submittable_api_client import SubmittableAPIClient
from mailchimp3 import MailChimp
import config as cfg

# API information

SClient = SubmittableAPIClient(username=cfg.SubmittableUsername, apitoken=cfg.SubmittableAPIToken)
MCClient = MailChimp(cfg.MailChimpUsername, cfg.MailChimpAPIToken)


# get list of submitters
SubmittableList = SClient.submitters(page=1, per_page=200)
print( str( SubmittableList.count ) + " submitters loaded into memory" )

#for item in submitters.items:
#    print( item.email )

# get MailChimp mailing list for comparison
MailChimpList = list()
for each in MCClient.lists.members.all(cfg.MailChimpMailingListID, get_all=True, fields="members.email_address")['members']:
	MailChimpList.append( each )
print( str( len( MailChimpList ) ) + " subscribers loaded into memory" )

# for each in recent submitters list
  # check if email exists in mailing list
  # if it does not exist
    # add to email list

# wait (?)
