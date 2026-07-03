import pytest
from mistborn_simulation import Metalborn, Mistborn, Twinborn, Anchor, AlloSteel, FeroIron, FeroSteel
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
    assert a_steel.remaining_mass == pytest.approx(0.9)
    
    # test if remaining metal mass will keep decreasing.
    pusher2.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed2 = anchor.anchor_mass / pusher2.body_mass
    assert pusher2.current_speed == expected_speed2
    assert a_steel.remaining_mass == pytest.approx(0.8)

    pusher3.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed3 = anchor.anchor_mass / pusher3.body_mass
    assert pusher3.current_speed == expected_speed3
    assert a_steel.remaining_mass == pytest.approx(0.7)  # needed to round floats to one decimal place; otherwise binary approximations yield repeated calculation errors.

    pusher4.burn(a_steel, anchor, radius_for_drag=0.825)
    expected_speed4 = anchor.anchor_mass / pusher4.body_mass
    assert pusher4.current_speed == expected_speed4
    assert a_steel.remaining_mass == pytest.approx(0.6)

# test_metalborn_burn()

def test_metalborn_flare():
    anchor = Anchor(anchor_mass=550.0, force_angle_degree=45.0)
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    # test all combos of simple and drag Booleans
    pusher1 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=False)
    pusher2 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=False)
    pusher3 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=True)
    pusher4 = Metalborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)

    pusher1.flare(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    expected_speed1 = 5 * anchor.anchor_mass / pusher1.body_mass
    assert pusher1.current_speed == pytest.approx(expected_speed1)
    assert a_steel.remaining_mass == pytest.approx(0.91)

    pusher2.flare(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    expected_speed2 = 5 * anchor.anchor_mass / pusher2.body_mass
    assert pusher2.current_speed == pytest.approx(expected_speed2)
    assert a_steel.remaining_mass == pytest.approx(0.52)

    pusher3.flare(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    expected_speed3 = 5 * anchor.anchor_mass / pusher3.body_mass
    assert pusher3.current_speed == pytest.approx(expected_speed3)
    assert a_steel.remaining_mass == pytest.approx(0.13)

    a_steel.remaining_mass = 1.3
    pusher4.flare(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    expected_speed4 = 5 * anchor.anchor_mass / pusher4.body_mass
    # assert pusher4.current_speed == expected_speed4 # TODO: why assertionError, when a_steel.remaining_mass = 1.3 not at start of block?
    assert pusher4.current_speed == pytest.approx(expected_speed4)
    assert a_steel.remaining_mass == pytest.approx(0.91)
    # assert a_steel.remaining_mass == pytest.approx(-0.26) # TODO: try testing this

# test_metalborn_flare()

def test_mistborn_use_duralumin():
    anchor = Anchor(anchor_mass=550.0, force_angle_degree=45.0)
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    # test all combos of simple and drag Booleans
    pusher1 = Mistborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=False)
    pusher2 = Mistborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=False)
    pusher3 = Mistborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=True)
    pusher4 = Mistborn(initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)

    pusher1.use_duralumin(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    # expected_speed1 = (10 * a_steel.remaining_mass / a_steel.initial_mass) * anchor.anchor_mass / pusher1.body_mass
    assert pusher1.current_speed == pytest.approx(88.7)
    assert a_steel.remaining_mass == pytest.approx(0.0)
    
    a_steel.remaining_mass = 1.0
    pusher2.use_duralumin(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    assert pusher2.current_speed == pytest.approx(68.2)
    assert a_steel.remaining_mass == pytest.approx(0.0)

    a_steel.remaining_mass = 0.85
    pusher3.use_duralumin(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    assert pusher3.current_speed == pytest.approx(58.0)
    assert a_steel.remaining_mass == pytest.approx(0.0)

    a_steel.remaining_mass = 0.05
    pusher4.use_duralumin(a_steel, anchor, radius_for_drag=0.825) # average adult height divided by 2 in meters.
    assert pusher4.current_speed == pytest.approx(3.4)
    assert a_steel.remaining_mass == pytest.approx(0.0)

# test_mistborn_use_duralumin()

# Test Twinborn methods
# store weight
def test_twinborn_store_weight():
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron")
    pusher_skimmer1 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    # TODO: Don't think has_type_of_metal means anything or will be used for Twinborn attributes.
    # body weight potential is default 10.0
    pusher_skimmer1.store_weight(f_iron) # test default of fraction of 0.1
    assert f_iron.weight_stored == pytest.approx(1.000)
    assert pusher_skimmer1.body_weight_potential == pytest.approx(9.000)

    # wrong fero metal
    f_steel = FeroSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Steel")
    pusher_skimmer2 = Twinborn(a_steel, f_steel, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_skimmer2.store_weight(f_steel)
    assert f_iron.weight_stored == pytest.approx(1.000) # if hasn't changed
    assert pusher_skimmer1.body_weight_potential == pytest.approx(9.000) # if hasn't changed


test_twinborn_store_weight()

print("\nEnd testing")