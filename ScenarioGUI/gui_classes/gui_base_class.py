"""
This document contains some base functionality for the GUI.
It contains a function to reformat the graphs to a layout for the gui,
and it contains the main class that creates the framework for the GUI (top bar etc.)
"""
import PySide6.QtCore as QtC
import PySide6.QtGui as QtG
import PySide6.QtWidgets as QtW

from ..global_settings import BLACK, DARK, FOLDER, FONT, FONT_SIZE, GREY, ICON_NAME, LIGHT, LIGHT_SELECT, WHITE


class BaseUI:
    """
    This class contains the framework of the GUI, with the top bar,
    the scenario/run/ ... buttons and the shortcuts.
    """

    menu_language: QtW.QMenu
    status_bar: QtW.QStatusBar
    tool_bar: QtW.QToolBar
    menu_scenario: QtW.QMenu
    menu_settings: QtW.QMenu
    menu_calculation: QtW.QMenu
    push_button_cancel: QtW.QPushButton
    menu_file: QtW.QMenu
    push_button_start_multiple: QtW.QPushButton
    push_button_start_single: QtW.QPushButton
    horizontal_spacer_start_buttons: QtW.QSpacerItem
    progress_bar: QtW.QProgressBar
    horizontal_layout_start_buttons: QtW.QHBoxLayout
    label_status: QtW.QLabel
    horizontal_layout_progress_bar: QtW.QHBoxLayout
    stacked_widget: QtW.QStackedWidget
    vertical_layout_main: QtW.QVBoxLayout
    vertical_layout_menu: QtW.QVBoxLayout
    list_widget_scenario: QtW.QListWidget
    button_rename_scenario: QtW.QPushButton
    push_button_save_scenario: QtW.QPushButton
    vertical_layout_scenario: QtW.QVBoxLayout
    horizontal_layout_main: QtW.QHBoxLayout
    central_widget: QtW.QWidget
    push_button_delete_scenario: QtW.QPushButton
    action_start_single: QtG.QAction
    action_rename_scenario: QtG.QAction
    action_save_as: QtG.QAction
    action_delete_scenario: QtG.QAction
    action_add_scenario: QtG.QAction
    action_update_scenario: QtG.QAction
    menubar: QtW.QMenuBar
    push_button_add_scenario: QtW.QPushButton
    action_start_multiple: QtG.QAction
    action_open: QtG.QAction
    action_save: QtG.QAction
    action_new: QtG.QAction

    def setup_ui(self, ghe_tool):
        if not ghe_tool.objectName():
            ghe_tool.setObjectName("GHEtool")
        ghe_tool.resize(1920, 1080)
        size_policy = QtW.QSizePolicy(QtW.QSizePolicy.Preferred, QtW.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(ghe_tool.sizePolicy().hasHeightForWidth())
        ghe_tool.setSizePolicy(size_policy)
        ghe_tool.setMaximumSize(QtC.QSize(16777215, 16777215))
        font = QtG.QFont()
        font.setFamilies([FONT])
        font.setPointSize(FONT_SIZE)
        font.setBold(False)
        font.setItalic(False)
        ghe_tool.setFont(font)
        icon = QtG.QIcon()
        icon.addFile(f"{FOLDER}/icons/{ICON_NAME}", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        ghe_tool.setWindowIcon(icon)
        ghe_tool.setStyleSheet(
            f"*{'{'}color: {WHITE};font: {FONT_SIZE}pt '{FONT}';background-color: {DARK};selection-background-color: {LIGHT};"
            f"alternate-background-color: {LIGHT};{'}'}\n"
            f"QPushButton{'{'}border: 3px solid {LIGHT};border-radius: 5px;color:{WHITE};gridline-color:{LIGHT};background-color:{LIGHT};"
            f"font: 700 11pt '{font}';{'}'}"
            f"QPushButton:hover{'{'}background-color: {DARK};{'}'}\n"
            f"QPushButton:disabled{'{'}border: 3px solid {GREY};border-radius: 5px;color: {WHITE};gridline-color: {GREY};background-color: {GREY};{'}'}\n"
            f"QPushButton:disabled:hover{'{'}background-color: {DARK};{'}'}\n"
            f"QComboBox{'{'}border: 1px solid {WHITE};border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;{'}'}\n"
            f"QSpinBox{'{'}selection-color: {WHITE};selection-background-color: {LIGHT};border: 1px solid {WHITE};font: 11pt '{FONT}';{'}'}\n"
            f"QLineEdit{'{'}border: 3px solid {LIGHT};border-radius: 5px;color: {WHITE};gridline-color: {LIGHT};background-color: {LIGHT};font-weight:500;\n"
            f"selection-background-color: {LIGHT_SELECT};{'}'}\n"
            f"QLineEdit:hover{'{'}background-color: {DARK};{'}'}"
            f"QToolTip{'{'}color: {WHITE}; background-color: {DARK}; border: 1px solid {LIGHT};border-radius: 4px;{'}'}"
            f"QTabBar::tab{'{'}background-color: {DARK};padding-top:5px;padding-bottom:5px;padding-left:5px;padding-right:5px;color: {WHITE};{'}'}"
            f"QTabBar::tab:selected, QTabBar::tab:hover{'{'}background-color: {LIGHT};{'}'}"
            f"QTabBar::tab:selected{'{'}background-color: {LIGHT};{'}'}"
            f"QTabBar::tab:!selected{'{'}background-color:  {DARK};{'}'}"
            f"QTabWidget::pane{'{'}border: 1px solid {WHITE};{'}'}"
            f"QTabWidget::tab-bar{'{'}left: 5px;{'}'}"
        )
        self.action_new = QtG.QAction(ghe_tool)
        self.action_new.setObjectName("actionNew")
        self.action_new.setCheckable(False)
        self.action_new.setChecked(False)
        self.action_new.setEnabled(True)
        icon1 = QtG.QIcon()
        icon1.addFile(f"{FOLDER}/icons/New.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon1.addFile(f"{FOLDER}/icons/New_Inv.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_new.setIcon(icon1)
        self.action_save = QtG.QAction(ghe_tool)
        self.action_save.setObjectName("actionSave")
        self.action_save.setEnabled(True)
        icon2 = QtG.QIcon()
        icon2.addFile(f"{FOLDER}/icons/Save.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon2.addFile(f"{FOLDER}/icons/Save_Inv.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_open = QtG.QAction(ghe_tool)
        self.action_open.setObjectName("actionOpen")
        self.action_open.setEnabled(True)
        icon3 = QtG.QIcon()
        icon3.addFile(f"{FOLDER}/icons/Open.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon3.addFile(f"{FOLDER}/icons/Open_Inv.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_open.setIcon(icon3)
        self.action_start_multiple = QtG.QAction(ghe_tool)
        self.action_start_multiple.setObjectName("action_start_multiple")
        self.action_start_multiple.setEnabled(True)
        icon4 = QtG.QIcon()
        icon4.addFile(
            f"{FOLDER}/icons/Start_multiple_inv.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        icon4.addFile(
            f"{FOLDER}/icons/Start_multiple.svg",
            QtC.QSize(),
            QtG.QIcon.Active,
            QtG.QIcon.Off,
        )
        self.action_start_multiple.setIcon(icon4)
        self.action_update_scenario = QtG.QAction(ghe_tool)
        self.action_update_scenario.setObjectName("actionUpdate_Scenario")
        icon7 = QtG.QIcon()
        icon7.addFile(
            f"{FOLDER}/icons/Update_Inv.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        icon7.addFile(f"{FOLDER}/icons/Update.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_update_scenario.setIcon(icon7)
        self.action_add_scenario = QtG.QAction(ghe_tool)
        self.action_add_scenario.setObjectName("actionAdd_Scenario")
        icon8 = QtG.QIcon()
        icon8.addFile(f"{FOLDER}/icons/Add_Inv.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon8.addFile(f"{FOLDER}/icons/Add.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_add_scenario.setIcon(icon8)
        self.action_delete_scenario = QtG.QAction(ghe_tool)
        self.action_delete_scenario.setObjectName("actionDelete_scenario")
        icon9 = QtG.QIcon()
        icon9.addFile(
            f"{FOLDER}/icons/Delete_Inv.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        icon9.addFile(f"{FOLDER}/icons/Delete.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_delete_scenario.setIcon(icon9)
        self.action_save_as = QtG.QAction(ghe_tool)
        self.action_save_as.setObjectName("actionSave_As")
        icon10 = QtG.QIcon()
        icon10.addFile(f"{FOLDER}/icons/SaveAs.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon10.addFile(
            f"{FOLDER}/icons/Save_As_Inv.svg",
            QtC.QSize(),
            QtG.QIcon.Active,
            QtG.QIcon.Off,
        )
        self.action_save_as.setIcon(icon10)
        self.action_rename_scenario = QtG.QAction(ghe_tool)
        self.action_rename_scenario.setObjectName("actionRename_scenario")
        icon14 = QtG.QIcon()
        icon14.addFile(
            f"{FOLDER}/icons/Rename_Inv.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        icon14.addFile(f"{FOLDER}/icons/Rename.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_rename_scenario.setIcon(icon14)
        self.action_start_single = QtG.QAction(ghe_tool)
        self.action_start_single.setObjectName("action_start_single")
        icon15 = QtG.QIcon()
        icon15.addFile(
            f"{FOLDER}/icons/Start_inv.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        icon15.addFile(f"{FOLDER}/icons/Start.svg", QtC.QSize(), QtG.QIcon.Active, QtG.QIcon.Off)
        self.action_start_single.setIcon(icon15)
        self.central_widget = QtW.QWidget(ghe_tool)
        self.central_widget.setObjectName("central_widget")
        self.horizontal_layout_main = QtW.QHBoxLayout(self.central_widget)
        self.horizontal_layout_main.setObjectName("horizontalLayout_23")
        self.vertical_layout_scenario = QtW.QVBoxLayout()
        self.vertical_layout_scenario.setObjectName("verticalLayout_scenario")
        self.push_button_save_scenario = QtW.QPushButton(self.central_widget)
        self.push_button_save_scenario.setObjectName("pushButton_SaveScenario")
        size_policy1 = QtW.QSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Minimum)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(self.push_button_save_scenario.sizePolicy().hasHeightForWidth())
        self.push_button_save_scenario.setSizePolicy(size_policy1)
        self.push_button_save_scenario.setMinimumSize(QtC.QSize(180, 30))
        self.push_button_save_scenario.setMaximumSize(QtC.QSize(250, 30))
        self.push_button_save_scenario.setStyleSheet("text-align:left;")
        icon18 = QtG.QIcon()
        icon18.addFile(f"{FOLDER}/icons/Update.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.push_button_save_scenario.setIcon(icon18)
        self.push_button_save_scenario.setIconSize(QtC.QSize(20, 20))

        self.vertical_layout_scenario.addWidget(self.push_button_save_scenario)

        self.push_button_add_scenario = QtW.QPushButton(self.central_widget)
        self.push_button_add_scenario.setObjectName("pushButton_AddScenario")
        self.push_button_add_scenario.setMinimumSize(QtC.QSize(180, 30))
        self.push_button_add_scenario.setMaximumSize(QtC.QSize(250, 30))
        self.push_button_add_scenario.setStyleSheet("text-align:left;")
        icon19 = QtG.QIcon()
        icon19.addFile(f"{FOLDER}/icons/Add.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.push_button_add_scenario.setIcon(icon19)
        self.push_button_add_scenario.setIconSize(QtC.QSize(20, 20))

        self.vertical_layout_scenario.addWidget(self.push_button_add_scenario)

        self.push_button_delete_scenario = QtW.QPushButton(self.central_widget)
        self.push_button_delete_scenario.setObjectName("pushButton_DeleteScenario")
        self.push_button_delete_scenario.setMinimumSize(QtC.QSize(180, 30))
        self.push_button_delete_scenario.setMaximumSize(QtC.QSize(250, 30))
        self.push_button_delete_scenario.setStyleSheet("text-align:left;")
        icon20 = QtG.QIcon()
        icon20.addFile(f"{FOLDER}/icons/Delete.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.push_button_delete_scenario.setIcon(icon20)
        self.push_button_delete_scenario.setIconSize(QtC.QSize(20, 20))

        self.vertical_layout_scenario.addWidget(self.push_button_delete_scenario)

        self.button_rename_scenario = QtW.QPushButton(self.central_widget)
        self.button_rename_scenario.setObjectName("button_rename_scenario")
        self.button_rename_scenario.setMinimumSize(QtC.QSize(180, 30))
        self.button_rename_scenario.setMaximumSize(QtC.QSize(250, 30))
        self.button_rename_scenario.setStyleSheet("text-align:left;")
        icon21 = QtG.QIcon()
        icon21.addFile(f"{FOLDER}/icons/Rename.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.button_rename_scenario.setIcon(icon21)
        self.button_rename_scenario.setIconSize(QtC.QSize(20, 20))

        self.vertical_layout_scenario.addWidget(self.button_rename_scenario)

        self.list_widget_scenario = QtW.QListWidget(self.central_widget)
        QtW.QListWidgetItem(self.list_widget_scenario)
        self.list_widget_scenario.setObjectName("list_widget_scenario")
        size_policy.setHeightForWidth(self.list_widget_scenario.sizePolicy().hasHeightForWidth())
        self.list_widget_scenario.setSizePolicy(size_policy)
        self.list_widget_scenario.setMaximumSize(QtC.QSize(16666711, 16666711))
        self.list_widget_scenario.setStyleSheet(
            f"*{'{'}border: 1px solid {WHITE};{'}'}\n"
            "QListWidget{outline: 0;}\n"
            f"QListWidget::item:selected{'{'}background:{LIGHT};color: {WHITE};border: 0px solid {WHITE};{'}'}\n"
            f"QListWidget::item:hover{'{'}border: 1px solid {WHITE};color: {WHITE};{'}'}QListWidget:disabled{'{'}background-color: {GREY};{'}'}"
        )
        self.list_widget_scenario.setSizeAdjustPolicy(QtW.QAbstractScrollArea.AdjustToContents)
        self.list_widget_scenario.setAutoScrollMargin(10)
        self.list_widget_scenario.setEditTriggers(
            QtW.QAbstractItemView.DoubleClicked | QtW.QAbstractItemView.EditKeyPressed | QtW.QAbstractItemView.SelectedClicked
        )
        self.list_widget_scenario.setDragDropMode(QtW.QAbstractItemView.DragDrop)
        self.list_widget_scenario.setDefaultDropAction(QtC.Qt.TargetMoveAction)
        self.list_widget_scenario.setSelectionBehavior(QtW.QAbstractItemView.SelectItems)
        self.list_widget_scenario.setSelectionRectVisible(False)

        self.vertical_layout_scenario.addWidget(self.list_widget_scenario)

        self.horizontal_layout_main.addLayout(self.vertical_layout_scenario)

        self.vertical_layout_menu = QtW.QVBoxLayout()
        self.vertical_layout_menu.setSpacing(0)
        self.vertical_layout_menu.setObjectName("verticalLayout_menu")

        self.horizontal_layout_main.addLayout(self.vertical_layout_menu)

        self.vertical_layout_main = QtW.QVBoxLayout()
        self.vertical_layout_main.setObjectName("verticalLayout_21")
        self.stacked_widget = QtW.QStackedWidget(self.central_widget)
        self.stacked_widget.setObjectName("stackedWidget")
        self.stacked_widget.setFrameShadow(QtW.QFrame.Plain)
        self.stacked_widget.setLineWidth(0)

        self.vertical_layout_main.addWidget(self.stacked_widget)

        self.horizontal_layout_progress_bar = QtW.QHBoxLayout()
        self.horizontal_layout_progress_bar.setObjectName("horizontalLayout_7")
        self.label_status = QtW.QLabel(self.central_widget)
        self.label_status.setObjectName("label_Status")
        self.label_status.setStyleSheet(f"*{'{'}background-color: {LIGHT};{'}'}")
        self.horizontal_layout_progress_bar.addWidget(self.label_status)

        self.progress_bar = QtW.QProgressBar(self.central_widget)
        self.progress_bar.setObjectName("progressBar")
        self.progress_bar.setStyleSheet(
            f"QProgressBar{'{'}border: 1px solid {WHITE};border-radius: 10px;text-align: center;color: {WHITE};{'}'}\n"
            f"QProgressBar::chunk{'{'}background-color: {LIGHT}; border-radius: 10px;{'}'}"
        )
        self.progress_bar.setValue(24)

        self.horizontal_layout_progress_bar.addWidget(self.progress_bar)

        self.vertical_layout_main.addLayout(self.horizontal_layout_progress_bar)

        self.horizontal_layout_start_buttons = QtW.QHBoxLayout()
        self.horizontal_layout_start_buttons.setObjectName("horizontalLayout_2")
        self.horizontal_spacer_start_buttons = QtW.QSpacerItem(40, 20, QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Minimum)

        self.horizontal_layout_start_buttons.addItem(self.horizontal_spacer_start_buttons)

        self.push_button_start_single = QtW.QPushButton(self.central_widget)
        self.push_button_start_single.setObjectName("pushButton_start_single")
        self.push_button_start_single.setMinimumSize(QtC.QSize(100, 40))
        self.push_button_start_single.setMaximumSize(QtC.QSize(16777215, 40))
        icon32 = QtG.QIcon()
        icon32.addFile(f"{FOLDER}/icons/Start.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.push_button_start_single.setIcon(icon32)
        self.push_button_start_single.setIconSize(QtC.QSize(24, 24))

        self.horizontal_layout_start_buttons.addWidget(self.push_button_start_single)

        self.push_button_start_multiple = QtW.QPushButton(self.central_widget)
        self.push_button_start_multiple.setObjectName("pushButton_start_multiple")
        self.push_button_start_multiple.setMinimumSize(QtC.QSize(100, 40))
        self.push_button_start_multiple.setMaximumSize(QtC.QSize(16777215, 40))
        icon33 = QtG.QIcon()
        icon33.addFile(
            f"{FOLDER}/icons/Start_multiple.svg",
            QtC.QSize(),
            QtG.QIcon.Normal,
            QtG.QIcon.Off,
        )
        self.push_button_start_multiple.setIcon(icon33)
        self.push_button_start_multiple.setIconSize(QtC.QSize(24, 24))

        self.horizontal_layout_start_buttons.addWidget(self.push_button_start_multiple)

        self.push_button_cancel = QtW.QPushButton(self.central_widget)
        self.push_button_cancel.setObjectName("pushButton_Cancel")
        self.push_button_cancel.setMinimumSize(QtC.QSize(100, 40))
        self.push_button_cancel.setMaximumSize(QtC.QSize(16777215, 40))
        icon34 = QtG.QIcon()
        icon34.addFile(f"{FOLDER}/icons/Exit.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        self.push_button_cancel.setIcon(icon34)
        self.push_button_cancel.setIconSize(QtC.QSize(24, 24))

        self.horizontal_layout_start_buttons.addWidget(self.push_button_cancel)

        self.vertical_layout_main.addLayout(self.horizontal_layout_start_buttons)

        self.horizontal_layout_main.addLayout(self.vertical_layout_main)

        ghe_tool.setCentralWidget(self.central_widget)
        self.menubar = QtW.QMenuBar(ghe_tool)
        self.menubar.setObjectName("menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtC.QRect(0, 0, 1226, 30))
        self.menubar.setStyleSheet(
            f"QMenuBar::item{'{'}background-color: {DARK};{'}'}\n"
            f"QMenuBar::item:pressed{'{'}background-color: {LIGHT};{'}'}\n"
            f"QMenuBar::item:selected{'{'}background-color: {LIGHT};{'}'}\n"
            f"QToolTip{'{'} color: {WHITE}; background-color: {BLACK}; border: none; {'}'}"
        )
        self.menubar.setNativeMenuBar(True)
        self.menu_file = QtW.QMenu(self.menubar)
        self.menu_file.setObjectName("menuFile")
        self.menu_file.setStyleSheet(
            f"QtG.QAction::icon {'{'} background-color:{LIGHT};selection-background-color: {LIGHT};{'}'}\n"
            f"*{'{'}	background-color: {DARK};{'}'}\n"
            f"*:hover{'{'}background-color: {LIGHT};{'}'}"
        )
        self.menu_file.setTearOffEnabled(False)
        self.menu_calculation = QtW.QMenu(self.menubar)
        self.menu_calculation.setObjectName("menuCalculation")
        self.menu_settings = QtW.QMenu(self.menubar)
        self.menu_settings.setObjectName("menuSettings")
        self.menu_language = QtW.QMenu(self.menu_settings)
        self.menu_language.setObjectName("menuLanguage")
        self.menu_language.setEnabled(True)
        icon35 = QtG.QIcon()
        icon35.addFile(f"{FOLDER}/icons/Language.svg", QtC.QSize(), QtG.QIcon.Normal, QtG.QIcon.Off)
        icon35.addFile(
            f"{FOLDER}/icons/Language_Inv.svg",
            QtC.QSize(),
            QtG.QIcon.Active,
            QtG.QIcon.Off,
        )
        self.menu_language.setIcon(icon35)
        self.menu_scenario = QtW.QMenu(self.menubar)
        self.menu_scenario.setObjectName("menuScenario")
        ghe_tool.setMenuBar(self.menubar)
        self.tool_bar = QtW.QToolBar(ghe_tool)
        self.tool_bar.setObjectName("toolBar")
        self.tool_bar.setStyleSheet(
            f"QAction::icon {'{'} background-color:{LIGHT};selection-background-color: {LIGHT};{'}'}\n"
            f"*{'{'}	background-color: {DARK};{'}'}\n"
            f"*:hover{'{'}background-color: {LIGHT};{'}'}"
        )
        self.tool_bar.setMovable(False)
        ghe_tool.addToolBar(QtC.Qt.TopToolBarArea, self.tool_bar)
        self.status_bar = QtW.QStatusBar(ghe_tool)
        self.status_bar.setObjectName("status_bar")
        self.status_bar.setStyleSheet(f"QStatusBar::item{'{'}border:None;{'}'}QStatusBar{'{'}color:{BLACK};background-color: {LIGHT};{'}'}")
        ghe_tool.setStatusBar(self.status_bar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_calculation.menuAction())
        self.menubar.addAction(self.menu_scenario.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_open)
        self.menu_calculation.addAction(self.action_start_multiple)
        self.menu_calculation.addAction(self.action_start_single)
        self.menu_settings.addAction(self.menu_language.menuAction())
        self.menu_scenario.addAction(self.action_update_scenario)
        self.menu_scenario.addAction(self.action_add_scenario)
        self.menu_scenario.addAction(self.action_delete_scenario)
        self.menu_scenario.addAction(self.action_rename_scenario)
        self.tool_bar.addAction(self.action_new)
        self.tool_bar.addAction(self.action_save)
        self.tool_bar.addAction(self.action_save_as)
        self.tool_bar.addAction(self.action_open)
        self.tool_bar.addAction(self.action_start_single)
        self.tool_bar.addAction(self.action_start_multiple)
        self.tool_bar.addAction(self.action_update_scenario)
        self.tool_bar.addAction(self.action_add_scenario)
        self.tool_bar.addAction(self.action_delete_scenario)
        self.tool_bar.addAction(self.action_rename_scenario)

        self.button_rename_scenario.clicked.connect(self.action_rename_scenario.trigger)
        self.push_button_cancel.clicked.connect(ghe_tool.close)
        self.push_button_start_multiple.clicked.connect(self.action_start_multiple.trigger)
        self.push_button_add_scenario.clicked.connect(self.action_add_scenario.trigger)
        self.push_button_delete_scenario.clicked.connect(self.action_delete_scenario.trigger)
        self.push_button_save_scenario.clicked.connect(self.action_update_scenario.trigger)
        self.list_widget_scenario.itemDoubleClicked.connect(self.action_rename_scenario.trigger)
        self.push_button_start_single.clicked.connect(self.action_start_single.trigger)

        self.stacked_widget.setCurrentIndex(0)
        QtC.QMetaObject.connectSlotsByName(ghe_tool)

        ghe_tool.setWindowTitle("GHEtool")
        self.action_new.setText("New")
        # if QT_CONFIG(tooltip)
        self.action_new.setToolTip("Create new project file")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.action_new.setShortcut("Ctrl+N")
        # endif // QT_CONFIG(shortcut)
        self.action_save.setText("Save")
        # if QT_CONFIG(shortcut)
        self.action_save.setShortcut("Ctrl+S")
        # endif // QT_CONFIG(shortcut)
        self.action_open.setText("Open")
        # if QT_CONFIG(shortcut)
        self.action_open.setShortcut("Ctrl+O")
        # endif // QT_CONFIG(shortcut)
        self.action_start_multiple.setText("Calculate all scenarios")
        # if QT_CONFIG(shortcut)
        self.action_start_multiple.setShortcut("Ctrl+R")
        # endif // QT_CONFIG(shortcut)
        self.action_update_scenario.setText("Update scenario")
        # if QT_CONFIG(shortcut)
        self.action_update_scenario.setShortcut("Ctrl+Shift+S")
        # endif // QT_CONFIG(shortcut)
        self.action_add_scenario.setText("Add scenario")
        # if QT_CONFIG(shortcut)
        self.action_add_scenario.setShortcut("Ctrl+Shift+A")
        # endif // QT_CONFIG(shortcut)
        self.action_delete_scenario.setText("Delete scenario")
        # if QT_CONFIG(shortcut)
        self.action_delete_scenario.setShortcut("Ctrl+Shift+D")
        # endif // QT_CONFIG(shortcut)
        self.action_save_as.setText("Save As")
        # if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut("F12")
        # endif // QT_CONFIG(shortcut)
        self.action_rename_scenario.setText("Rename scenario")
        # if QT_CONFIG(shortcut)
        self.action_rename_scenario.setShortcut("Ctrl+Shift+R")
        # endif // QT_CONFIG(shortcut)
        self.action_start_single.setText("Calculate current scenario")
        # if QT_CONFIG(shortcut)
        self.action_start_single.setShortcut("Ctrl+Shift+R")
        # endif // QT_CONFIG(shortcut)
        self.push_button_save_scenario.setText("Update scenario")
        self.push_button_add_scenario.setText("Add scenario")
        self.push_button_delete_scenario.setText("Delete scenario")
        self.button_rename_scenario.setText("Rename scenario")

        __sorting_enabled = self.list_widget_scenario.isSortingEnabled()
        self.list_widget_scenario.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_widget_scenario.item(0)
        ___qlistwidgetitem.setText("Scenario: 1")
        self.list_widget_scenario.setSortingEnabled(__sorting_enabled)
        self.label_status.setText("Progress: ")
        self.push_button_start_single.setText("Calculate current scenario")
        self.push_button_start_multiple.setText("Calculate all scenarios")
        self.push_button_cancel.setText("Exit")
        self.menu_file.setTitle("File")
        self.menu_calculation.setTitle("Calculation")
        self.menu_settings.setTitle("Settings")
        self.menu_language.setTitle("Language")
        self.menu_scenario.setTitle("Scenario")
        self.tool_bar.setWindowTitle("toolBar")
