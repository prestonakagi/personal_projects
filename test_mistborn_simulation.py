import pytest
from mistborn_simulation import Metalborn, Mistborn, Twinborn, Anchor, AlloSteel, FeroIron, FeroSteel
from projectile_motion_simple import simulate_projectile_motion
from projectile_motion_with_drag import simulate_projectile_motion_with_drag
from projectile_motion_with_drag_and_changing_weight import simulate_projectile_motion_with_drag_and_changing_weight

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
    # expected_speed1 = anchor.anchor_mass / pusher1.body_mass
    assert pusher1.current_speed == pytest.approx(8.9) # expected_speed1 # 8.8710
    assert a_steel.remaining_mass == pytest.approx(0.9)
    
    # test if remaining metal mass will keep decreasing.
    pusher2.burn(a_steel, anchor, radius_for_drag=0.825)
    # expected_speed2 = anchor.anchor_mass / pusher2.body_mass
    assert pusher2.current_speed == pytest.approx(8.9) # expected_speed2 # 8.8710
    assert a_steel.remaining_mass == pytest.approx(0.8)

    pusher3.burn(a_steel, anchor, radius_for_drag=0.825)
    # expected_speed3 = anchor.anchor_mass / pusher3.body_mass
    assert pusher3.current_speed == pytest.approx(8.9) # expected_speed3 # 8.8710
    assert a_steel.remaining_mass == pytest.approx(0.7)  # needed to round floats to one decimal place; otherwise binary approximations yield repeated calculation errors.

    pusher4.burn(a_steel, anchor, radius_for_drag=0.825)
    # expected_speed4 = anchor.anchor_mass / pusher4.body_mass
    assert pusher4.current_speed == pytest.approx(8.9) # expected_speed4 # 8.8710
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


# test_twinborn_store_weight()

# store speed
def test_twinborn_store_speed():
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_steel = FeroSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Steel")
    pusher_runner1 = Twinborn(a_steel, f_steel, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    # TODO: Don't think has_type_of_metal means anything or will be used for Twinborn attributes.
    # body speed potential is default 10.0
    pusher_runner1.store_speed(f_steel) # test default of fraction of 0.1
    assert f_steel.speed_stored == pytest.approx(1.000)
    assert pusher_runner1.body_speed_potential == pytest.approx(9.000)

    # wrong fero metal
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron")
    pusher_runner2 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_runner2.store_speed(f_iron)
    assert f_steel.speed_stored == pytest.approx(1.000) # if hasn't changed
    assert pusher_runner1.body_speed_potential == pytest.approx(9.000) # if hasn't changed

# test_twinborn_store_speed()

def test_use_stored_weight():
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron", weight_stored=1.1)
    pusher_skimmer1 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    
    weight_to_use = pusher_skimmer1.use_stored_weight(f_iron, weight_fraction_to_use=0.2)
    assert f_iron.weight_stored == pytest.approx(0.880)
    assert weight_to_use == pytest.approx(0.220)

    # wrong fero metal
    f_steel = FeroSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Steel")
    pusher_skimmer2 = Twinborn(a_steel, f_steel, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_skimmer2.use_stored_weight(f_steel, weight_fraction_to_use=0.2)
    assert f_iron.weight_stored == pytest.approx(0.880) # if hasn't changed

# test_use_stored_weight()

def test_store_weight_while_jumping():
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron")
    pusher_skimmer1 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    # body weight potential is default 10.0
    weight_storing = pusher_skimmer1.store_weight_while_jumping(f_iron) # test default of fraction of 0.1
    assert f_iron.weight_stored == pytest.approx(1.000)
    assert pusher_skimmer1.body_weight_potential == pytest.approx(9.000)
    assert weight_storing == pytest.approx(-1.000)

    # wrong fero metal
    f_steel = FeroSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Steel")
    pusher_skimmer2 = Twinborn(a_steel, f_steel, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_skimmer2.store_weight_while_jumping(f_steel)
    assert f_iron.weight_stored == pytest.approx(1.000) # if hasn't changed
    assert pusher_skimmer1.body_weight_potential == pytest.approx(9.000) # if hasn't changed

# test_store_weight_while_jumping()

def test_use_stored_speed():
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_steel = FeroSteel(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Steel", speed_stored=1.1)
    pusher_runner1 = Twinborn(a_steel, f_steel, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    
    pusher_runner1.use_stored_speed(f_steel, speed_fraction_to_use=0.3)
    assert pusher_runner1.current_speed == pytest.approx(0.330)
    assert f_steel.speed_stored == pytest.approx(0.770)

    # wrong fero metal
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron", weight_stored=1.1)
    pusher_runner2 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_runner2.use_stored_speed(f_iron, speed_fraction_to_use=0.3)
    assert pusher_runner1.current_speed == pytest.approx(0.330) # if hasn't changed
    assert f_steel.speed_stored == pytest.approx(0.770) # if hasn't changed

# test_use_stored_speed()

def test_simulate_projectile_motion_with_drag():
    """
    As radius increases, drag force increases. If drag too high, object will drop vertically.
    As object's mass increases, drag force does less, so more like simple projectile (with no drag).
    """
    # simulate_projectile_motion_with_drag((165/2), 62.0, 0.0, 45.0)
    # simulate_projectile_motion_with_drag(82.5, 62.0, 0.0, 45.0) # output vertical line going down at x = 0.
    # simulate_projectile_motion_with_drag(82.5, 62.0, 10.0, 45.0) # output is a curve, but max height and distance both 0.00 m and flight time 0.01 seconds.
    # simulate_projectile_motion_with_drag(0.825, 62.0, 10.0, 45.0) # Max Height: 2.44 meters, Total Distance (Range): 9.45 meters, Total Flight Time: 1.41 seconds
    # simulate_projectile_motion_with_drag(0.825, 62.0, 0.0, 45.0) # vertical line going down at x = 0.
    # NOTE: for motion with drag, initial velocity cannot be 0!
    # simulate_projectile_motion_with_drag(0.825, 62.0, 0.0, 90.0) # vertical line going down at x = 0.
    simulate_projectile_motion_with_drag(0.825, 62.0, 10.0, 90.0) # Max Height: 4.85 meters, Total Distance (Range): 0.00 meters, Total Flight Time: 1.99 seconds
        # initial_velocity is technically vector in x and y directions. 90 degrees is about 1.571 radians, cosine of that is zero, so no horizontal movement!

test_simulate_projectile_motion_with_drag()

def test_simulate_projectile_motion_with_drag_and_changing_weight():
    # simulate_projectile_motion_with_drag_and_changing_weight((165/2), 62.0, 0.0, 45.0, 0.05, 1.0) # Error of StopIteration, I think concerning change_time and t_list.
    # simulate_projectile_motion_with_drag_and_changing_weight(82.5, 62.0, 0.0, 45.0, 0.05, 1.0) # Same as line above.
    simulate_projectile_motion_with_drag_and_changing_weight(82.5, 62.0, 10.0, 45.0, 0.05, 1.0) # Error of StopIteration.
    # simulate_projectile_motion_with_drag_and_changing_weight(0.825, 62.0, 10.0, 45.0, 0.05, 1.0) # Max Height: 34.62 meters, Total Distance (Range): 99.54 meters, Total Flight Time: 5.26 seconds
    # simulate_projectile_motion_with_drag_and_changing_weight(0.825, 62.0, 0.0, 45.0, 0.05, 1.0) # With speed_change, the initial velocity of zero does not stay zero, so no vertical line going down at x = 0. Output same as line above.
    # NOTE: for motion with drag, initial velocity cannot be 0!

# test_simulate_projectile_motion_with_drag_and_changing_weight()


def test_jump_and_change_weight_already_stored_weight():
    anchor = Anchor(anchor_mass=550.0, force_angle_degree=45.0)
    a_steel = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")    
    a_steel2 = AlloSteel(initial_mass=1.3, remaining_mass=1.3, name_of_metal_key="Allo Steel")
    f_iron = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron")
    f_iron2 = FeroIron(initial_mass=1.0, remaining_mass=1.0, name_of_metal_key="Fero Iron")
    # pusher_skimmer1 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_skimmer1 = Twinborn(a_steel, f_iron, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=True, want_drag_projectile=True)
    pusher_skimmer2 = Twinborn(a_steel2, f_iron2, initial_speed=0.0, current_speed=0.0, body_mass=62.0, want_simple_projectile=False, want_drag_projectile=True)
    # body weight potential is default 10.0

    pusher_skimmer1.store_weight(f_iron, weight_fraction_to_store=0.2)
    # pusher_skimmer1.jump_and_change_weight(f_iron, anchor, (1.65/2), 0.8, 0.05)
    pusher_skimmer1.burn(a_steel, anchor, (165/2))
    pusher_skimmer2.store_weight(f_iron2, weight_fraction_to_store=0.2)
    pusher_skimmer2.jump_and_change_weight(a_steel2, f_iron2, anchor, (1.65/2), 0.8, 0.05)

# TODO: 05JUL26, jump_and_change_weight NOT showing a plot (like a with drag).
# test_jump_and_change_weight_already_stored_weight()

print("\nEnd testing")