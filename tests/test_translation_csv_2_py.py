from pathlib import Path
import pandas as pd

from ScenarioGUI.translation_csv_to_py import translate_csv_2_class
from ScenarioGUI.global_settings import FOLDER


def test_csv_2_py():
    folder: Path = Path(__file__).parent
    translate_csv_2_class(FOLDER.joinpath("./gui_classes/Translations.csv"), folder)
    d_f = pd.read_csv(FOLDER.joinpath("./gui_classes/Translations.csv"), sep=";")
    from .translation_class import Translations
    translation = Translations()
    for name, trans_1, trans_2 in zip(d_f["name"], d_f["English"], d_f["German"], strict=True):
        assert getattr(translation, name)[0] == trans_1
        assert getattr(translation, name)[1] == trans_2
