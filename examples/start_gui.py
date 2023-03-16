"""
script to start the GUI
"""
# pragma: no cover
from __future__ import annotations

import sys
from platform import system
from sys import argv
from time import sleep
from typing import TYPE_CHECKING, Callable

import ScenarioGUI.global_settings as global_vars
from examples.translation_class import Translations
from ScenarioGUI.global_settings import FILE_EXTENSION, GUI_NAME
from ScenarioGUI.gui_classes.gui_structure import Aim, Category, GuiStructure, Page, ResultText
from ScenarioGUI.gui_classes.gui_structure_classes import IntBox

if TYPE_CHECKING:
    import PySide6.QtWidgets as QtW

os_system = system()
is_frozen = getattr(sys, "frozen", False) and os_system == "Windows"  # pragma: no cover


class ResultsClass:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.result = None

    def adding(self):
        sleep(5)
        self.result = self.a + self.b

    def subtract(self):
        self.result = self.a - self.b
        
    def _to_dict(self) -> dict:
        return {"a":self.a, "b": self.b, "result": self.result}


class GUI(GuiStructure):
    def __init__(self, default_parent: QtW.QWidget, translations: Translations):
        super().__init__(default_parent, translations)
        self.page_inputs = Page(name="Inputs", button_name="Inputs", icon="Add.svg")
        self.aim_add = Aim(label="Adding", icon="Add", page=self.page_inputs)
        self.aim_sub = Aim(label="Substract", icon="Delete", page=self.page_inputs)
        self.category_inputs = Category(page=self.page_inputs, label="Inputs")
        self.int_a = IntBox(
            label="a",
            default_value=2,
            minimal_value=0,
            maximal_value=200,
            category=self.category_inputs,
        )
        self.int_b = IntBox(
            label="b",
            default_value=2,
            minimal_value=0,
            maximal_value=200,
            category=self.category_inputs,
        )

        self.create_results_page()
        self.numerical_results = Category(
            page=self.page_result, label="Numerical results"
        )

        self.result_text_add = ResultText(
            "Result", category=self.numerical_results, prefix="Result: ", suffix="m"
        )
        self.result_text_add.text_to_be_shown("ResultsClass", "result")
        self.result_text_add.function_to_convert_to_text(lambda x: round(x, 2))
        self.result_text_sub = ResultText(
            "Result", category=self.numerical_results, prefix="Result: ", suffix="m"
        )
        self.result_text_sub.text_to_be_shown("ResultsClass", "result")
        self.result_text_sub.function_to_convert_to_text(lambda x: round(x, 2))
        self.aim_add.add_link_2_show(self.result_text_add)
        self.aim_sub.add_link_2_show(self.result_text_sub)

        self.create_settings_page()
        self.create_lists()


def data_2_results(data) -> tuple[ResultsClass, Callable[[], None]]:
    result = ResultsClass(data.int_a, data.int_b)
    return result, result.adding if data.aim_add else result.subtract


global_vars.ResultsClass = ResultsClass
global_vars.DATA_2_RESULTS_FUNCTION = data_2_results


def run(path_list=None):  # pragma: no cover
    if is_frozen:
        import pyi_splash

        pyi_splash.update_text("Loading .")
    from sys import exit as sys_exit

    if is_frozen:
        pyi_splash.update_text("Loading ..")

    from PySide6.QtWidgets import QApplication as QtWidgets_QApplication
    from PySide6.QtWidgets import QMainWindow as QtWidgets_QMainWindow

    from ScenarioGUI.global_settings import VERSION
    from ScenarioGUI.gui_classes.gui_combine_window import MainWindow

    if is_frozen:
        pyi_splash.update_text("Loading ...")

    # init application
    app = QtWidgets_QApplication()
    # set version and id
    myAppID = f"{GUI_NAME} v{VERSION}"  # arbitrary string
    if os_system == "Windows":
        from ctypes import windll as ctypes_windll

        ctypes_windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)
    app.setApplicationName(GUI_NAME)
    app.setApplicationVersion(f"v{VERSION}")
    # init window
    window = QtWidgets_QMainWindow()
    # init gui window
    main_window = MainWindow(window, app, GUI, Translations)
    if is_frozen:
        pyi_splash.update_text("Loading ...")
    # load file if it is in path list
    if path_list is not None:
        main_window.filename = (
            [path for path in path_list if path.endswith(f".{FILE_EXTENSION}")][0],
            0,
        )
        main_window.fun_load_known_filename()

    # show window
    if is_frozen:
        pyi_splash.close()
    window.showMaximized()
    # close app
    sys_exit(app.exec())


if __name__ == "__main__":  # pragma: no cover
    # pass system args like a file to read
    run(argv if len(argv) > 1 else None)
