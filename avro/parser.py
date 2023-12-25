from .record import Record
from .field import Field
from .enum import Enum

def parse_record(raw: dict) -> Record:
    name = raw['name']
    doc = raw.get('doc', '')

    primary_keys = []

    if 'indexes' in raw:
        for index in raw['indexes']:
            if 'name' in index and index['name'] == 'pk':
                primary_keys = index['parts']

        if len(primary_keys) == 0:
            primary_keys.append(raw['indexes'][0])

    fields = []
    for raw_field in raw['fields']:
        field_name = raw_field['name']
        if field_name == '_MVCC':
            continue

        field_type, is_nullable = parse_type(raw_field['type'])
        field_doc = raw_field.get('doc', '')
        fields.append(Field(
            name=field_name,
            type=field_type,
            is_primary=field_name in primary_keys,
            is_nullable=is_nullable,
            doc=field_doc
        ))
    return Record(
        name=name,
        fields=fields,
        doc=doc
    )

def parse_enum(raw: dict) -> Enum:
    name = raw['name']
    doc = raw.get('doc', '')
    values = raw['symbols']
    return Enum(
        name=name,
        values=values,
        doc=doc,
    )

def parse_type(_type):
    if isinstance(_type, str):
        return (_type, False)

    if isinstance(_type, list):
        is_nullable = _type[0] == 'null'
        if isinstance(_type[1], str):
            return (_type[1], is_nullable)
        if isinstance(_type[1], dict):
            if 'logicalType' in _type[1]:
                return (_type[1]['logicalType'], is_nullable)
            if 'type' in _type[1]:
                if _type[1]['type'] == 'array':
                    return ('[]' + _type[1]['items'], is_nullable)

    if isinstance(_type, dict):
        return (_type['logicalType'], False)

    return None