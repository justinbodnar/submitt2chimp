# -*- coding: utf-8 -*-

from submittable_api_client.submittable_api_client import SubmittableAPIClient
from mailchimp3 import MailChimp
import mailchimp
import config as cfg

# API Client objects
SClient = SubmittableAPIClient(username=cfg.SubmittableUsername, apitoken=cfg.SubmittableAPIToken)
MCClient = MailChimp(cfg.MailChimpUsername, cfg.MailChimpAPIToken)

# get list of submitters
SubmittableResponse = SClient.submitters(page=1, per_page=200)
SubmittableList = list()
for each in SubmittableResponse.items:
	SubmittableList.append( each.email )

# get MailChimp mailing list for comparison
MailChimpListUnsplit = list()
for each in MCClient.lists.members.all(cfg.MailChimpMailingListID, get_all=True, fields="members.email_address")['members']:
	MailChimpListUnsplit.append( each )
# split MailChimpList entries and add to usable list
MailChimpList = list()
for entry in MailChimpListUnsplit:
	temp = str( entry )
	temp = temp[21:-2]
	MailChimpList.append( temp )

# print sizes of lists to stdout
print
print( str( len( MailChimpList ) ) + " subscribers loaded into memory" )
print
print( str( len( SubmittableList ) ) + " submitters loaded into memory" )

# loop through submitters and check if they are subscribed to MC list
i = 0
for submitter in SubmittableList:
	# check if email exists in mailing list
	if submitter.lower() in (subscribed.lower() for subscribed in MailChimpList):
		print( submitter + " is already subscribed." )
	else:
		print( submitter + " is not subscribed." )
		# add the email, increment counter
		MCClientv2 = mailchimp.Mailchimp(cfg.MailChimpAPIToken)
		MCClientv2.lists.subscribe(cfg.MailChimpMailingListID, {'email': submitter})
		i = i + 1

# print report to stdout
print
print( str(i) + " new subscribers loaded into MailChimp mailing list." )
