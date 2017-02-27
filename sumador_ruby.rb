require 'socket' # Provides TCPServer and TCPSocket classes

server = TCPServer.new(Socket.gethostname, 2345)
primer_sumando = true
suma = 0
loop do

  socket = server.accept

  # la primera linea
  request = socket.gets
  sumando = request.split("/")[1].split(" ")[0]
  suma = suma + sumando.to_i
  response = "HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>El primer sumando es #{sumando}</h1>" +
                    "<h2>Introduzca otro </h2>"+
                    "</body></html>" +
                    "\r\n"
 final_response = "HTTP/1.1 200 OK\r\n\r\n" +
                  "<html><body><h1>El segundo sumando es #{sumando}</h1>" +
                  "<h2> La suma total es #{suma} </h2>" +
                  "</body></html>" +
                  "\r\n"
  socket.print "HTTP/1.1 200 OK\r\n"

  # Print the actual response body
  socket.print response if primer_sumando
  socket.print final_response unless primer_sumando
  primer_sumando = false
  # Close the socket, terminating the connection
  socket.close
end
