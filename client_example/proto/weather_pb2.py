# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/weather.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/weather.proto',
  package='weather',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13proto/weather.proto\x12\x07weather\"\x10\n\x0eWeatherRequest\"#\n\x0cWeatherReply\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x32L\n\x07\x43hecker\x12\x41\n\rcheck_weather\x12\x17.weather.WeatherRequest\x1a\x15.weather.WeatherReply\"\x00\x62\x06proto3')
)




_WEATHERREQUEST = _descriptor.Descriptor(
  name='WeatherRequest',
  full_name='weather.WeatherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=48,
)


_WEATHERREPLY = _descriptor.Descriptor(
  name='WeatherReply',
  full_name='weather.WeatherReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='weather.WeatherReply.temperature', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['WeatherRequest'] = _WEATHERREQUEST
DESCRIPTOR.message_types_by_name['WeatherReply'] = _WEATHERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeatherRequest = _reflection.GeneratedProtocolMessageType('WeatherRequest', (_message.Message,), dict(
  DESCRIPTOR = _WEATHERREQUEST,
  __module__ = 'proto.weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherRequest)
  ))
_sym_db.RegisterMessage(WeatherRequest)

WeatherReply = _reflection.GeneratedProtocolMessageType('WeatherReply', (_message.Message,), dict(
  DESCRIPTOR = _WEATHERREPLY,
  __module__ = 'proto.weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherReply)
  ))
_sym_db.RegisterMessage(WeatherReply)



_CHECKER = _descriptor.ServiceDescriptor(
  name='Checker',
  full_name='weather.Checker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=87,
  serialized_end=163,
  methods=[
  _descriptor.MethodDescriptor(
    name='check_weather',
    full_name='weather.Checker.check_weather',
    index=0,
    containing_service=None,
    input_type=_WEATHERREQUEST,
    output_type=_WEATHERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHECKER)

DESCRIPTOR.services_by_name['Checker'] = _CHECKER

# @@protoc_insertion_point(module_scope)