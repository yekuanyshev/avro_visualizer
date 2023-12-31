import json
import avro

def main():
    raw = read_json_file('models.avsc')
    table_format = 'simple_grid'

    result = ''
    for raw_schema in raw:
        if raw_schema['type'] == 'record':
            record = avro.parse_record(raw_schema)
            result += record.dump(table_format=table_format)

        if raw_schema['type'] == 'enum':
            enum = avro.parse_enum(raw_schema)
            result += enum.dump(table_format=table_format)

        result += '\n'

    with open('result.txt', 'w') as f:
        f.write(result)

def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)




if __name__ == '__main__':
    main()