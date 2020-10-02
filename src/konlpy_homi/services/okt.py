from homi import Service
from konlpy.tag import Okt

from .utils import attachThreadToJVM, check_options
from konlpy_homi.api.v0alpha import okt_pb2
from typed import StringArrayResponse, StringResponse, TupleArrayResponse

HANDLE_OPTIONS = {"norm", "stem", "join"}


def okt_option_checker(options: dict):
    check_options(HANDLE_OPTIONS, options)


engine = Okt()

okt_svc = Service(okt_pb2._OKT)


@okt_svc.method()
@attachThreadToJVM
def Pos(payload: str, options: dict = None, **kwargs) -> TupleArrayResponse:
    options = options or {}
    okt_option_checker(options)
    resp: TupleArrayResponse = TupleArrayResponse(options=options)
    if options.get("join", False):
        resp['results'] = [{'keyword': keyword, 'tag': None} for keyword in engine.pos(payload, **options)]
    else:
        resp['results'] = [{'keyword': keyword, 'tag': tag} for keyword, tag in engine.pos(payload, **options)]
    return resp


@okt_svc.method()
@attachThreadToJVM
def Nouns(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    options = options or {}
    return {
        "results": engine.nouns(payload),
        "options": options
    }


@okt_svc.method()
@attachThreadToJVM
def Morphs(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    options = options or {}
    return {
        "results": engine.morphs(payload, **options),
        "options": options
    }


@okt_svc.method()
@attachThreadToJVM
def Phrases(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.phrases(payload),
        "options": options
    }


@okt_svc.method()
@attachThreadToJVM
def Normalize(payload: str, options: dict = None, **kwargs) -> StringResponse:
    print(payload)
    return {
        "results": engine.normalize(payload),
        "options": options
    }
