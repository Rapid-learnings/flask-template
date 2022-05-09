from __future__ import print_function

import logging 
from dotenv import load_dotenv

import grpc
import flask_pb2
import flask_pb2_grpc 


load_dotenv()
print("grpc version: ", grpc.__version__)
def run():
    with grpc.insecure_channel('GRPC_SERVER_HOST') as channel:
        stub = flask_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(flask_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message) 

# for any other request/response
# def operation():
#     with grpc.insecure_channel('GRPC_SERVER_HOST') as channel: 
#         stub = flask_pb2_grpc.SERVICE



if __name__ == '__main__':
    logging.basicConfig()
    run()