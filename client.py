import sys
import grpc

import oursystem_pb2
import oursystem_pb2_grpc

channel = grpc.insecure_channel('localhost:53051')

stub = oursystem_pb2_grpc.OurSystemStub(channel)

number = oursystem_pb2.DataInput(data=int(sys.argv[1]))

response = stub.OurFunction(number)

print(response.data)
