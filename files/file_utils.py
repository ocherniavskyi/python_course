import os
import json
from lxml import objectify
from .person import Person, PersonEncoder


def deserialize_persons_from_xml(file_path):
    with open(file_path, 'r') as file:
        objects = objectify.parse(file).getroot().PERSON
    return [Person(str(obj.FIRST_NAME), str(obj.LAST_NAME), str(obj.YEAR_OF_BIRTH), str(obj.MONTH_OF_BIRTH),
                   str(obj.DAY_OF_BIRTH), str(obj.COMPANY), str(obj.PROJECT), str(obj.ROLE), str(obj.ROOM),
                   str(obj.HOBBY)) for obj in objects]


def deserialize_persons_from_json(file_path):
    with open(file_path, 'r') as file:
        objects = json.load(file)
    return [Person(str(obj["FIRST_NAME"]), str(obj["LAST_NAME"]), str(obj["YEAR_OF_BIRTH"]), str(obj["MONTH_OF_BIRTH"]),
                   str(obj["DAY_OF_BIRTH"]), str(obj["COMPANY"]), str(obj["PROJECT"]), str(obj["ROLE"]), str(obj["ROOM"]),
                   str(obj["HOBBY"])) for obj in objects]


def serialize_persons_to_json(persons, file_path):
    if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
    with open(file_path, 'w') as file:
        json.dump(persons, file, cls=PersonEncoder)


def data_file_processing(path_to_source_file, path_to_destination_file):
    persons = deserialize_persons_from_xml(path_to_source_file)
    for person in persons:
        person.FIRST_NAME = "updated"
        person.LAST_NAME = "updated"
        person.DAY_OF_BIRTH = "updated"
        person.PROJECT = "updated"
        person.ROLE = "updated"
        person.ROOM = "updated"
        person.HOBBY = "updated"
    serialize_persons_to_json(persons, path_to_destination_file)


def main():
    resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.realpath("resources/samples"))
    print(resources_folder)
    path_to_json = os.path.join(resources_folder, "json/test_data.json")
    print(path_to_json)
    path_to_xml = os.path.join(resources_folder, "xml/test_data.xml")
    print(path_to_json)
    print("Persons before update: {}".format(deserialize_persons_from_xml(path_to_xml)))
    data_file_processing(path_to_xml, path_to_json)
    print("Persons after update: {}".format(deserialize_persons_from_json(path_to_json)))


if __name__ == "__main__":
    main()

