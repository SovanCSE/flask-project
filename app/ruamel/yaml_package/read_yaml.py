from ruamel.yaml import YAML
import json

def read_yaml_files():
    yaml = YAML()
    base_config = open('base_config.yaml')
    # another_config = open('inp_master_campus_fe_non_att.yaml')
    base_yaml = yaml.load(base_config)
    base_yaml_dict = dict(base_yaml.items())
    with open("data_file.json", "w") as write_file:
        json.dump(base_yaml_dict, write_file, indent=2)

    # another_yaml = yaml.load(another_config)
    # another_yaml_dict = dict(another_yaml.items())
    #
    # base_yaml_dict.update(another_yaml_dict)
    # print(base_yaml_dict['latest1']['root_path'])



if __name__ == "__main__":
    read_yaml_files()