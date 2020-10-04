import grpc
from grpc_requests import Client

from ..typed import TupleMsg
__DEFAULT_ENDPOINT = 'konlpy.whatilearened.today:443'
__SSL = True
__ENDPOINT: str = __DEFAULT_ENDPOINT
__COMPRESSION = grpc.Compression.Gzip


def set_endpoint(endpoint: str,ssl=None,compression:grpc.Compression=grpc.Compression.Gzip):
    global __ENDPOINT,__SSL
    __ENDPOINT = endpoint
    __COMPRESSION = compression
    if ssl is not None:
        __SSL = ssl

def get_service(service_name: str):
    return Client.get_by_endpoint(__ENDPOINT,ssl=__SSL,compression=__COMPRESSION).service(service_name)


def make_request(phrase: str, options=None):
    return {
        "payload": phrase,
        "options": options
    }


def make_tuple(tuple_msg: TupleMsg):
    return (tuple_msg['keyword'], tuple_msg.get('tag'))


def make_join_able_return(results, options=None):
    options = options or {}
    if options.get('join'):
        return [t['keyword'] for t in results]
    return [make_tuple(t) for t in results]


def make_double_list_tuple_return(results):
    return [
        [
            [
                make_tuple(tuple_msg) for tuple_msg in sub_group.get('results',[])
             ] for sub_group in group.get('results', [])
        ] for group in results
    ]


class KonlpyClient:
    service_name: str = None

    def __init__(self):
        self._service = get_service(self.service_name)
