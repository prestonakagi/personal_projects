# Module for simple projectile motion 
# from personal_projects.projectile_motion_simple import simulate_projectile_motion
from projectile_motion_simple import simulate_projectile_motion
# Module for projectile motion with (large) quadratic drag. Euler-Cromer numerical method 
# from personal_projects.projectile_motion_with_drag import simulate_projectile_motion_with_drag
from projectile_motion_with_drag import simulate_projectile_motion_with_drag

# For each module, code as function, and comments on each equation and what each parameter means (with units!). Also a variable for each equation parameter. 
# Maybe make Classes for metallic object, Mistborn, Feruchemist, Twinborn.
# Maybe PyMunk for physics stuff0.1


# dictionaries of metal:power (short summary) for Mistborn and Ferochemist.
# dictionary of interesting Twinborn permutations of key of Allumantic metal then Ferruchemic metal and value of string description of what could do.

# Maybe only simulate Allo steel, Allo iron, Allo duralumin with one of the two other metals, Twin Crasher (Allo Steel, Fer iron), Twin Steel both (but no Compounding!), Twin Allo iron Fer Steel, Twin iron both.

# For rioting Allo zinc and soothing Allo brass, decrease or increase probability for a choice to be successful. 
# Flaring metal is a multiplier.
# need total or running total mass of metal ingested/stored so duralumon works. As burn or flare metal, running total decreases.

# Simulate graph 2D (vertical and horizontal) flight, both simple and with drag.
#-------------------------------------------------------

# dictionary of Type_and_Metal:description_ of_power. Allo steel, Allo iron, Allo duralumin with one of the two other metals, Twin Crasher (Allo Steel, Fer iron), Twin Steel both (but no Compounding!), Twin Allo iron Fer Steel, Twin iron both.
metal_and_powers_dictionary = {"Allo Steel":"Pushes on nearby sources of metal",
                               "Fero Steel":"Stores physical speed",
                               "Allo Iron":"Pulls on nearby sources of metal",
                               "Fero Iron":"Stores physical weight",
                               "Allo Duralumin":"Quickly burns any remaining mass of a metal"
                               }

# Make Classes of Mistborn and Twinborn.
class Metalborn:
    """
    Assume anchor for pushing is straight behind the Metalborn, and anchor for pulling is straight in front. 
    """
    # The initializer method (constructor) to set up properties
    def __init__(self, initial_speed, current_speed, body_mass=62.0, position_x=0.0, position_y=0.0, want_simple_projectile=True, want_drag_projectile=False):
        self.initial_speed = initial_speed   # Instance attribute 
        self.current_speed = current_speed
        self.body_mass = body_mass
        self.position_x = position_x      # Instance attribute that has default 
        self.position_y = position_y
        self.want_simple_projectile = want_simple_projectile
        self.want_drag_projectile = want_drag_projectile

    def burn(self, type_of_metal_instance, anchor_instance, radius_for_drag):
        """
        Uses set amount of remaining_mass of specific metal to set initial condition for one flight ("bounce") and updates instance's metal' remaining_mass.
        Then simulates a graph of trajectory of either a simple projectile or projectile with drag or both.
        """
        # use a fraction of metal's remaining mass. Subtract by one tenth of initial mass.
        # burn multiplier is 1
        # Then multiply burn multiplier to anchor mass to Metalborn body mass ratio and add to current speed.
        if type_of_metal_instance.remaining_mass < 0.1 * type_of_metal_instance.initial_mass:
            print(f"You are out of {type_of_metal_instance.name_of_metal}!")
        elif type_of_metal_instance.remaining_mass == 0.1 * type_of_metal_instance.initial_mass:
            print(f"Last jump!")
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after first jump or already increased speed
                self.current_speed += (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.1 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)
        elif type_of_metal_instance.remaining_mass > 0.1 * type_of_metal_instance.initial_mass:
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after already increased speed
                self.current_speed += (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            # update remaining mass of metal instance
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.1 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)

        # Run projectile functions
        # run the simple projectile function
        if self.want_simple_projectile == True and self.want_drag_projectile == False:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
        # run the drag projectile function
        elif self.want_simple_projectile == False and self.want_drag_projectile == True:
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        # run both simple and then drag projectile functions
        elif self.want_simple_projectile == True and self.want_drag_projectile == True:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        else:
            print(f"Can't do neither simple and drag projectile!")

    def flare(self, type_of_metal_instance, anchor_instance, radius_for_drag):
        """
        Almost the same as burn(), but flare() multiplies metal usage and speed increase by 3 and 5, respectively.
        Uses set amount of remaining_mass of specific metal to set initial condition for one flight ("bounce") and updates instance's metal' remaining_mass.
        Then simulates a graph of trajectory of either a simple projectile or projectile with drag or both.
        """
        # use a fraction of metal's remaining mass. Subtract by three tenths of initial mass.
        # flare multiplier is 5
        # Then multiply burn multiplier to anchor mass to Metalborn body mass ratio and add to current speed.
        if type_of_metal_instance.remaining_mass < 0.3 * type_of_metal_instance.initial_mass:
            print(f"You are out of {type_of_metal_instance.name_of_metal}!")
        elif type_of_metal_instance.remaining_mass == 0.3 * type_of_metal_instance.initial_mass:
            print(f"Last jump!")
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after first jump or already increased speed
                self.current_speed += (5 / 1 *(0.3 * type_of_metal_instance.remaining_mass))
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.3 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)
        elif type_of_metal_instance.remaining_mass > 0.3 * type_of_metal_instance.initial_mass:
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after already increased speed
                self.current_speed += (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.3 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)

        # Run projectile functions
        # run the simple projectile function
        if self.want_simple_projectile == True and self.want_drag_projectile == False:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
        # run the drag projectile function
        elif self.want_simple_projectile == False and self.want_drag_projectile == True:
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        # run both simple and then drag projectile functions
        elif self.want_simple_projectile == True and self.want_drag_projectile == True:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        else:
            print(f"Can't do neither simple and drag projectile!")

"""
The Rule for Arguments
When organizing parameters in the child class constructor (__init__), follow this exact order: 
Child positional arguments (no default)
Parent positional arguments (no default)
Parent default arguments
Child default arguments
"""

class Mistborn(Metalborn):
    # inherits all parent's (Metalborn's) attributes, by not listing any attribute for Mistborn class.
    
    def use_duralumin(self, type_of_metal_instance, anchor_instance, radius_for_drag):
        """
        Almost the same as burn(), but this uses all remaining mass of metal and speed increases by 10.
        Uses to set initial condition for one flight ("bounce") and updates instance's metal' remaining_mass.
        Then simulates a graph of trajectory of either a simple projectile or projectile with drag or both.
        """
        # uses all of metal's remaining mass.
        # flare multiplier is 10 times ratio of remaining metal mass to initial metal mass
        # Then multiply flare multiplier to anchor mass to Metalborn body mass ratio and add to current speed.
        
        if type_of_metal_instance.remaining_mass <= 0:
            print(f"You are out of {type_of_metal_instance.name_of_metal}!")
        elif type_of_metal_instance.remaining_mass > 0:
            self.current_speed = self.current_speed + ((10 * type_of_metal_instance.remaining_mass / type_of_metal_instance.initial_mass) * anchor_instance.anchor_mass / self.body_mass)
            self.current_speed = round(self.current_speed, 1)

        type_of_metal_instance.remaining_mass = 0.0

        # Run projectile functions
        # run the simple projectile function
        if self.want_simple_projectile == True and self.want_drag_projectile == False:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
        # run the drag projectile function
        elif self.want_simple_projectile == False and self.want_drag_projectile == True:
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        # run both simple and then drag projectile functions
        elif self.want_simple_projectile == True and self.want_drag_projectile == True:
            simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
            simulate_projectile_motion_with_drag(radius_for_drag, self.body_mass, self.current_speed, anchor_instance.force_angle_degree)
        else:
            print(f"Can't do neither simple and drag projectile!")

class Twinborn(Metalborn):
    def __init__(self, metal_allo_instance, metal_fero_instance, initial_speed, current_speed, body_mass=62.0, position_x=0.0, position_y=0.0, want_simple_projectile=True, want_drag_projectile=False, has_stored_weight=False, has_stored_speed=False, body_speed_potential=10.0, body_weight_potential=10.0):
        # super() calls the Parent's __init__ to inherit Parent's specified attributes
        super().__init__(initial_speed, current_speed, body_mass=62.0, position_x=0.0, position_y=0.0, want_simple_projectile=True, want_drag_projectile=False)
        self.has_stored_weight = has_stored_weight
        self.has_stored_speed = has_stored_speed
        self.body_speed_potential = body_speed_potential
        self.body_weight_potential = body_weight_potential

    def store_weight(self, metal_fero_instance, weight_fraction_to_store=0.1):
        # check if metal_fero_instance is an instance of FeroIron
        if isinstance(metal_fero_instance, FeroIron):
            # store weight in FeroIron instance, then subtract fraction from Twinborn body_weight_potential.
            metal_fero_instance.weight_stored += self.body_weight_potential * weight_fraction_to_store
            metal_fero_instance.weight_stored = round(metal_fero_instance.weight_stored, 3)
            self.body_weight_potential = self.body_weight_potential - (self.body_weight_potential * weight_fraction_to_store)
            self.body_weight_potential = round(self.body_weight_potential, 3)
            self.has_stored_weight = True
        else:
            print(f"The fero metal instance is not FeroIron!")

    def use_stored_weight(self, metal_fero_instance, weight_fraction_to_use=0.1):
        """
        Updates metal instance's weight stored attribute.
        Returns fraction of weight stored (to be used to add to Twinborn's current speed).
        """
        # check if metal_fero_instance is an instance of FeroIron
        if isinstance(metal_fero_instance, FeroIron):
            # take stored weight (float) in FeroIron instance and add to self.current_speed.
            stored_weight_to_use = metal_fero_instance.weight_stored * weight_fraction_to_use
            stored_weight_to_use = round(self.current_speed, 3)
            # subtract fraction from metal weight stored
            metal_fero_instance.weight_stored -= metal_fero_instance.weight_stored * weight_fraction_to_use
            if metal_fero_instance.weight_stored <= 0.0:
                self.has_stored_weight = False
                metal_fero_instance.weight_stored = 0.0 # make sure any negative value reset to zero.
            else: pass
            return stored_weight_to_use
        else:
            print(f"The fero metal instance is not FeroIron!")

    def store_weight_while_jumping(self, metal_fero_instance, weight_fraction_to_store=0.1):
        """
        Updates metal instance's weight stored attribute and subtracts from self body weight potential.
        Returns fraction of weight stored (to be used to add to Twinborn's current speed) as a negative float.
        """
        # check if metal_fero_instance is an instance of FeroIron
        if isinstance(metal_fero_instance, FeroIron):
            storing_weight_fraction = self.body_weight_potential * weight_fraction_to_store
            storing_weight_fraction = round(metal_fero_instance.weight_stored, 3)
            # store weight in FeroIron instance, then subtract fraction from Twinborn body_weight_potential.
            metal_fero_instance.weight_stored += storing_weight_fraction
            metal_fero_instance.weight_stored = round(metal_fero_instance.weight_stored, 3)
            self.body_weight_potential = self.body_weight_potential - storing_weight_fraction
            self.body_weight_potential = round(self.body_weight_potential, 3)
            self.has_stored_weight = True
            return (-1 * storing_weight_fraction)
        else:
            print(f"The fero metal instance is not FeroIron!")\

    def store_speed(self, metal_fero_instance, speed_fraction_to_store=0.1):
        # check if metal_fero_instance is an instance of FeroSteel
        if isinstance(metal_fero_instance, FeroSteel):
            # store speed in FeroSteel instance, then subtract fraction from Twinborn body_speed_potential.
            metal_fero_instance.speed_stored += self.body_speed_potential * speed_fraction_to_store
            metal_fero_instance.speed_stored = round(metal_fero_instance.speed_stored, 1)
            self.body_speed_potential = self.body_speed_potential - (self.body_speed_potential * speed_fraction_to_store)
            self.body_speed_potential = round(self.body_speed_potential, 3)
            self.has_stored_speed = True
        else:
            print(f"The fero metal instance is not FeroSteel!")        

    def use_stored_speed(self, metal_fero_instance, speed_fraction_to_use=0.1):
        # check if metal_fero_instance is an instance of FeroSteel
        if isinstance(metal_fero_instance, FeroSteel):
            # take stored speed in FeroSteel instance and add to self.current_speed.
            self.current_speed += metal_fero_instance.speed_stored * speed_fraction_to_use
            self.current_speed = round(self.current_speed, 3)
            # subtract fraction from metal speed stored
            metal_fero_instance.speed_stored -= metal_fero_instance.speed_stored * speed_fraction_to_use
            if metal_fero_instance.speed_stored <= 0.0:
                self.has_stored_speed = False
                metal_fero_instance.speed_stored = 0.0 # make sure any negative value reset to zero.
            else: pass
        else:
            print(f"The fero metal instance is not FeroSteel!") 

    def burn_for_Twinborn(self, type_of_metal_instance, anchor_instance):
        """
        Uses set amount of remaining_mass of specific metal to set initial condition for one flight ("bounce") and updates instance's metal' remaining_mass.
        Then simulates a graph of trajectory of either a simple projectile or projectile with drag or both.
        """
        # use a fraction of metal's remaining mass. Subtract by one tenth of initial mass.
        # burn multiplier is 1
        # Then multiply burn multiplier to anchor mass to Metalborn body mass ratio and add to current speed.
        if type_of_metal_instance.remaining_mass < 0.1 * type_of_metal_instance.initial_mass:
            print(f"You are out of {type_of_metal_instance.name_of_metal}!")
        elif type_of_metal_instance.remaining_mass == 0.1 * type_of_metal_instance.initial_mass:
            print(f"Last jump!")
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after first jump or already increased speed
                self.current_speed += (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.1 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)
        elif type_of_metal_instance.remaining_mass > 0.1 * type_of_metal_instance.initial_mass:
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after already increased speed
                self.current_speed += (1 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            # update remaining mass of metal instance
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.1 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)

    def flare_for_Twinborn(self, type_of_metal_instance, anchor_instance):
        """
        Almost the same as burn(), but flare() multiplies metal usage and speed increase by 3 and 5, respectively.
        Uses set amount of remaining_mass of specific metal to set initial condition for one flight ("bounce") and updates instance's metal' remaining_mass.
        Then simulates a graph of trajectory of either a simple projectile or projectile with drag or both.
        """
        # use a fraction of metal's remaining mass. Subtract by three tenths of initial mass.
        # flare multiplier is 5
        # Then multiply burn multiplier to anchor mass to Metalborn body mass ratio and add to current speed.
        if type_of_metal_instance.remaining_mass < 0.3 * type_of_metal_instance.initial_mass:
            print(f"You are out of {type_of_metal_instance.name_of_metal}!")
        elif type_of_metal_instance.remaining_mass == 0.3 * type_of_metal_instance.initial_mass:
            print(f"Last jump!")
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after first jump or already increased speed
                self.current_speed += (5 / 1 *(0.3 * type_of_metal_instance.remaining_mass))
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.3 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)
        elif type_of_metal_instance.remaining_mass > 0.3 * type_of_metal_instance.initial_mass:
            if self.current_speed == self.initial_speed:
                self.current_speed = self.initial_speed + (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            else: # for after already increased speed
                self.current_speed += (5 * anchor_instance.anchor_mass / self.body_mass)
                self.current_speed = round(self.current_speed, 1)
            type_of_metal_instance.remaining_mass = type_of_metal_instance.remaining_mass - (0.3 * type_of_metal_instance.initial_mass)
            type_of_metal_instance.remaining_mass = round(type_of_metal_instance.remaining_mass, 1)

    # use burn and/or flare method(s) after use store method then use_stored___ method.
    # make jump method that gives user input option to use stored weight during a jump with drag (at a specific time)
    def jump_and_change_weight(self, type_of_metal_instance, anchor_instance, radius_for_drag, fraction_stored_weight_to_use):
        ways_to_jump = ['burn', 'flare']
        if self.has_stored_weight:
            jump_type = ""
            while jump_type.lower() not in ways_to_jump:
                jump_type = input(f"Do you want to burn or flare to jump? ")
                if jump_type.lower() == "burn":
                    self.burn_for_Twinborn(type_of_metal_instance, anchor_instance)
                elif jump_type.lower() == "flare":
                    self.flare_for_Twinborn(type_of_metal_instance, anchor_instance)
                else: 
                    print(f"Need to enter the word burn or the word flare!")
                    jump_type = input(f"Do you want to burn or flare to jump? ")

            # make a variable to store speed change to use as arguement in the projectile drag weight function
            stored_weight_to_speed = self.use_stored_weight(type_of_metal_instance, fraction_stored_weight_to_use)
            #weight_being_stored_to_speed = self.  TODO: make a store weight while jumping method.
            if self.want_drag_projectile == True and self.want_simple_projectile == False:



                pass
            elif self.want_drag_projectile == False and self.want_simple_projectile == True:
                simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
            elif self.want_drag_projectile == True and self.want_simple_projectile == True:
                simulate_projectile_motion(self.current_speed, anchor_instance.force_angle_degree)
                #TODO: the complicated jump here
            else:
                print(f"Can't do neither simple and drag projectile!")
        else:
            print(f"\nYou have not stored any weight yet. First store some weight and then jump again.")

# Make Parent Class of Metal and Child Classes of each type_and_metal.
class Metal:
    # The initializer method (constructor) to set up properties
    def __init__(self, initial_mass, remaining_mass, name_of_metal_key):
        # name_of_metal_key is string of the name of the metal
        self.initial_mass = initial_mass
        self.remaining_mass = remaining_mass
        self.name_of_metal = name_of_metal_key
        self.power_description = metal_and_powers_dictionary[name_of_metal_key]

"""
To use super() in a child class when the parent class has multiple attributes, 
you must pass all required parent arguments into super().__init__() inside 
the child's constructor, and then define the child's unique attributes.
"""
class FeroSteel(Metal):
    def __init__(self, initial_mass, remaining_mass, name_of_metal_key, speed_stored=0.0):
        # 1. Forward the required attributes to the parent constructor
        super().__init__(initial_mass, remaining_mass, name_of_metal_key)

        # 2. Initialize the child-specific attributes
        self.speed_stored = speed_stored

class FeroIron(Metal):
    def __init__(self, initial_mass, remaining_mass, name_of_metal_key, weight_stored=0.0):
        # 1. Forward the required attributes to the parent constructor
        super().__init__(initial_mass, remaining_mass, name_of_metal_key)

        # 2. Initialize the child-specific attributes
        self.weight_stored = weight_stored

class AlloSteel(Metal):
    pass

class AlloIron(Metal):
    pass

# Anchor class
class Anchor:
    def __init__(self, anchor_mass=550.0, force_angle_degree=45.0):
        self.anchor_mass = anchor_mass
        self.force_angle_degree = force_angle_degree

# Make one instance of each class. Metals first.
# a_steel = AlloSteel(1.0, )
# kal = Mistborn(0.0, 0.0)
# wax = Twinborn(0.0, 0.0, has_allo_steel=True, has_fero_iron=True)
# wax_but_pull = Twinborn(0.0, 0.0, has_allo_iron=True, has_fero_iron=True)
# runner_push = Twinborn(0.0, 0.0, has_fero_steel=True, has_allo_steel=True)
# runner_pull = Twinborn(0.0, 0.0, has_fero_steel=True, has_allo_iron=True)

# Allo steel set initial conditions, then show graph simulation

# Allo iron set initial conditions, then show graph simulation 

# Twin Crasher (Allo Steel, Fer iron) set initial conditions, then show graph simulation

# Twin iron both set initial conditions, then show graph simulation

# Twin steel both set initial conditions, then show graph simulation

# Twin Allo iron Fer steel set initial conditions, then show graph simulation


#---------------------------------------

# Simple projectile motion
# multi line comment of equations and parameters and explanations of both (each)

"""
Initial velocity m/s
Launch angle theta degrees input but convert to radians
Gravity acceleration 9.81 m/s²

"""

if __name__ == "__main__": # use for module
    pass