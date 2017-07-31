from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from messageHandler.models import MessageHash
import hashlib
import json


@csrf_exempt 
def index(request):
	if (request.method == "POST"):
		response = handlePost(request)
		return response
	elif(request.method == "GET"):
		response = handleGet(request)
		return response
	else:
		raise Http404("HTTP Error")


def handlePost(request):
	#process the post 
	body = json.loads(request.body)
	message = body.get("message").encode('utf-8')

	#set up the hasher object and hash tehe message using SHA-256
	hasher = hashlib.sha256()
	hasher.update(message)
	messageHash = hasher.hexdigest()

	#Save the data to the database
	m, created = MessageHash.objects.get_or_create(message=message, hash=messageHash)
	if(created==True):
		m.save()

	#create the message to return
	data = {
		'digest': messageHash
	}
	response = JsonResponse(data)

	return response

def handleGet(request):
	path = request.get_full_path()

	#This is a brute force way of doing this, but don't really
	#need anything too smart.  Just pulling the last 64 chars
	#from the URL. which should be the hash
	length = len(path)
	inputHash = path[length-64:length]

	# find the object if it exists
	if(MessageHash.objects.filter(hash=inputHash).exists()):
		m = MessageHash.objects.get(hash=inputHash)

		#create the message to return
		data = {
			'message': m.message
		}
		response = JsonResponse(data)
		return response

	else:
		#The message was never hashed, so return a default message.
		#create the message to return
		raise Http404("Hash does not exist in the database!")


