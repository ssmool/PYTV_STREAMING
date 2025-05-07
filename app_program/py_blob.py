#py_blob.py
#-------------------------
#author:asytrick
#website:github.com/ssmool
#e-mail:eusmool@gmail.com
#-------------------------
import base64
import os

localdb = '/endpoint/'

def stream_to_blob(stream_path):
	stream_path = find_endpoint('stream_path')
	with open(stream_path, "rb") as stream_file:
		stream = base64.b64encode(stream_file.read()).decode('utf-8')
	return stream

def find_endpoint(endpoint):
	keyword = endopoint.split('?')
	col = [fx for fx os.listdir('.{localdb}') if os.path.isfile(fx)]
	for fx in col:
		for temp in keyword:
			if(in_(fx,temp)):
				return fx
				break
	return None

def in_(query, endpoint):
	return query in endpoint