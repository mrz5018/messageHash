# Message Hash Testing

## Prerequisites

- Python 3 (Python 3.4 was used for development)
- Python Requests Library
	Run the following command to install:
	>pip install requests

## Test Procedure

### Testing hashing capability

Run the following command set to test that the hashing is working properly.

> python3 MessageHash.py

Once the program is running:

- Enter the "H" option
- Enter the word "flabbergast"
- Check to make sure that the program responds with:
	> {'digest': '0c6c5dd1cc34024e51e38d7aac7075ecd7c2890dd84eb6f5e44f79f6824244e9'}


### Testing lookup capability

Run the following command set to test that the hashing is working properly.

> python3 MessageHash.py

Once the program is running:

- Enter the "L" option
- Enter the hash "0c6c5dd1cc34024e51e38d7aac7075ecd7c2890dd84eb6f5e44f79f6824244e9"
- Check to make sure that the program responds with:
	> {'message': 'flabbergast'}


### Testing 404 feedback

Run the following command set to test that the hashing is working properly.

> python3 MessageHash.py

Once the program is running:

- Enter the "L" option
- Enter the hash "0000000000000000000000000000000000000000000000000000000000000000"
- Check to make sure that the program responds with:
	> <Response [404]\>