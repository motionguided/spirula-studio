from ._anvil_designer import DocumentationTemplate
from anvil import open_form


class Documentation(DocumentationTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

  def home_click(self, **event_args):
    open_form("Machine1")

  def intro_click(self, **event_args):
    open_form("Documentation.Topics.Introduction")

  def machine_click(self, **event_args):
    open_form("Documentation.Topics.Machine1")

  def branch_click(self, **event_args):
    open_form("Documentation.Topics.ThisBranch")
