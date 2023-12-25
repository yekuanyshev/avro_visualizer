import tabulate
from dataclasses import dataclass

@dataclass
class Enum:
    name:   str
    values: list[str]
    doc:    str = None

    def dump(self):
        headers = ['Enum', 'Values']
        data = [
            [self.name, '']
        ]
        for value in self.values:
            data.append(['', value])

        return tabulate.tabulate(
            data,
            headers=headers,
            tablefmt='simple_grid',
            showindex='always'
        )