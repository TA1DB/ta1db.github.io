from sympy.abc import s
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import pole_zero_plot
tf1 = TransferFunction(s, s**2 + 5*s + 8, s)
pole_zero_plot(tf1)
