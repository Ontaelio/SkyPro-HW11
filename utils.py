import json
from typing import Optional, Iterable

from models.persons import Person


def import_data(json_file: str = 'candidates.json') -> list:
    """
    Get json data from the file provided
    :param json_file: filename, default is given
    :return: a list of dicts (or an empty list if FNF)
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as fin:
            staff = [Person(p) for p in json.load(fin)]
    except FileNotFoundError:
        staff = []

    return staff


def get_candidate_by_id(staff: Iterable[Person], id_num: int) -> Optional[Person]:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param id_num: candidate's ID (int)
    :return: a Person class object if found
    """

    for p in staff:
        if p.id == id_num:
            return p


def get_candidate_by_name(staff: Iterable[Person], name: str) -> Iterable[Person]:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param name: candidate's name (str)
    :return: a list of Person class objects
    """

    s_list = []
    for p in staff:
        if name.lower() in p.name.lower():
            s_list.append(p)

    return s_list


def get_candidate_by_skill(staff: Iterable[Person], skill: str) -> Iterable[Person]:
    """
    Returns a single candidate record
    :param staff: list of Person class objects
    :param skill: candidate's skill (str)
    :return: a list of Person class objects
    """

    s_list = []
    for p in staff:
        # using lower to ignore case
        if skill.lower() in [skl.lower() for skl in p.skills]:
            s_list.append(p)

    return s_list

