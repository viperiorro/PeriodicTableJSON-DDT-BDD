from pytest_bdd import given, when, then, scenarios, parsers

from scripts.file_utils import join_paths
from scripts.validate_json import validate_json_data


scenarios('json_validation.feature')


@given(parsers.parse('a JSON schema file "{schema_file_path}"'), target_fixture="context")
def json_schema_file_path(context, test_files_dir_path, schema_file_path):
    schema_file_path_path = join_paths(test_files_dir_path, schema_file_path)
    context["schema_file_path"] = schema_file_path_path
    return context


@when("the JSON data is validated against the schema", target_fixture="context")
def validate_json_data_in_context(context):
    json_data_file = context["data_file_path"]
    schema_file_path = context["schema_file_path"]

    try:
        validate_json_data(json_data_file, schema_file_path)
    except Exception as e:
        context["error"] = f"{type(e).__name__}: {e}"

    return context


@then("the validation passes without errors")
def check_no_errors(context):
    assert "error" not in context


@then("the validation raises an error")
def check_error_raised(context):
    assert "error" in context