

from PyQt4 import QtCore, QtGui
from ui.subpanel.BasePanelController import BasePanelController
from ui.subpanel.pidparametersupdater.PIDParametersUpdaterPanel import Ui_PIDParametersUpdaterPanel
from ui.subpanel.pidparametersupdater.accropidtuning.AccroPIDTuningController import AccroPIDTuningController
from ui.subpanel.pidparametersupdater.stablepidtuning.StablePIDTuningController import StablePIDTuningController
from ui.subpanel.pidparametersupdater.PIDUpdateMode import PIDUpdateMode

class PIDParametersUpdaterController(QtGui.QWidget, BasePanelController):
    
    
    def __init__(self, vehicle_event_dispatcher, ui_event_dispatcher):
        QtGui.QWidget.__init__(self)
        BasePanelController.__init__(self)
        
        self.ui = Ui_PIDParametersUpdaterPanel()
        self.ui.setupUi(self)
        
        self.ui.pid_type_list.addItem("ACCRO")
        self.ui.pid_type_list.addItem("STABLE")
        self.ui.pid_type_list.clicked.connect(self._pid_list_selection_clicked)
        self.ui.pid_type_list.setCurrentRow(0)
        
        self._accro_pid_tuning_controller = AccroPIDTuningController(vehicle_event_dispatcher, ui_event_dispatcher)
        self.ui.panel_container.addWidget(self._accro_pid_tuning_controller)
        self.ui.panel_container.setCurrentIndex(0)
        
        self._stable_pid_tuning_controller = StablePIDTuningController(vehicle_event_dispatcher, ui_event_dispatcher)
        self.ui.panel_container.addWidget(self._stable_pid_tuning_controller)
        
        self.ui.beginner_radio_button.clicked.connect(self._beginner_radio_button_pressed)
        self.ui.intermediate_radio_button.clicked.connect(self._intermediate_radio_button_pressed)
        self.ui.advance_radio_button.clicked.connect(self._advanced_radio_button_pressed)
        self.ui.beginner_radio_button.setChecked(True)
        self.ui.default_button.clicked.connect(self._default_button_pressed)
        
        self._current_pid_tuning_controller = self._accro_pid_tuning_controller
        self._user_level_mode = PIDUpdateMode.BEGINNER_MODE
        
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self._sync_with_board)
        
    def _pid_list_selection_clicked(self):
        self._current_pid_tuning_controller.stop()
        if (self.ui.pid_type_list.currentItem().text() == 'ACCRO'):
            self._current_pid_tuning_controller = self._accro_pid_tuning_controller
        else:
            self._current_pid_tuning_controller = self._stable_pid_tuning_controller
        
        self.ui.panel_container.setCurrentWidget(self._current_pid_tuning_controller)
        if (self._user_level_mode == PIDUpdateMode.BEGINNER_MODE) :
            self._current_pid_tuning_controller.setBeginnerMode()
        elif (self._user_level_mode == PIDUpdateMode.INTERMEDIATE_MODE) :
            self._current_pid_tuning_controller.setIntermediateMode()
        else :
            self._current_pid_tuning_controller.setAdvancedMode()
        self._current_pid_tuning_controller.start()
        
    def _beginner_radio_button_pressed(self):
        self._user_level_mode = PIDUpdateMode.BEGINNER_MODE
        self._current_pid_tuning_controller.set_beginner_mode()
        
    def _intermediate_radio_button_pressed(self):
        self._user_level_mode = PIDUpdateMode.INTERMEDIATE_MODE
        self._current_pid_tuning_controller.set_intermediate_mode()
    
    def _advanced_radio_button_pressed(self):
        self._user_level_mode = PIDUpdateMode.ADVANCED_MODE
        self._current_pid_tuning_controller.set_advanced_mode()

    def start(self):
        self._current_pid_tuning_controller.start()
        self._timer.start(250)
        
    def stop(self):
        self._current_pid_tuning_controller.stop()
        self._timer.stop()

    def _sync_with_board(self):
        self._current_pid_tuning_controller.sync_with_board()

    def _default_button_pressed(self):
        self._current_pid_tuning_controller.reset_default()
