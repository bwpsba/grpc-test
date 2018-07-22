import sys
import grpc

import oursystem_pb2
import oursystem_pb2_grpc

options = [('grpc.max_send_message_length', 1024 * 1024 * 20), ('grpc.max_receive_message_length', 1024 * 1024 * 20)]

channel = grpc.insecure_channel('localhost:53051', options=options)

stub = oursystem_pb2_grpc.OurSystemStub(channel)

number = oursystem_pb2.DataInput(data=int(sys.argv[1]))

response = stub.OurFunction(number)

print(response.data)
