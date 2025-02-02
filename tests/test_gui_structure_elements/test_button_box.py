import numpy as np
import PySide6.QtWidgets as QtW

from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
from ScenarioGUI.gui_classes.gui_structure_classes import Option

from ..gui_structure_for_tests import GUI
from ..result_creating_class_for_tests import ResultsClass, data_2_results
from ..test_translations.translation_class import Translations


def test_button_box(qtbot):
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

    button_box = main_window.gui_structure.button_box
    assert np.isclose(button_box.get_value(), button_box.default_value)
    button_box.set_value(button_box.default_value + 1)
    assert np.isclose(button_box.default_value + 1, button_box.get_value())
    button_box._init_links()
    assert button_box.check_linked_value(button_box.default_value + 1)
    assert not button_box.check_linked_value(button_box.default_value)
    button_box.add_link_2_show(main_window.gui_structure.int_a, on_index=0)
    button_box.set_value(button_box.default_value)
    button_box.set_value(button_box.default_value + 1)
    assert main_window.gui_structure.int_a.is_hidden()
    button_box.set_value(button_box.default_value)
    assert not main_window.gui_structure.int_a.is_hidden()
    main_window.save_scenario()
    assert "button_box" in main_window.list_ds[0].to_dict()
    # test if the hidden button box is enabled
    main_window.gui_structure.aim_plot.widget.click() if not main_window.gui_structure.aim_plot.widget.isChecked() else None
    button_box.set_value(button_box.default_value + 1)
    main_window.save_scenario()
    main_window.add_scenario()
    main_window.gui_structure.aim_add.widget.click()
    main_window.save_scenario()
    main_window.add_scenario()
    main_window.gui_structure.aim_plot.widget.click()
    button_box.set_value(button_box.default_value)
    main_window.save_scenario()
    assert main_window.list_widget_scenario.count() == 3
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(1))
    assert np.isclose(button_box.default_value + 1, button_box.get_value())
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(2))
    Option.hidden_option_editable = False
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(1))
    assert np.isclose(button_box.default_value, button_box.get_value())
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(2))
    Option.hidden_option_editable = True
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(1))
    assert np.isclose(button_box.default_value + 1, button_box.get_value())
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(2))
    button_box.hidden_option_editable = False
    assert np.isclose(button_box.default_value, button_box.get_value())
    main_window.list_widget_scenario.setCurrentItem(main_window.list_widget_scenario.item(2))
    Option.hidden_option_editable = True
    assert not button_box.hidden_option_editable
    button_box.hidden_option_editable = True
    main_window.delete_backup()

