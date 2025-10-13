class parameters:
    def __init__(self):
        # Inertial Parameters
        self.m = 1.0  # mass (kg)
        self.Ixx = 0.0142  # moment of inertia around x-axis (kg*m^2)
        self.Iyy = 0.0142  # moment of inertia around y-axis (kg*m^2)
        self.Izz = 0.0284  # moment of inertia around z-axis (kg*m^2)
        self.S = 0.2589  # wing area (m^2)
        self.J_r = 0.0000075  # rotor moment of inertia (kg*m^2)
        
        # Geometric Parameters
        self.l = 0.3302     # distance from CG to propeller (m)
        self.h = 0.05       #vertical distance parameter (m)
        
        # Physical Constants
        self.g = 9.81       # gravitational acceleration (m/s^2)

        # Aerodynamic coefficients
        self.C_x = 0.1      # drag coefficient in x-direction
        self.C_y = 0.1      # drag coefficient in y-direction
        self.A_c = 0.03          # reference area for drag calculation
        self.rho = 1.225   # air density at sea level (kg/m^3)