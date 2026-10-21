from common import *
import names
import test
def main():
    enter_login_pin()
    open_expert_screen()
    test.vp("TreatmentScreen")
    adjust_primary_pulse_energy_frequency()
    adjust_secondary_pulse_energy_frequency()
    interact_with_value_and_fiber_labels()
    interact_with_pedal_preset_tabs()
    move_treatment_screen_sliders_to_right()
    change_standby_ready_states()
    test.vp("ReadyScreen")
