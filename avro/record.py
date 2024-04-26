from .field import Field
from dataclasses import dataclass
import tabulate

@dataclass
class Record:
    name:           str
    fields:         list[Field]
    doc:            str = None

    def dump(self, table_format='html'):
        headers = ['Table', 'Field', 'Type', 'Required', 'Doc']
        table_data = [
            [self.name, '', '', '', self.doc]
        ]
        for field in self.fields:
            field_name = f'{field.name} *' if field.is_primary else field.name
            table_data.append([
                '',
                field_name,
                field.type,
                field.is_required,
                field.doc,
            ])

        return tabulate.tabulate(
            table_data,
            headers=headers,
            tablefmt=table_format,
            showindex='always'
        )