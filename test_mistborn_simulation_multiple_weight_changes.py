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


test_simulate_projectile_motion_with_drag_and_multiple_changing_weight()