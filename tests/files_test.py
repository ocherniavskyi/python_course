import os
from files import file_utils


path_to_json = "./resources/samples/json/test_data.json"
path_to_xml = "./resources/samples/xml/test_data.xml"


def test_check_test_data_file_exists():
    assert os.path.isfile(path_to_xml), "test_data.xml does't exist"


def test_check_test_data_file_has_valid_structure():
    assert file_utils.deserialize_persons_from_xml(path_to_xml)


def test_check_required_fields_updated():
    file_utils.data_file_processing(path_to_xml, path_to_json)
    persons = file_utils.deserialize_persons_from_json(path_to_json)
    for person in persons:
        assert person.FIRST_NAME == "updated"
        assert person.LAST_NAME == "updated"
        assert person.DAY_OF_BIRTH == "updated"
        assert person.PROJECT == "updated"
        assert person.ROLE == "updated"
        assert person.ROOM == "updated"
        assert person.HOBBY == "updated"


def test_check_that_json_file_created():
    if os.path.exists(path_to_json):
        os.remove(path_to_json)
    file_utils.data_file_processing(path_to_xml, path_to_json)
    assert os.path.isfile(path_to_json)


def test_check_that_json_file_content_correct():
    test_check_that_json_file_created()
    assert file_utils.deserialize_persons_from_json(path_to_json)
