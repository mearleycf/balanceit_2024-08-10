import plaid
from plaid.api import plaid_api

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': 'foo',
        'secret': 'bar'
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)