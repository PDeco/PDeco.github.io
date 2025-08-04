import numpy as np
import scipy as sp
import scipy.integrate


class DynamicSystem:
    def __init__(
        self,
        system_equation: callable,
        initial_state: np.ndarray,
        integration_shceme: str = "RK45",
    ):
        """Args:
        system_equation (callable): Equation defining the dynamics of the
        system i.e. returns the derivative of the input state, often denoted
        y_dot(x1, ..., xn)
        initial_state (ndarray): state in which the system starts in, described
                                 by numerical values in an array format. Must
                                 be of the same dimension as the input desired
                                 by system_equation.
        integration_scheme (string): Default integration scheme to fall back
                                     on if no other is specified. Current
                                     choices are:
                                     - "RK45" (Runge-Kutta 4,5)
        """
        self.system_equation = system_equation
        self.state = initial_state
        self.default_integration_scheme = integration_shceme

    def propagate(
        self, timespan: float, eval_timestamps=None, scheme: str = "None"
    ) -> tuple[np.ndarray, np.ndarray]:
        """Propagate the dynamics forward from the object's current state."""
        # XXX REMEMBER TO RAVEL THE STATE IF IT COMES IN AS 2D AND THE SYSTEM EQUATION LAMBDA EXCPECTS 1D
        if scheme == "None":
            scheme = self.default_integration_scheme

        timespan = [0.0, timespan]  # NOTE currently assumes time independence
        x0 = self.state.ravel()
        sol = scipy.integrate.solve_ivp(
            self.system_equation, timespan, x0, scheme, eval_timestamps
        )
        states = sol.y
        timestamps = sol.t
        return states, timestamps


class Lorenz(DynamicSystem):
    """A dynamic system defined by the lorenz equations"""

    def __init__(self, x0, coefs: list = [10, 28, 2.667], integration_scheme="RK45"):

        self.coefs = coefs

        super().__init__(
            system_equation=self.system_equation,
            initial_state=x0,
        )

    def system_equation(self, t, x):
        a, b, c = self.coefs
        x_dot = a * (x[1] - x[0])
        y_dot = x[0] * (b - x[2]) - x[1]
        z_dot = x[0] * x[1] - c * x[2]
        return np.array([x_dot, y_dot, z_dot])
