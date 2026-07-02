import pytest
from mistborn_simulation import Metalborn, Anchor, AlloSteel
from projectile_motion_simple import simulate_projectile_motion

# Unit tests for Metalborn.burn using pytest
# These tests create an Anchor instance before constructing Metalborn instances.

def test_metalborn_burn():
    anchor = Anchor(anchor_mass=550.0, force_angle_degree=45.0)
    a_steel = AlloSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Allo Steel")
    # test all combos of simple and drag Booleans
    pusher1 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=False)
    pusher2 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=False)
    pusher3 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=True)
    pusher4 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)

    pusher1.burn(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    expected_speed1 = anchor.anchor_mass / pusher1.body_mass
    assert pusher1.current_speed == expected_speed1
    assert a_steel.remaining_mass == 0.9
    
    # test if remaining metal mass will keep decreasing.
    pusher2.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed2 = anchor.anchor_mass / pusher2.body_mass
    assert pusher2.current_speed == expected_speed2
    assert a_steel.remaining_mass == 0.8

    pusher3.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed3 = anchor.anchor_mass / pusher3.body_mass
    assert pusher3.current_speed == expected_speed3
    assert a_steel.remaining_mass == 0.7  # TODO: 01JUL26, AssertionError. NEED to round floats to one decimal place; otherwise binary approximations yield repeated calculation errors.

    pusher4.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed4 = anchor.anchor_mass / pusher4.body_mass
    assert pusher4.current_speed == expected_speed4
    assert a_steel.remaining_mass == 0.6

test_metalborn_burn()