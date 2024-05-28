from .field import Field
from .function import Function
from .relation import Relation
from dataclasses import dataclass
import tabulate

@dataclass
class Record:
    name:           str
    fields:         list[Field]
    functions:      list[Function]
    relations:      list[Relation]
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

        if len(self.functions) > 0:
            table_data.append([])

            table_data.append(['Functions'])
            for function in self.functions:
                table_data.append([
                    '',
                    function.name
                ])
        
        if len(self.relations) > 0:
            table_data.append([])
            
            table_data.append(['Relations', 'Field', 'Count', 'To'])
            for relation in self.relations:
                table_data.append([
                    '',
                    relation.name,
                    relation.count,
                    relation.to
                ])

        return tabulate.tabulate(
            table_data,
            headers=headers,
            tablefmt=table_format,
            showindex='always'
        )