const WebSocket = require("ws");

const server = new WebSocket.Server({port:8080});

server.on("connection", (ws) => {
   console.log("New client connected !");

   //send welcome message
   ws.send("Hello this is welcome message");

   //reply
   ws.on("message", (message) => {
      console.log(message);

      //message handling
      if(message == "hi"){
         ws.send("hello");
      }else if(message == "bye"){
         ws.send("goodbye");
      }else{
         ws.send("other message");
      }
   });
});