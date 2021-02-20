// recieve.js by Dorcas Lanyero
// Listens for messages on an endpoint and prints the messages to the console

var zmq = require('zeromq'),
    endpoint = zmq.socket('sub');

//try connection
try {
    endpoint.connect("tcp://127.0.0.1:5000");
    endpoint.subscribe('All');
} catch(err){
    console.log("Connection error")
}

console.log("Connected and listening for messages on port 5000");

//recieve and print to console
endpoint.on("message", function (topic, messagedata) {
    console.log('TOPIC: ', topic.toString())
    console.log( 'DATA: ', messagedata.toString())

});










