function connectPyTV(host, port, endpoint)
{
	var addr = host + ':' + port + '/?endpoint=' + endpoint;
	$.ajax({
		url: addr, // Replace with your actual video URL
		type: 'GET',
		xhrFields: {
			responseType: 'blob' // Important: set the response type to blob
		},
		success: function(blob) {
			var video = document.getElementById('vpy');
			var url = URL.createObjectURL(blob);
			video.src = url;
		},
		error: function(error) {
			console.error('connection error [404 - 500]:', error);
		}
	});
}

function connect()
{
	var host, port, endpoint;
	host = document.getElementById('addr_host').value;
	port = document.getElementById('addr_port').value;
	endpoint = document.getElementById('addr_endpoint').value;
	connectPyTV(host, port, endpoint);
}