import pytest
from mistborn_simulation_multiple_weight_changes import Metalborn, Mistborn, Twinborn, Anchor, AlloSteel, FeroIron, FeroSteel
from projectile_motion_with_drag_and_multiple_changing_weight import time_projectile_motion_with_drag_and_changing_weight, simulate_projectile_motion_with_drag_and_multiple_changing_weight

def test_time_projectile_motion_with_drag_and_multiple_changing_weight():
    # arguments are initial conditions, a.k.a. first of user lists' elements.
    timing_list = time_projectile_motion_with_drag_and_changing_weight(0.855, 62.0, 15.9, 45.0, 0.5425, 1)
    # print(f"{timing_list[2]=}") # to get approx to not throw AssertionError.
    assert timing_list[0] == pytest.approx(2.174) # total flight time
    assert timing_list[1] == pytest.approx(5.80307) # max height
    assert timing_list[2] == pytest.approx(22.7260479) # total distance


# test_time_projectile_motion_with_drag_and_multiple_changing_weight()

def test_simulate_projectile_motion_with_drag_and_multiple_changing_weight():
    # call timing function first
    timing_list = time_projectile_motion_with_drag_and_changing_weight(0.855, 62.0, 15.9, 45.0, 0.5425, 1)
    simulate_projectile_motion_with_drag_and_multiple_changing_weight(0.855, 62.0, 15.9, 45.0, [0.5425, 1.085, 1.6325], [1, 1, 1])


# test_simulate_projectile_motion_with_drag_and_multiple_changing_weight()

def test_jump_and_multiple_times_change_weight():
    anchor = Anchor(anchor_mass=550.0, force_angle_degree=45.0)
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")    
    a_steel2 = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron", weight_stored= 0)
    f_iron2 = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron", weight_stored= 0)
    # pusher_skimmer1 to test use stored weight
    pusher_skimmer1 = Twinborn(a_steel, f_iron, 0.0, 6.999, True, True, body_mass=62.0)
    # pusher_skimmer1 = Twinborn(a_steel, f_iron, 0.0, 17.559, True, True, body_mass=62.0)
    # pusher_skimmer 2 to test store_weight_while_jumping
    pusher_skimmer2 = Twinborn(a_steel2, f_iron2, 0.0, 6.999, True, True, body_mass=62.0)
    # body weight potential is default 100.0

    # pusher_skimmer1 to test using STORED weight while jumping
    # pusher_skimmer1.use_stored_weight(f_iron, weight_fraction_to_store=0.1)
    pusher_skimmer1.store_weight(f_iron, weight_fraction_to_store= 0.1)
    # pusher_skimmer1.jump_and_change_weight(a_steel, f_iron, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= (0.01 / 0.9)) # speed_change is -1.0
    # pusher_skimmer1.jump_and_change_weight(a_steel, f_iron, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= (7 * 0.01 / 0.9)) # speed_change is -7.0
    # pusher_skimmer1.jump_and_multiple_times_change_weight(a_steel, f_iron, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= (0.01 / 0.9)) # speed_change is -1.0
    pusher_skimmer1.jump_and_multiple_times_change_weight(a_steel, f_iron, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= (7 * 0.01 / 0.9)) # speed_change is -7.0

    # pusher_skimmer2 to test STORING weight while jumping
    # to calculate Twinborn.store_weight(..., weight_fraction_to_store= ___) --> ((speed_change / fraction_stored_weight_to_use) - 100) / 100
    pusher_skimmer2.store_weight(f_iron2, weight_fraction_to_store=0.1)
    # pusher_skimmer2.jump_and_change_weight(a_steel2, f_iron2, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= 0.1) # speed_change is 1.0
    # pusher_skimmer2.jump_and_change_weight(a_steel2, f_iron2, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= 0.7) # speed_change is 7.0   
    # pusher_skimmer2.jump_and_multiple_times_change_weight(a_steel2, f_iron2, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= 0.1)    
    pusher_skimmer2.jump_and_multiple_times_change_weight(a_steel2, f_iron2, anchor, time_to_change_weight= 0.5425, fraction_stored_weight_to_use= 0.7)

    # pusher_skimmer3 to test STORING AND USE STORED weight while jumping.