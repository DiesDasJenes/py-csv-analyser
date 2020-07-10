
from py_csv_analyser.cli import main

class MockedSystemInterface:
  @staticmethod
  def read_csv_to_dict(filepath):
    return "Fun"

def test_main():
    assert main([]) == 0
