import json

from models.persons import Person


def import_data(json_file: str = 'candidates.json'):
    """
    Get json data from the file provided
    :param json_file: filename, default is given
    :return: a list of dicts (or None if FNF)
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as fin:
            staff = [Person(p) for p in json.load(fin)]
    except FileNotFoundError:
        staff = None

    return staff


def get_candidate_by_id(staff: list, id: int) -> Person:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param id: candidate's ID (int)
    :return: a Person class object
    """

    for p in staff:
        if p.id == id:
            return p


def get_candidate_by_name(staff: list, name: str) -> list:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param name: candidate's name (str)
    :return: a Person class object
    """

    s_list = []
    for p in staff:
        if name.lower() in p.name.lower():
            s_list.append(p)

    if s_list:
        return s_list


def get_candidate_by_skill(staff: list, skill: str) -> list:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param skill: candidate's skill (str)
    :return: a list pf Person class objects
    """

    s_list = []
    for p in staff:
        if skill.lower() in [skl.lower() for skl in p.skills]:
            s_list.append(p)

    if s_list:
        return s_list

