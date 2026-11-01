from ._anvil_designer import IntroductionTemplate
from anvil import open_form


class Introduction(IntroductionTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

  def contents_click(self, **event_args):
    open_form("Documentation")
