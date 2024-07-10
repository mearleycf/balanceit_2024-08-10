import os
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser

# load env vars from .env file
from dotenv import load_dotenv
load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENVIRONMENT = os.getenv('PLAID_ENVIRONMENT', 'sandbox')

# config
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': PLAID_CLIENT_ID, 
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

# initialize client
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# create link token
request = LinkTokenCreateRequest(
    user=LinkTokenCreateRequestUser(
        client_user_id='unique_user_id'
    ),
    client_name='BalanceIt',
    products=['auth', 'transactions'],
    country_codes=['US'],
    language='en'
)

response = client.link_token_create(request)
link_token = response['link_token']

print(f'Link token: {link_token}')