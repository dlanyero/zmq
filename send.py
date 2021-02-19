#Sender.py by Dorcas Lanyero
#Recieves string input from the console and send sends it to a recipient application listening on the same socket
#Closes the socket and stops sending messages when the user enters the string "close"

import zmq
import logging
import traceback


# #Establishes socket connection for bublishing messages.
def publish():
    #set url
    adress = "127.0.0.1"
    port = "5000"
    url = '''tcp://{}:{}'''.format(adress, port)

    cntx = zmq.Context()
    endpoint = cntx.socket(zmq.PUB)

    #try connecting to socket
    try:
        endpoint.connect(url)
    except Exception as e:
        print("An error was encountered. The socket was either not successfuly created, or we could not connect to it")
        logging.error(traceback.format_exc())


    get_send_message(endpoint)

    #close the socket
    cntx.socket.close()
    print("The endpoint is  closed. You are no longer able to send messages")


# #Gets messages from the console and publishes them
def get_send_message(pub):
    try:
        while True:
            msg = input()
            pub.send_string(msg, flags=0, copy=True, encoding='utf-8')
            if msg == "end":
                break
    except Exception as e:
        print("An error occured while sending this message. Please try again,")
        logging.error(traceback.format_exc())


if __name__ == '__main__':
    publish()



