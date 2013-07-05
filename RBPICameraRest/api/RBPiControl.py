#!/usr/bin/env python

#  Copyright (C) 2013
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/.
#
#  Authors : Roberto Calvo <rocapal at gmail dot com>


from subprocess import call
import StringIO
from json import JSONEncoder
from django.utils import simplejson

IMAGE_FILE_PATH = "/tmp/image.jpg"
RBPI_PHOTO_COMMAND = "raspistill"

disable_args = ['none','false', 'off']

def snap_photo (args_list):

	args = "--output " + IMAGE_FILE_PATH + " "

	if "timeout" is not args_list:
		args = args + "--timeout 0 "


	for arg in args_list:
		if (arg["argument"] == "true"):
			args = args + "--" + arg["name"] + " "
			continue
		if (arg["argument"] in disable_args):
			continue
			
		args = args + "--" + arg["name"] + " " + arg["argument"] + " "


	command = RBPI_PHOTO_COMMAND + " " + args
	print command

	return_code = call(command, shell=True);
	if (return_code == 0):
		return IMAGE_FILE_PATH
	else:
		return None
