import yaml

def get_data(datafile='sample.yaml'):
  with open(datafile) as file:
    obj = yaml.safe_load(file)

  return obj
