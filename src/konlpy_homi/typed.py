from typing import Any, Dict, List, TypedDict


class TupleMsg(TypedDict):
    keyword: str
    tag: str


OptionsMsg=Dict


class TupleArrayResponse(TypedDict):
    results: List[TupleMsg]
    options: OptionsMsg

class ListOfTuple(TypedDict):
    results : List[TupleMsg]

class ListOfListOfTuple(TypedDict):
    results : List[ListOfTuple]


class TupleDoubleArrayResponse(TypedDict):
    results: List[ListOfListOfTuple]
    options:OptionsMsg

class StringArrayResponse(TypedDict):
    results: List[str]
    options: OptionsMsg


class StringResponse(TypedDict):
    results: str
    options: OptionsMsg


class StructMsg(TypedDict):
    result: Any


class StructResponse(TypedDict):
    result: StructMsg
    options: OptionsMsg
