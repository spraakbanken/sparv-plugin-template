"""Example for a custom annotator."""

from sparv.api import Annotation, Output, annotator


@annotator("Convert every word to uppercase")
def uppercase(word: Annotation = Annotation("<token:word>"),
              out: Output = Output("<token>:uppercase.upper"),
              # some_config_variable: str = Config("uppercase.some_setting")
              ):
    """Convert to uppercase."""
    out.write([val.upper() for val in word.read()])
