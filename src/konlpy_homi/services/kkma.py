from homi import Service
from konlpy.tag import Kkma

from .utils import attachThreadToJVM, check_options
from konlpy_homi.api.v0alpha  import kkma_pb2
from typed import StringArrayResponse, TupleArrayResponse

HANDLE_OPTIONS = {"flatten", "join"}


def kkma_option_checker(options: dict):
    check_options(HANDLE_OPTIONS, options)


engine = Kkma()

kkma_svc = Service(kkma_pb2._KKMA)


@kkma_svc.method()
@attachThreadToJVM
def Pos(payload: str, options: dict = None, **kwargs) -> TupleArrayResponse:
    options = options or {}
    kkma_option_checker(options)
    resp = TupleArrayResponse(options=options, results=[])
    if options.get("join", False):
        resp['results'] = [{'keyword': keyword, 'tag': None} for keyword in engine.pos(payload, **options)]
    else:
        resp['results'] = [{'keyword': keyword, 'tag': tag} for keyword, tag in engine.pos(payload, **options)]
    return resp


@kkma_svc.method()
@attachThreadToJVM
def Nouns(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.nouns(payload),
        "options": options
    }


@kkma_svc.method()
@attachThreadToJVM
def Morphs(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.morphs(payload),
        "options": options
    }

@kkma_svc.method()
@attachThreadToJVM
def Sentences(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.sentences(payload),
        "options": options
    }
