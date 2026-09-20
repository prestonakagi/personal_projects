import pytest
from mistborn_simulation_multiple_weight_changes import Metalborn, Mistborn, Twinborn, Anchor, AlloSteel, FeroIron, FeroSteel
from projectile_motion_with_drag_and_multiple_changing_weight import time_projectile_motion_with_drag_and_changing_weight, simulate_projectile_motion_with_drag_and_multiple_changing_weight

def test_simulate_projectile_motion_with_drag_and_multiple_changing_weight():
    # arguments are initial conditions, a.k.a. first of user lists' elements.
    timing_list = time_projectile_motion_with_drag_and_changing_weight(0.855, 62.0, 15.9, 45.0, 0.5425, 1)
    assert timing_list[0] == pytest.approx(2.17) # total flight time
    assert timing_list[1] == pytest.approx(5.80) # max height
    assert timing_list[2] == pytest.approx(22.73) # total distance


test_simulate_projectile_motion_with_drag_and_multiple_changing_weight()