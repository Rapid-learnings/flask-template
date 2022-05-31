from concurrent import futures
from email import message 
import logging
from flask import Blueprint  
import grpc
import flask_pb2_grpc
import flask_pb2 

class Greeter(flask_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return flask_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    flask_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
