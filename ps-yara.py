import yara
import os

directory = '/pluralsight'
yara_rules = yara.compile(filepath='/pluralsight/yara_rules/test_rule.yar')

for filename in os.listdir(directory):
  matches = yara_rules.match(data=filename)
  if matches:
    print(filename + ": Matched, possibly infected!")
  else:
    print(filename + ": Clean")