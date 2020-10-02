from homi import Service
from konlpy.tag import Hannanum

from .utils import attachThreadToJVM, check_options
from konlpy_homi.api.v0alpha import hannanum_pb2
from typed import StringArrayResponse, TupleDoubleArrayResponse, TupleArrayResponse

HANDLE_OPTIONS = {"ntags", "flatten", "join"}


def hannanum_option_checker(options: dict):
    check_options(HANDLE_OPTIONS, options)


engine = Hannanum()

hannanum_svc = Service(hannanum_pb2._HANNANUM)


@hannanum_svc.method()
@attachThreadToJVM
def Pos(payload: str, options: dict = None, **kwargs) -> TupleArrayResponse:
    options = options or {}
    hannanum_option_checker(options)
    resp = TupleArrayResponse(options=options, results=[])
    if options.get("join", False):
        resp['results'] = [{'keyword': keyword, 'tag': None} for keyword in engine.pos(payload, **options)]
    else:
        resp['results'] = [{'keyword': keyword, 'tag': tag} for keyword, tag in engine.pos(payload, **options)]
    return resp


@hannanum_svc.method()
@attachThreadToJVM
def Nouns(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.nouns(payload),
        "options": options
    }


@hannanum_svc.method()
@attachThreadToJVM
def Morphs(payload: str, options: dict = None, **kwargs) -> StringArrayResponse:
    return {
        "results": engine.morphs(payload),
        "options": options
    }


@hannanum_svc.method()
@attachThreadToJVM
def Analyze(payload: str, options: dict = None, **kwargs) -> TupleDoubleArrayResponse:
    results = [
        { "results":[ {"results":[{'keyword': keyword, 'tag': tag} for keyword, tag in sub_group]} for sub_group in group]} for group in engine.analyze(payload)

    ]
    return {
        "results":results,
        "options": options
    }
