#! /usr/bin/python3

# from cgi import parse_qs, escape
from urllib.parse import parse_qs

def myapp(environ, start_response):
    data = ''
    p_data = parse_qs(environ['QUERY_STRING'])
    for i in p_data:
        data += str(i) + "=" + str(p_data[i]) + "\n"
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(data)))]
    start_response(status, response_headers)
    return [ data ]