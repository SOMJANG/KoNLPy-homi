# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: konlpy_homi/api/v0alpha/kkma.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from konlpy_homi.api.v0alpha import global_pb2 as konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='konlpy_homi/api/v0alpha/kkma.proto',
  package='konlpy_homi.api.v0alpha',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"konlpy_homi/api/v0alpha/kkma.proto\x12\x17konlpy_homi.api.v0alpha\x1a$konlpy_homi/api/v0alpha/global.proto2\x84\x03\n\x04Kkma\x12Z\n\x03Pos\x12&.konlpy_homi.api.v0alpha.StringRequest\x1a+.konlpy_homi.api.v0alpha.TupleArrayResponse\x12]\n\x05Nouns\x12&.konlpy_homi.api.v0alpha.StringRequest\x1a,.konlpy_homi.api.v0alpha.StringArrayResponse\x12^\n\x06Morphs\x12&.konlpy_homi.api.v0alpha.StringRequest\x1a,.konlpy_homi.api.v0alpha.StringArrayResponse\x12\x61\n\tSentences\x12&.konlpy_homi.api.v0alpha.StringRequest\x1a,.konlpy_homi.api.v0alpha.StringArrayResponseb\x06proto3'
  ,
  dependencies=[konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_KKMA = _descriptor.ServiceDescriptor(
  name='Kkma',
  full_name='konlpy_homi.api.v0alpha.Kkma',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=490,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pos',
    full_name='konlpy_homi.api.v0alpha.Kkma.Pos',
    index=0,
    containing_service=None,
    input_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGREQUEST,
    output_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._TUPLEARRAYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Nouns',
    full_name='konlpy_homi.api.v0alpha.Kkma.Nouns',
    index=1,
    containing_service=None,
    input_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGREQUEST,
    output_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGARRAYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Morphs',
    full_name='konlpy_homi.api.v0alpha.Kkma.Morphs',
    index=2,
    containing_service=None,
    input_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGREQUEST,
    output_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGARRAYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Sentences',
    full_name='konlpy_homi.api.v0alpha.Kkma.Sentences',
    index=3,
    containing_service=None,
    input_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGREQUEST,
    output_type=konlpy__homi_dot_api_dot_v0alpha_dot_global__pb2._STRINGARRAYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KKMA)

DESCRIPTOR.services_by_name['Kkma'] = _KKMA

# @@protoc_insertion_point(module_scope)
