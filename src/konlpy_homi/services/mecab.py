from homi import Service
from konlpy.tag import Mecab

from .utils import attachThreadToJVM, check_options
from konlpy_homi.api.v0alpha import mecab_pb2
from typed import StringArrayResponse, TupleArrayResponse

HANDLE_OPTIONS = {"flatten", "join"}


def mecab_option_checker(options: dict):
    check_options(HANDLE_OPTIONS, options)


engine = Mecab()

mecab_svc = Service(mecab_pb2._MECAB)


@mecab_svc.method()
@attachThreadToJVM
def Pos(payload: str, options: dict = None, **kwargs) -> TupleArrayResponse:
    options = options or {}
    mecab_option_checker(options)
    resp = TupleArrayResponse(options=options, results=[])
    if options.get("join", False):
        resp['results'] = [{'keyword': keyword, 'tag': None} for keyword in engine.pos(payload, **options)]
    else:
        resp['results'] = [{'keyword': keyword, 'tag': tag} for keyword, tag in engine.pos(payload, **options)]
    return resp


@mecab_svc.method()
@attachThreadToJVM
def Nouns(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.nouns(payload),
        "options": options
    }


@mecab_svc.method()
@attachThreadToJVM
def Morphs(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.morphs(payload),
        "options": options
    }
