import sys

from loguru import logger
from loguru._colorizer import Colorizer


def formatter(record: dict):
    """
    Formats the logging message by:

    - Adding color and bold
    - Indenting the message
    """

    base_format = (
        "<b>"  # bold
        "<light-blue>[eds-scikit]</light-blue>"
        "- "
        "{name}:"  # corresponds to __name__
        "{extra[classname]}{extra[sep]}"  # class name, if relevant
        "</b>"
        "{function}"  # function name
    )
    colored_format = Colorizer.ansify(base_format)
    colored_message = Colorizer.ansify(str(record["message"]))

    escaped_record = escape(record)
    base = colored_format.format(**escaped_record)

    lines = colored_message.splitlines()
    new_message = "".join("\n   " + line for line in lines) + "\n"

    return base + new_message


logger.remove(0)
logger.add(sys.stdout, format=formatter, colorize=False)

# Default logging: no classname, and consequently
# no separator between classname and function name
logger.configure(extra={"classname": "", "sep": ""})


def escape(record: dict):
    """
    Escape the "<" character before markup parsing
    """
    return {
        k: v if not isinstance(v, str) else v.replace("<", r"\<")
        for k, v in record.items()
    }
