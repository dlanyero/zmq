#Sender.py by Dorcas Lanyero
#Recieves string input from the console and sends it to a recipient application listening on the same socket
#Closes the socket and stops sending messages when the user enters the string "end"

import zmq
import logging
import traceback
import time


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
        endpoint.bind(url)
    except Exception as e:
        print("An error was encountered. The socket was either not successfuly created, or we could not connect to it")
        logging.error(traceback.format_exc())


    get_send_message(endpoint)

    #close the socket
    endpoint.close()
    print("The endpoint is  closed. You are no longer able to send messages")


# #Gets messages from the console and publishes them
def get_send_message(pub):
    print("Type a message and hit enter to send. Type 'end' to stop")
    try:
        while True:
            messagedata = input()
            topic = "All"
            pub.send_multipart([topic.encode(), messagedata.encode()])
            time.sleep(1)
            if messagedata == "end":
                break
    except Exception as e:
        print("An error occured while sending this message. Please try again,")
        logging.error(traceback.format_exc())


if __name__ == '__main__':
    publish()



