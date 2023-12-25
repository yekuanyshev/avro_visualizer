import json
import avro

def main():
    raw = read_json_file('models.avsc')

    result = ''
    for raw_schema in raw:
        if raw_schema['type'] == 'record':
            record = avro.parse_record(raw_schema)
            result += record.dump()

        if raw_schema['type'] == 'enum':
            enum = avro.parse_enum(raw_schema)
            result += enum.dump()

        result += '\n'

    with open('result.txt', 'w') as f:
        f.write(result)

def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)




if __name__ == '__main__':
    main()