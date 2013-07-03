# -*- coding: utf-8 -*- 
import sys
from django.http import HttpResponse
from django.utils import simplejson
import collections
import os
import datetime
from parser import parse
import jsonpickle
from operator import itemgetter


JSON_MIMETYPE="application/json"



def version(request):

	data = {'name': 'RBPICameraRest',
		'version' : '0.1'}

	return HttpResponse(simplejson.dumps(data), JSON_MIMETYPE)


def get_parameters (request):
	
	commands = parse()
	#d = collections.defaultdict()
	#for k in commands.keys():
	#	d[k] = commands[k]

	l = commands.values()
	l.sort(key=lambda x: x.cid)

	return HttpResponse(jsonpickle.encode(l), JSON_MIMETYPE)
	 

