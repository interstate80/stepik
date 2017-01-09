#! /usr/bin/python3

from cgi import parse_qs, escape

def myapp(environ, start_response):
    data = ''
    p_data = parse_qs(environ['QUERY_STRING'])
    b_data = p_data.get('b', [''])[0]
    a_data = p_data.get('a', [])
    for aa in a_data:
        data = data + 'a=' + aa + '\n'
    data = data + 'b=' + b_data + '\n'
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(data)))]
    start_response(status, response_headers)
    return [ data ]