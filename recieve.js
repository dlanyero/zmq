// recieve.js by Dorcas Lanyero
// Listens for messages on an endpoint and prints the messages to the console

var zmq = require("zeromq")
var sock = zmq.socket("pub")

try {
    endpoint.connect("tcp://127.0.0.1:5000");
    endpoint.subscribe("");
} catch(err){
    console.log("Connection error")
}

console.log("Connected and listening for messages on port 5000");
while(True) {
    endpoint.on("message", function (topic, message) {
        console.log(
            message
        );
    });
    if(message == "end"){
        socket.close()
    }
}








