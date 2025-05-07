#py_streaming.py
#-------------------------
#author:asytrick
#website:github.com/ssmool
#e-mail:eusmool@gmail.com
#-------------------------

import socket
from app_program import py_blob

def start_pytv_server(data, localhost, port):
	HOST, PORT = localhost, port
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((HOST, PORT))
	server_socket.listen(1)
	print(f'Serving HTTP on {HOST} port {PORT} ...')
	while True:
		client_connection, client_address = server_socket.accept()
		request_data = client_connection.recv(1024)
		print(request_data.decode('utf-8'))
		globaladdr(request_data)
		http_response = stream_to_blob(stream_path)
		client_connection.sendall(http_response.encode('utf-8'))
		client_connection.close()

def globaladrr(request_data):
	first_line = request_str.split('\r\n')[0]
	path_query = first_line.split(" ")[1]
	if '?' in path_query:
		query_string = path_query.split('?')[1]
	else:
		query_string = ""
	return query_string