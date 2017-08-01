import requests

# This is the URL of the AWS server
url = 'http://34.210.111.55/messages/'

# Clear the screen up a little
print("\n\n\n\n")

# Choose if the program is hashing a word or doing a lookup
choice = input("Hash a word [H] or Look up a hash [L]? ")

# If "H" was entered then the program will hash a word and return
# the digest.
if(choice == "H"):

	# Accept the input of a word/message to be hashed
	message = input("Enter a word to Hash: ")

	# Setup the payload JSON
	payload = {'message' : str(message)}
	headers = {'content-type': 'application/json',
			   'Accept': 'application/json'}

	# Send the post to the server
	res = requests.post(url, json=payload, headers=headers, allow_redirects=False)
	
	# If the response found something worthwhile then print it out
	if(res.status_code == 200):
		print(res.json())
	else:
		print(res)

elif(choice == "L"):
	# Accept the input of a hash.  No error checking is necessary, because it will
	# just 404 if the request is bad.
	hash = input("Enter a Hash to look up: ")

	# Send the get to reverse look-up the hash
	res = requests.get(url + str(hash))

	# If the response found something worthwhile then print it out
	if(res.status_code == 200):
		print(res.json())
	else:
		print(res)

