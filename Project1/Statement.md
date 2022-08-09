Considering a two-dimensional, incompressible, non-viscous and stationary flow.

We need to determine the velocity vector field u = u(x, y), v = v(x, y), as well as the pathlines.

The differential equation ruling this flow corresponds to a potential flow, id est:

And the velocity components u and v are related to the stream function, id est:

We need to use the finite difference method with the following schemes:

  - Point Gauss-Seidel,
  - Line Gauss-Seidel,
  - Point Succesive Over Relaxation (PSOR), and
  - Line Succesive Over Relaxation (LSOR).
  
For all the schemes we need to guarantee the following values:

We also need to graph the velocity vector field and pathlines for each scheme.
