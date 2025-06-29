from typing import Optional

from src.core.custom_exceptions import InvalidVersion
from src.utils.instructions import get_instructions_versions_list, load_instructions


class VersionManager:
    instructions: Optional[dict]
    versions: list[str]
    departments: list[str]

    def __init__(self):
        self.instructions = None
        self.versions = get_instructions_versions_list()
        self.departments = []

    def load_version(self, version: str) -> None:
        if version not in self.versions:
            raise InvalidVersion(f'Invalid version: {version}')

        self.instructions = load_instructions(version)
        self.departments: list[str] = self.get_build_departments()

    def get_build_departments(self) -> list[str]:
        if self.instructions:
            return list(self.instructions.keys())
        else:
            return []
