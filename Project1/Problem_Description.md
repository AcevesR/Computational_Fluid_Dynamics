Considering a two-dimensional, incompressible, non-viscous and stationary flow.

We need to determine the velocity vector field u = u(x, y), v = v(x, y), as well as the pathlines.

The differential equation ruling this flow corresponds to a potential flow, id est:

d2Phi / dx2 + d2Phi / dy2 = 0

And the velocity components u and v are related to the stream function, id est:

u = dPhi / dy, and v = - dPhi / dx

We need to use the finite difference method with the following schemes:

  - Point Gauss-Seidel,
  - Line Gauss-Seidel,
  - Point Succesive Over Relaxation (PSOR), and
  - Line Succesive Over Relaxation (LSOR).
  
For all the schemes we need to guarantee the following values: 

dx = 0.2,
dy = 0.2,
max error = 0.1

We also need to graph the velocity vector field and stream function for each scheme.