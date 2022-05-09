from concurrent import futures
# from email import message 
import logging 
import grpc

from app.lib.grpc_helper.flask_pb2_grpc import  GreeterServicer, add_GreeterServicer_to_server
from app.lib.grpc_helper.flask_pb2 import HelloReply



class Greeter(GreeterServicer):
    def SayHello(self, request, context):
        return HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server) 
    server.add_insecure_port('[::]: GRPC_SERVER_PORT')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
