import os

import pytest
from pytest_bdd import given, parsers, then

from scripts.file_utils import get_root_path, join_paths


@pytest.fixture
def context():
    return dict()


@pytest.fixture(scope="session")
def root_path():
    return get_root_path()


@pytest.fixture(scope="session")
def test_files_dir_path(root_path):
    return join_paths(root_path, "tests", "test_files")


@pytest.fixture(scope="session")
def output_dir_path(test_files_dir_path):
    return join_paths(test_files_dir_path, "output")


@pytest.fixture(autouse=True)
def the_output_directory_is_clean(output_dir_path):
    for file_name in os.listdir(output_dir_path):
        file_path = join_paths(output_dir_path, file_name)
        os.remove(file_path)


@given(parsers.parse('a test data file "{file_path}"'), target_fixture="context")
def data_file(test_files_dir_path, file_path, context):
    data_file_path = join_paths(test_files_dir_path, file_path)
    context["data_file_path"] = data_file_path
    return context


@given(parsers.parse('the output file path of "{file_name}"'), target_fixture="context")
def output_file_path(context, output_dir_path, file_name):
    output_file_path = join_paths(output_dir_path, file_name)

    # Remove the file if it already exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    context["output_file_path"] = output_file_path
    return context


@then(parsers.parse('the error "{error}" should be raised'))
def check_json_decode_error(context, error):
    assert "error" in context
    assert error in context["error"]


@then("the file should be created")
def check_file_created(context):
    assert os.path.exists(context["output_file_path"])
