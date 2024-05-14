'''
    Author:     H Foxwell
    Date:       14/May/2024
    Purpose:
        To dynamically load all assets into a single dictionary so
        that they can be used in the program without causing path
        errors.
'''
# Imports
from pathlib import Path

# Global Variables
GAME_ASSETS: dict[str, Path] = {}

def load_assets():
    """
        Searches the local directory for assets
        using current working directory.
    """
    # Constants
    cwd: Path = Path.cwd()
    assets_folder = Path.joinpath(cwd, 'assets')
    image_types = ('.jpg', '.png')

    for item in Path.iterdir(assets_folder):
        if item.is_file and item.suffix in image_types:
            GAME_ASSETS[item.stem] = item
