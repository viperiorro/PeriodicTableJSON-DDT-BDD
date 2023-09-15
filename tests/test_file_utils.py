import json

from pytest_bdd import given, when, then, scenarios, parsers
import os

from scripts.file_utils import join_paths, read_json_file, write_json_to_csv_file, write_json_to_json_file, \
    get_root_path

scenarios('file_utils.feature')


@given("the root path", target_fixture="context")
def expected_root_path(context):
    current_file_path = os.path.abspath(__file__)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD/tests/test_file_utils.py
    parent_directory = os.path.dirname(current_file_path)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD/tests
    grandparent_directory = os.path.dirname(parent_directory)  # e.g. C:/GitHub/PeriodicTableJSON-DDT-BDD
    context["expected_root_path"] = grandparent_directory
    return context


@given(parsers.parse('paths to join separated by coma: "{paths}"'), target_fixture="context")
def paths_to_join(paths, context):
    context["paths_to_join"] = paths.split(",")
    return context


@given("the content of the json file", target_fixture="context")
def json_file_content(context):
    json_file_path = context["data_file_path"]

    with open(json_file_path, "r") as json_file:
        context["json_file_content"] = json.load(json_file)

    return context


@when("I get the root path from the file utils", target_fixture="context")
def get_root_path_from_file_utils(context):
    context["actual_root_path"] = get_root_path()
    return context


@when("I join the paths using the file utils", target_fixture="context")
def join_paths_using_file_utils(context):
    paths_to_join = context["paths_to_join"]
    context["actual_joined_path"] = join_paths(*paths_to_join)
    return context


@when("I read the json file using the file utils", target_fixture="context")
def read_json_file_using_file_utils(context):
    json_file_path = context["data_file_path"]

    try:
        context["actual_json_file_content"] = read_json_file(json_file_path)
    except Exception as e:
        context["error"] = f"{type(e).__name__}: {e}"

    return context


@when(parsers.parse('I write the json to the csv file using the file utils'), target_fixture="context")
def write_json_to_csv_file_using_file_utils(context, output_dir_path):
    input_json_file_content = context["json_file_content"]
    output_csv_file_path = context["output_file_path"]

    try:
        write_json_to_csv_file(input_json_file_content, output_csv_file_path)
    except Exception as e:
        context["error"] = f"{type(e).__name__}: {e}"

    return context


@when(parsers.parse('I write the json to the json file using the file utils'), target_fixture="context")
def write_json_to_json_file_using_file_utils(context, output_dir_path):
    input_json_file_content = context["json_file_content"]
    output_json_file_path = context["output_file_path"]

    try:
        write_json_to_json_file(input_json_file_content, output_json_file_path)
    except Exception as e:
        context["error"] = f"{type(e).__name__}: {e}"

    return context


@then("the root path should match the expected value")
def check_root_path(context):
    expected_root_path = context["expected_root_path"]
    actual_root_path = context["actual_root_path"]
    assert actual_root_path == expected_root_path


@then(parsers.parse('the joined path should match the expected value: "{expected}"'))
def check_joined_path(context, expected):
    actual_joined_path = context["actual_joined_path"]
    assert actual_joined_path == expected


@then("the returned json should match the expected json")
def check_json_file_content(context):
    expected_json_file_content = context["json_file_content"]
    actual_json_file_content = context["actual_json_file_content"]
    assert actual_json_file_content == expected_json_file_content


@then(parsers.parse('the file should be created at "{file_path}"'))
def check_file_created(context, file_path):
    assert os.path.exists(file_path)
