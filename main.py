import json
import avro
import typer
import sys

ignore_schemas = [
    'DictKeys',
    'DictItem',
    'FieldTrack',
    'SimpleDictValue',
    'CreditPurposeDictRecord',
    'CreditPurposeDictValue',
    'ExtraDataRecord',
    'ExternalRefMVCC',
    'ClientRoleMVCC',
    'GuarantorRecordMVCC',
    'ContractorRecordMVCC',
    'ClientRef',
    'ProductRef',
    'RestructurizationRef',
    'TransactionRef',
    'StaffRef',
    'ClientGroupRef',
    'ClientGroupIDRef',
    'BusinessAreaRef',
]

app = typer.Typer()

@app.command()
def convert(file: str = None, format: str = 'grid'):
    raw = get_schema(file)
    table_format = format

    result = ''
    for raw_schema in raw:
        if raw_schema['name'] in ignore_schemas:
            continue

        if raw_schema['type'] == 'record':
            record = avro.parse_record(raw_schema)
            result += record.dump(table_format=table_format)

        if raw_schema['type'] == 'enum':
            enum = avro.parse_enum(raw_schema)
            result += enum.dump(table_format=table_format)

        result += '\n'

    print(result)

def get_schema(schema_file: str = None) -> list[dict]:
    if schema_file is not None:
        with open(schema_file) as f:
            return json.load(f)

    content = sys.stdin.read()
    if content is None or len(content) == 0:
        raise Exception('empty schema file')

    return json.loads(content)


if __name__ == '__main__':
    app()