# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ws.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08ws.proto\x12\x02ws\"\xe3\x01\n\x07NewTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0csource_image\x18\x02 \x01(\t\x12\x1b\n\x13source_image_bearer\x18\t \x01(\t\x12\x17\n\x0ftarget_language\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x04 \x01(\t\x12\x11\n\tdirection\x18\x05 \x01(\t\x12\x12\n\ntranslator\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\t\x12\x18\n\x10translation_mask\x18\x08 \x01(\t\x12\x1f\n\x17translation_mask_bearer\x18\n \x01(\t\"$\n\x06Status\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"G\n\nFinishTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x1c\n\x14has_translation_mask\x18\x03 \x01(\x08\"\x83\x01\n\x10WebSocketMessage\x12\x1f\n\x08new_task\x18\x01 \x01(\x0b\x32\x0b.ws.NewTaskH\x00\x12\x1c\n\x06status\x18\x02 \x01(\x0b\x32\n.ws.StatusH\x00\x12%\n\x0b\x66inish_task\x18\x03 \x01(\x0b\x32\x0e.ws.FinishTaskH\x00\x42\t\n\x07messageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ws_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_NEWTASK']._serialized_start=17
  _globals['_NEWTASK']._serialized_end=244
  _globals['_STATUS']._serialized_start=246
  _globals['_STATUS']._serialized_end=282
  _globals['_FINISHTASK']._serialized_start=284
  _globals['_FINISHTASK']._serialized_end=355
  _globals['_WEBSOCKETMESSAGE']._serialized_start=358
  _globals['_WEBSOCKETMESSAGE']._serialized_end=489
# @@protoc_insertion_point(module_scope)