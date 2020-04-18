def wsgi_application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	body = [bytes(i + '\n') for i in environ['QUERY_STRING'].split('&')]
	return body