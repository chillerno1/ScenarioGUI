import numpy as np
import PySide6.QtWidgets as QtW

from ScenarioGUI.gui_classes.gui_combine_window import MainWindow

from ..gui_structure_for_tests import GUI
from ..result_creating_class_for_tests import ResultsClass, data_2_results
from ..test_translations.translation_class import Translations


def test_float_box(qtbot):
    """
    test float box functions

    Parameters
    ----------
    qtbot: qtbot
        bot for the GUI
    """
    # init gui window
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    main_window.delete_backup()
    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
    float_b = main_window.gui_structure.float_b
    assert np.isclose(float_b.get_value(), float_b.default_value)
    float_b.set_value(float_b.default_value + 50)
    assert np.isclose(float_b.default_value + 50, float_b.get_value())
    float_b._init_links()
    assert float_b.check_linked_value((200, None))
    assert float_b.check_linked_value((None, 50))
    assert not float_b.check_linked_value((50, 200))
    float_b.show_option(main_window.gui_structure.int_a, 50, 200)
    main_window.gui_structure.page_inputs.button.click()
    assert main_window.gui_structure.int_a.is_hidden()
    float_b.set_value(20)
    float_b.show_option(main_window.gui_structure.int_a, 50, 200)
    assert not main_window.gui_structure.int_a.is_hidden()
    float_b.set_value(220)
    float_b.show_option(main_window.gui_structure.int_a, 50, 200)
    assert not main_window.gui_structure.int_a.is_hidden()
    float_b.add_link_2_show(main_window.gui_structure.int_a, 50, 200)
    float_b.set_value(110)
    assert main_window.gui_structure.int_a.is_hidden()
    float_b.set_value(20)
    assert not main_window.gui_structure.int_a.is_hidden()
    float_b.set_value(220)
    assert not main_window.gui_structure.int_a.is_hidden()
    # test set text
    main_window.gui_structure.float_b.set_text("Hello")
    assert main_window.gui_structure.float_b.label.text() == "Hello"
    main_window.save_scenario()
    assert "float_b" in main_window.list_ds[0].to_dict()
    main_window.delete_backup()
