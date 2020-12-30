# HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket
# constants
IP = '0.0.0.0'
PORT = 8080
SOCKET_TIMEOUT = 30




def get_file_data(filename):
    """ Get data from file """


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response

    # if resource == '':
    #     url = DEFAULT_URL
    # else:
    #     url = resource
    #
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    # if url in REDIRECTION_DICTIONARY:
    #     # TO DO: send 302 redirection response

    # # TO DO: extract requested file type from URL (html, jpg etc)
    # if filetype == 'html':
    #     http_header = # TO DO: generate proper HTTP header
    # elif filetype == 'jpg':
    #     http_header = # TO DO: generate proper jpg header
    # # TO DO: handle all other headers

    # TO DO: read the data from the file
    # data = get_file_data(filename)
    data = "C:\\Users\\User\\Documents\\עומר סייבר\\סייבר\\htttp_server_omer_jonathan_ofek\\webroot"
    split_recourse = resource.split("/")
    for split in split_recourse:
        data += "\\" + split
    http_header = "HTTP/1.1 200 ok\\r\\n"
    http_header += "Content-Length: 2652\\r\\n"
    http_header += "Content-Type: <text/html; charset=utf-8> \\r\\n"
    http_header += "\\r\\n"
    http_response = http_header + data
    client_socket.send(http_response.encode())


def validate_http_request(request):
    """ Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL """
    request_str = request.decode('utf-8')
    split_request = request_str.split(' ')
    print(split_request)
    if (split_request[0] == 'GET'):
            request_url = request_str[1].replace("/", "\\")
            x = (True, request_url)
            return x
    y = (False, None)
    return y




def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        # get client request
        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
        else:
            print('Error: Not a valid HTTP request')
            break
    print('Closing connection')
    client_socket.close()

def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)
    print("Listening for connections on port %d" % PORT)

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()




