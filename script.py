# pip install tgtg

from tgtg import TgtgClient
your_email: str = "mail@example.org"
client = TgtgClient(email=your_email)
credentials = client.get_credentials()

# ------------------------------------

# after successful login with the email
print(credentials)
