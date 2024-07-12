import os
from dotenv import load_dotenv
from dotenv import set_key, dotenv_values
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.products import Products

# Load environment variables from .env file
load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENVIRONMENT = os.getenv('PLAID_ENVIRONMENT', 'sandbox')
ENV_PATH = '.env'

# Configure Plaid client
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

# Initialize client
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# Create link token
request = LinkTokenCreateRequest(
    user=LinkTokenCreateRequestUser(
        client_user_id='unique_user_id'
    ),
    client_name='BalanceIt',
    products=[Products('auth'), Products('transactions')],
    country_codes=[CountryCode('US')],
    language='en'
)

response = client.link_token_create(request)
link_token = response['link_token']

print(f'Link token: {link_token}')

# Save the Link token to .env file without quotes
current_values = dotenv_values(ENV_PATH)
current_values['PLAID_LINK_TOKEN'] = link_token

with open(ENV_PATH, 'w') as env_file:
    for key, value in current_values.items():
        env_file.write(f"{key}={value}\n")