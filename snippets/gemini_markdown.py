import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown

from google.api_core import retry

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))