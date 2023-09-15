"""
Validate that the JSON data is correctly formatted according
to the template in the 'schemas' directory.
"""
import jsonschema

from scripts.file_utils import Paths, read_json_file


def validate_json_data(json_data_file, schema_file):
    print(f"Validating {json_data_file} against {schema_file}")

    data = read_json_file(json_data_file)
    schema = read_json_file(schema_file)

    # Raises an exception in case of failure
    jsonschema.validate(instance=data, schema=schema)
    print("Validation passed")


if __name__ == "__main__":
    PERIODIC_TABLE_JSON = Paths.PERIODIC_TABLE_JSON
    PERIODIC_TABLE_SCHEMA = Paths.PERIODIC_TABLE_SCHEMA

    validate_json_data(PERIODIC_TABLE_JSON, PERIODIC_TABLE_SCHEMA)