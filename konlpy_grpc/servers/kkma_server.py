import time
from concurrent import futures

import grpc
import jpype

from konlpy.tag import Kkma

from .._generated import global_pb2, kkma_pb2, kkma_pb2_grpc
from ..monkeypatch import _ORIGINAL, KEY_TAG_KKMA


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class KkmaService(kkma_pb2_grpc.KkmaServicer):
    HANDLE_OPTIONS = ("flatten", "join")

    def __init__(self):
        self.engine = _ORIGINAL[KEY_TAG_KKMA]() if KEY_TAG_KKMA in _ORIGINAL else Kkma()  # TODO: Thread-safe? Performance?

    @staticmethod
    def _check_options(options):
        result = {}
        for option in options:
            if option.key not in KkmaService.HANDLE_OPTIONS:
                raise Exception("%s option is not supported! (supported: %s)" % (option.key, ", ".join(KkmaService.HANDLE_OPTIONS)))
                # TODO: context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            else:
                result[option.key] = option.value
        return result

    def Pos(self, request, context):
        jpype.attachThreadToJVM()  # XXX: Performance Incresed. (Still don't know yet)
        options = self._check_options(request.options)
        if options.get("join", False):
            return global_pb2.TupleArrayResponse(
                results=[global_pb2.TupleArrayResponse.Tuple(keyword=keyword, tag=None) for keyword in self.engine.pos(request.payload, **options)],
                options=request.options,
            )
        return global_pb2.TupleArrayResponse(
            results=[global_pb2.TupleArrayResponse.Tuple(keyword=keyword, tag=tag) for keyword, tag in self.engine.pos(request.payload, **options)],
            options=request.options,
        )

    def Nouns(self, request, context):
        jpype.attachThreadToJVM()  # XXX: Performance Incresed. (Still don't know yet)
        return global_pb2.StringArrayResponse(results=self.engine.nouns(request.payload), options=request.options)

    def Morphs(self, request, context):
        jpype.attachThreadToJVM()  # XXX: Performance Incresed. (Still don't know yet)
        return global_pb2.StringArrayResponse(results=self.engine.morphs(request.payload), options=request.options)

    def Sentences(self, request, context):
        jpype.attachThreadToJVM()  # XXX: Performance Incresed. (Still don't know yet)
        return global_pb2.StringArrayResponse(results=self.engine.sentences(request.payload), options=request.options)


add_to_server = kkma_pb2_grpc.add_KkmaServicer_to_server


SERVICE_NAME = kkma_pb2._KKMA.full_name


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kkma_pb2_grpc.add_KkmaServicer_to_server(KkmaService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
