from ._anvil_designer import Machine1Template
from anvil import open_form


class Machine1(Machine1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  def docs_click(self, **event_args):
    open_form("Documentation")
