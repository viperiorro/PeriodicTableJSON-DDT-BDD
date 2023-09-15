import os
import json

import pandas as pd


def get_root_path():
    """Return the absolute path of the project root directory"""
    current_file_path = os.path.abspath(__file__)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD/scripts/file_utils.py
    parent_directory = os.path.dirname(current_file_path)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD/scripts
    grandparent_directory = os.path.dirname(parent_directory)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD
    return grandparent_directory


def join_paths(*args):
    """Joins paths"""
    return os.path.join(*args)


def read_json_file(json_file_name: str) -> dict:
    """Reads a json file and returns a dictionary."""
    with open(json_file_name, encoding="utf8") as jfile:
        jdata = json.load(jfile)
    return jdata


def write_json_to_csv_file(json_dict: dict, csv_file_name: str):
    """Converts a dictionary to a csv file."""
    df = pd.json_normalize(json_dict)
    df.to_csv(csv_file_name, index=False)
    print(f"CSV saved to {csv_file_name}")


def write_json_to_json_file(json_dict: dict, json_file_name: str):
    """Converts a dictionary to a json file."""
    with open(json_file_name, 'w', encoding="utf8") as f:
        json.dump(json_dict, f, indent=4)


class Paths:
    ROOT = get_root_path()  # root directory of the project

    # directories
    RESOURCES = os.path.join(ROOT, "resources")
    OUTPUT = os.path.join(RESOURCES, "output")

    # files
    PERIODIC_TABLE_CSV = os.path.join(RESOURCES, "PeriodicTableCSV.csv")
    PERIODIC_TABLE_JSON = os.path.join(RESOURCES, "PeriodicTableJSON.json")
    PERIODIC_TABLE_SCHEMA = os.path.join(RESOURCES, "periodicTableJSON.schema")
    PERIODIC_TABLE_LOOKUP = os.path.join(RESOURCES, "PeriodicTableLookup.json")


if __name__ == "__main__":
    jdata = read_json_file(Paths.PERIODIC_TABLE_JSON)
    elements = jdata['elements']

    output_file_path = os.path.join(Paths.OUTPUT, "JsonToCsv.csv")
    write_json_to_csv_file(elements, output_file_path)

    output_file_path = os.path.join(Paths.OUTPUT, "JsonToJson.json")
    write_json_to_json_file(elements, output_file_path)
