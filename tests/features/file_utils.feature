Feature: File Utils
  The File Utils should be validated

  Scenario: Get root path
    Given the root path
    When I get the root path from the file utils
    Then the root path should match the expected value

  Scenario Outline: Join paths
    Given paths to join separated by coma: "<paths>"
    When I join the paths using the file utils
    Then the joined path should match the expected value: "<expected>"
    Examples:
      | paths                               | expected                            |
      | path1                               | path1                               |
      | path1,path2                         | path1\path2                         |
      | path1\path2                         | path1\path2                         |
      | path1,path2,path3                   | path1\path2\path3                   |
      | path1\path2,path3                   | path1\path2\path3                   |
      | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 | 1\2\3\4\5\6\7\8\9\10\11\12\13\14\15 |

  Scenario: Read json file
    Given a test data file "ValidJSONData.json"
    And the content of the json file
    When I read the json file using the file utils
    Then the returned json should match the expected json

  Scenario Outline: Read json file with error
    Given a test data file "<file_path>"
    When I read the json file using the file utils
    Then the error "<error>" should be raised
    Examples:
      | file_path              | error             |
      | InvalidJSONFormat.json | JSONDecodeError   |
      | InvalidPath.json       | FileNotFoundError |
