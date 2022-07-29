"""cli"""

import os
import click

import json
from typing import Sequence

@click.command()
@click.argument('benchmark', type=click.File(mode="r"), default='-')
def main(benchmark):
    """Read tile."""
    benchmark = json.loads(benchmark.read())

    output = []
    for key, value in benchmark.items():
        if isinstance(value, Sequence):
            if key.startswith("sort_"):
                for v in value:
                    output.append(
                        {
                            "name": v["sort"],
                            "value": v["duration"],
                            "unit": "Second",
                        }
                    )
            else:
                continue

        else:
            output.append(
                {
                    "name": key,
                    "value": value,
                    "unit": "Second",
                }
            )

    click.echo(json.dumps(output))


if __name__ == '__main__':
    main()
