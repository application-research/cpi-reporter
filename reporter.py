import os,sys
import requests
import yaml

# Static settings
gitea_url = "https://git.estuary.tech"
gitea_org = "fws-customers"

# Load Gitea API key from local file ~/.gitea_api_key
with open(os.path.expanduser('~/.gitea_api_key'), 'r') as f:
    gitea_api_key = f.read().strip()

# Get the list of repos from Git
try:
    list_of_repos = requests.get(gitea_url + "/api/v1/orgs/" + gitea_org + "/repos", headers={"Authorization": "token " + gitea_api_key}).json()
except:
    print("Error getting list of repos from Gitea")
    sys.exit(1)

customers_list = []

# For each repo, get the raw Kubernetes header file from Git
for customer in list_of_repos:
    # Print the customer's name
    customer_name = customer['name']
    customer_updated_at = customer['updated_at']
    customer_created_at = customer['created_at']
    # Get the customer's raw Helm values from Git
    try:
        customer_details = requests.get(gitea_url + "/api/v1/repos/" + gitea_org + "/" + customer_name + "/raw/kubernetes%2Fvalues.yaml", headers={"Authorization": "token " + gitea_api_key}).text
        # Load from YAML
        customer_details = yaml.load(customer_details, Loader=yaml.SafeLoader)
    except:
        print("Error fetching customer details from Gitea")
        sys.exit(1)

    # What products does the customer have?
    customer_products = customer_details['global']['products']
    # What wallet address is the customer using?
    customer_wallet_address = customer_details['global']['customer']['walletAddress']
    customer_wallet_name = customer_details['global']['customer']['walletName']

    # Prepare a dict for the customer
    customer_dict = {}
    customer_dict['name'] = customer_name
    customer_dict['updated_at'] = customer_updated_at
    customer_dict['created_at'] = customer_created_at
    customer_dict['products'] = customer_products
    customer_dict['wallet_address'] = customer_wallet_address
    customer_dict['wallet_name'] = customer_wallet_name

    # Add our customer to the customers list
    customers_list.append(customer_dict)

# Print the complete list of customers
print(customers_list)

# Write to file
