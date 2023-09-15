Feature: Periodic Table Helper

  Background:
    Given the periodic table helper

  Scenario Outline: Periodic Table with 1 property to JSON
    Given a property named "<property_name>"
    When I extract the periodic table to a file with "json" extension
    Then the file should be created
    And the file with periodic table match the expected file
    Examples:
      | property_name                   |
      | name                            |
      | appearance                      |
      | atomic_mass                     |
      | boil                            |
      | category                        |
      | density                         |
      | discovered_by                   |
      | melt                            |
      | molar_heat                      |
      | named_by                        |
      | number                          |
      | period                          |
      | group                           |
      | phase                           |
      | source                          |
      | bohr_model_image                |
      | bohr_model_3d                   |
      | spectral_img                    |
      | summary                         |
      | symbol                          |
      | xpos                            |
      | ypos                            |
      | wxpos                           |
      | wypos                           |
      | shells                          |
      | electron_configuration          |
      | electron_configuration_semantic |
      | electron_affinity               |
      | electronegativity_pauling       |
      | ionization_energies             |
      | cpk-hex                         |
      | image                           |
      | block                           |

  Scenario Outline: Periodic Table with 1 property to CSV
    Given a property named "<property_name>"
    When I extract the periodic table to a file with "csv" extension
    Then the file should be created
    And the file with periodic table match the expected file
    Examples:
      | property_name                   |
      | name                            |
      | appearance                      |
      | atomic_mass                     |
      | boil                            |
      | category                        |
      | density                         |
      | discovered_by                   |
      | melt                            |
      | molar_heat                      |
      | named_by                        |
      | number                          |
      | period                          |
      | group                           |
      | phase                           |
      | source                          |
      | bohr_model_image                |
      | bohr_model_3d                   |
      | spectral_img                    |
      | summary                         |
      | symbol                          |
      | xpos                            |
      | ypos                            |
      | wxpos                           |
      | wypos                           |
      | shells                          |
      | electron_configuration          |
      | electron_configuration_semantic |
      | electron_affinity               |
      | electronegativity_pauling       |
      | ionization_energies             |
      | cpk-hex                         |
      | image                           |
      | block                           |

  Scenario Outline: Periodic Table with properties to JSON
    Given properties separated by coma: "<properties>"
    When I extract the periodic table to a file with "json" extension
    Then the file should be created
    And the file with periodic table match the expected file
    Examples:
      | properties         |
      | name,appearance    |
      | name,atomic_mass   |
      | name,boil          |
      | number,symbol,name |
