from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values


credentials = get_credentials()
neutron = client.Client(**credentials)
sg = neutron.list_security_groups()
print sg
