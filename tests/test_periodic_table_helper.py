import os

from pytest_bdd import given, when, then, scenarios, parsers, scenario

from scripts.file_utils import join_paths
from scripts.periodic_table_helper import PeriodicTableHelper

feature = 'periodic_table_helper.feature'


@scenario(feature, 'Periodic Table with 1 property to JSON')
def test_periodic_table_with_1_property_to_json():
    pass


@scenario(feature, 'Periodic Table with 1 property to CSV')
def test_periodic_table_with_1_property_to_csv():
    pass


@scenario(feature, 'Periodic Table with properties to JSON')
def test_periodic_table_with_properties_to_json():
    pass


@given("the periodic table helper", target_fixture='context')
def the_periodic_table_helper(context):
    helper = PeriodicTableHelper()
    context["helper"] = helper
    return context


@given(parsers.parse('a property named "{property_name}"'), target_fixture='context')
def a_property_named(context, property_name):
    context["properties"] = [property_name]
    return context


@given(parsers.parse('properties separated by coma: "{properties}"'), target_fixture='context')
def properties(context, properties):
    context["properties"] = properties.split(',')
    return context


@when(parsers.parse('I extract the periodic table to a file with "{extension}" extension'), target_fixture='context')
def i_extract_the_periodic_table_to_file_with_extension(context, output_dir_path, extension):
    helper = context["helper"]
    properties = context["properties"]
    output_file_name = f"{'_'.join(properties)}.{extension}"

    output_file_path = join_paths(output_dir_path, output_file_name)

    helper.extract_data(properties, output_file_path)

    context["output_file_path"] = output_file_path
    context["extension"] = extension
    return context


@then("the file with periodic table match the expected file")
def the_file_with_periodic_table_match_the_expected_file(context, test_files_dir_path):
    properties = context["properties"]
    extension = context["extension"]

    expected_file_path = join_paths(test_files_dir_path, "periodic_table_properties", extension, f"{'_'.join(properties)}.{extension}")
    actual_file_path = context["output_file_path"]

    with open(expected_file_path, "r", encoding="utf8") as expected_file:
        expected_file_content = expected_file.read()

    with open(actual_file_path, "r", encoding="utf8") as actual_file:
        actual_file_content = actual_file.read()

    assert actual_file_content == expected_file_content