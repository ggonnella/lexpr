import lark
import importlib.resources
from . import error

_data = importlib.resources.files("lexpr").joinpath("data")
GrammarFilename = str(_data.joinpath("lexpr.g"))

class Parser():

  def __init__(self):
    grammar_file = open(GrammarFilename)
    self.parser = lark.Lark(grammar_file)

  def parse(self, text):
    try:
      return self.parser.parse(text)
    except lark.exceptions.UnexpectedCharacters as e:
      errmsg = f"Invalid logic expression: {e}\n"
      errmsg += f"Invalid/unexpected character: {e.char}"
      raise error.LexprParserError(errmsg)
    except lark.exceptions.UnexpectedEOF as e:
      errmsg = f"Invalid logic expression: {e}\n"
      errmsg += "Invalid/unbalanced expression"
      raise error.LexprParserError(errmsg)

  def _get_identifiers(self, tree, identifiers=None):
      if identifiers is None:
          identifiers = []
      if isinstance(tree, lark.Tree):
          for child in tree.children:
              self._get_identifiers(child, identifiers)
      elif isinstance(tree, lark.Token) and tree.type == 'IDENTIFIER':
          identifiers.append(tree.value)
      return identifiers

  def list_identifiers(self, text):
    return self._get_identifiers(self.parse(text))

