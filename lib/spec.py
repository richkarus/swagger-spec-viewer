import os
import json
from os.path import isfile, join, abspath, curdir
from pathlib import Path, PosixPath
from typing import List, Dict


class SpecLoader:
    """
    Load specs from the specs/ folder
    and return list of validated dictionaries

    Ideally when passing specs, this will only work
    currently with JSON files.
    """

    def __init__(self) -> None:
        self.parent_path = Path(abspath(curdir))
        self.specs_path = Path(self.parent_path / "specs")

    def load(self) -> List[Dict]:
        """
        Load swagger JSON file(s) and return as a list of string dicts
        """
        return [{f.stem: json.dumps(self.json_loader(f))} for f in self.spec_files]

    @property
    def spec_files(self) -> List[PosixPath]:
        """
        Return list of PosixPath specs ready for loading
        """
        return [
            self.specs_path / spec
            for spec in os.listdir(self.specs_path)
            if self.is_file(spec)
        ]

    def json_loader(self, path: PosixPath) -> Dict:
        """
        Try to load JSON and pass if exception raised
        """
        try:
            return json.load(open(path, "r"))
        except json.JSONDecodeError:
            pass

    def is_empty(self) -> bool:
        """
        Check if the folder is empty.

        True is empty
        False is not empty
        """
        return len(os.listdir(self.specs_path)) == 0

    def is_file(self, file: str) -> bool:
        """
        Check whether path is a file

        True is a file
        False is not a file
        """

        return isfile(join(self.specs_path, file))
