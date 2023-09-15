Feature: JSON data validation
  The JSON data should be validated against a schema

  Scenario Outline: Validate valid JSON data
    Given a test data file "<file_path>"
    And a JSON schema file "<schema_path>"
    When the JSON data is validated against the schema
    Then the validation passes without errors
    Examples:
      | file_path          | schema_path      |
      | ValidJSONData.json | ValidSchema.json |
      | NewJSON.json       | NewSchema.json   |

  Scenario Outline: Failed validation
    Given a test data file "<file_path>"
    And a JSON schema file "<schema_path>"
    When the JSON data is validated against the schema
    Then the error "<error>" should be raised
    Examples:
      | file_path            | schema_path        | error           |
      | ValidJSONData.json   | InvalidSchema.json | SchemaError     |
      | InvalidJSONData.json | ValidSchema.json   | ValidationError |
      | NewJSON.json         | ValidSchema.json   | ValidationError |