import tabulate
from dataclasses import dataclass

@dataclass
class Enum:
    name:           str
    values:         list[str]
    doc:            str = None

    def dump(self, table_format='html'):
        headers = ['Enum', 'Values']
        data = [
            [self.name, '']
        ]
        for value in self.values:
            data.append(['', value])

        return tabulate.tabulate(
            data,
            headers=headers,
            tablefmt=table_format,
            showindex='always'
        )