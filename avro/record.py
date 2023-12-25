from .field import Field
from dataclasses import dataclass
import tabulate

@dataclass
class Record:
    name:   str
    fields: list[Field]
    doc:    str = None

    def dump(self):
        headers = ['Table', 'Field', 'Type', 'Required', 'Doc']
        table_data = [
            [self.name, '', '', '', '']
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
            tablefmt='simple_grid',
            showindex='always'
        )