import os
from functools import cached_property

from scripts.file_utils import write_json_to_json_file, Paths, write_json_to_csv_file, read_json_file


class PeriodicTableHelper:

    @cached_property
    def _elements(self):
        """Returns a list of elements from the periodic table."""
        jdata = read_json_file(Paths.PERIODIC_TABLE_JSON)
        return jdata['elements']

    @cached_property
    def _valid_properties(self):
        """Returns a list of valid properties for the elements in the periodic table."""
        first_element = self._elements[0]
        keys = first_element.keys()
        return list(keys)

    def _write_output_file(self, output_file_path, elements):
        """Writes the elements to the output file."""
        output_base, extension = os.path.splitext(output_file_path)  # Split the file name and extension
        match extension.lower():
            case '.json':
                write_json_to_json_file(elements, output_file_path)
            case '.csv':
                write_json_to_csv_file(elements, output_file_path)
            case _:
                raise ValueError(f'Invalid extension: {extension}')

    def _get_needed_properties(self, properties: list):
        """Returns a dictionary of the properties needed."""
        data_needed = {}
        if properties:
            for prop in properties:
                if prop in self._valid_properties:
                    data_needed[prop] = True
                else:
                    raise ValueError(f'Property {prop} not found.')

        if not data_needed:
            raise ValueError('No properties selected.')

        return data_needed

    def _get_elements_to_write(self, properties: list):
        """Returns a list of elements to write to the output file."""
        needed_properties = self._get_needed_properties(properties)
        elements_to_write = [{key: element[key] for key in needed_properties} for element in self._elements]
        return elements_to_write

    def extract_data(self, properties: list, output_file_path: str):
        """Extracts the data from the periodic table and writes it to the output file."""
        elements_to_write = self._get_elements_to_write(properties)
        self._write_output_file(output_file_path, elements_to_write)


if __name__ == "__main__":
    # Configuration variables
    properties = ["number", "symbol", "name"]
    output = "SpecificData.json"
    extractor = PeriodicTableHelper()
    extractor.extract_data(properties, output)
