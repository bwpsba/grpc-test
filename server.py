import grpc
from concurrent import futures
import time

import oursystem_pb2
import oursystem_pb2_grpc

import oursystem


class OurSystemServicer(oursystem_pb2_grpc.OurSystemServicer):
    def OurFunction(self, request, context):
        response = oursystem_pb2.DataOutput()
        response.data = oursystem.our_function(request.data)
        return response


if __name__ == '__main__':

    options = [('grpc.max_send_message_length', 1024 * 1024 * 20), ('grpc.max_receive_message_length', 1024 * 1024 * 20)]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=options)

    oursystem_pb2_grpc.add_OurSystemServicer_to_server(OurSystemServicer(), server)

    print('Starting server. Listening on port 53051.')
    server.add_insecure_port('[::]:53051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
