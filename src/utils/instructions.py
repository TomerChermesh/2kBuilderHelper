import os

from src.utils.files import load_json_file

INSTRUCTIONS_DIR = os.path.join('../../resources', 'instructions')


def get_instructions_versions_list() -> list[str]:
    files_names: list[str] = os.listdir(INSTRUCTIONS_DIR)
    instructions_versions_list: list[str] = []
    for file_name in files_names:
        if file_name.endswith('.json'):
            instructions_versions_list.append(file_name[:-5])

    return instructions_versions_list


def load_instructions(version: str) -> dict:
    filepath: str = os.path.join(INSTRUCTIONS_DIR, f'{version}.json')
    return load_json_file(filepath=filepath)


if __name__ == '__main__':
    print(get_instructions_versions_list())
    print(load_instructions('2k24'))
