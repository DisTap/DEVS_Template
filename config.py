import yaml

with open('/instance/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config['name'])
