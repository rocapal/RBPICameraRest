# -*- coding: utf-8 -*- 
import os
import sys
import datetime
import collections
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from parser import parse
import jsonpickle
from operator import itemgetter

from django.core.servers.basehttp import FileWrapper
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from RBPiControl import *

JSON_MIMETYPE="application/json"



def version(request):

	data = {'name': 'RBPICameraRest',
		'version' : '0.1'}

	return HttpResponse(simplejson.dumps(data), JSON_MIMETYPE)


def get_parameters (request):
	
	commands = parse()

	l = commands.values()
	l.sort(key=lambda x: x.cid)

	return HttpResponse(jsonpickle.encode(l), JSON_MIMETYPE)


@csrf_exempt  
def photo_shot (request):

	if request.method == 'POST':
		json_data = simplejson.loads(request.raw_post_data)

		image_path = snap_photo (json_data)

		if (image_path == None):
			return HttpResponseServerError()


		image_file = open (image_path)

		response = HttpResponse(FileWrapper(image_file), content_type='image/jpeg')
		response['Content-Disposition'] = 'attachment; filename=image.jpg'

		return response

	else:
		data = { 'msg' : 'Just allowed POST petition' }
		return HttpResponse(simplejson.dumps(data), JSON_MIMETYPE)
