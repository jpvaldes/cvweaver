from jinja2 import Environment, FileSystemLoader, select_autoescape
from ruamel.yaml import YAML
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
import click


@dataclass
class BaseFormat:
    env: Environment
    template_name: str
    output_file: Path


@dataclass(kw_only=True)
class LatexFormat(BaseFormat):
    env = Environment(
        "((*",
        "*))",
        "(((",
        ")))",
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(default=True),
        trim_blocks=True,
    )
    template_name = "latex.tpl"
    output_extension = "tex"


class Format(Enum):
    latex = LatexFormat

    @classmethod
    def has(cls, name: str):
        return name in cls.__members__


def load_data(
    data_path: Path,
) -> dict[str, str | int | dict[str, str | int | list[dict[str, str]]]]:
    """Load CV data.

    Arguments
    ---------
    data_file : Path
        Path to the YAML file containing the CV data.
    Returns
    -------
    A nested dictionary with the CV data.
    """
    yaml = YAML(typ="safe")
    with open(data_path, "r") as fin:
        content = yaml.load(fin)

    return content


@click.command()
@click.option(
    "-d",
    "--data_file",
    type=str,
    default="data/cv.yaml",
    show_default=True,
    help="Path to YAML file with CV data.",
)
@click.option(
    "-t",
    "--to",
    type=str,
    default="latex",
    show_default=True,
    help="Output format. Supported values: latex.",
)
def main(data_file: str, to: str) -> None:
    data_path = Path(data_file)

    if not data_path.exists():
        raise IOError(f"Cannot find file with data {data_file}. Exiting.")
    content = load_data(data_path=data_path)

    if Format.has(to):
        cv = Format[to].value
    else:
        raise ValueError(
            f"The --to argument value {to} is not in the list of supported formats: {[f.name for f in Format]}."
        )

    template = cv.env.get_template(cv.template_name)
    render = template.render(content)
    output_file = f"{data_path.stem}.{cv.output_extension}"

    with open(output_file, "w") as output:
        output.write(render)
