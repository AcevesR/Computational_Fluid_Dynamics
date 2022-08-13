import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grdsp

# Node number
nx = 26
ny = 26

# Deltas
dx = 0.2
dy = 0.2

# Control Volume size
x_min = 0
y_min = 0
x_max = 5
y_max = 5

# Number of iterations and maximum error allowed
max_error = 0.1
sum = 0
iter = 0

# Coefficients
alpha = dx / dy
beta = (1 / (2 * (1 + alpha ** 2)))

# Boundary Conditions (B. C.)
psi_1 = 0
psi_2 = 100

# Creating vectors 
_X = np.linspace(x_min, x_max, nx)
_Y = np.linspace(y_min, y_max, ny)

# Creating mesh
X, Y = np.meshgrid(_X, _Y)

# Matrix creation
PSI = np.zeros ((ny, nx))
u = np.zeros ((ny, nx))
v = np.zeros ((ny, nx))
error = np.zeros ((ny, nx))

# Using B.C.

## A section
PSI [ : , : 1] = psi_2

## B section
PSI [(ny - 1) : , : ] = psi_2

## C section
PSI [16 : ny, (nx - 1) : ] = psi_2

## D section
PSI [ : 16, (nx - 1) : ] = psi_1

## E section
PSI [ : 1, : 6] = psi_2

## F section
PSI [ : 1, 6 : nx] = psi_1

### Solution

while True:
    for i in range(1, (ny - 1)):
        for j in range(1, (nx - 1)):
            psi = np.copy(PSI)

            # Equation to be solved by finite differences method and Point Gauss-Seidel
            PSI[i, j] = beta * (psi[i + 1][j] + psi[i - 1][j] + (alpha ** 2) * (psi[i][j + 1] + psi[i][j - 1]))

            # u = dpsi / dy; backward
            u[i, j] = ((PSI[i, j] -PSI[i - 1, j]) / dx)

            # v = - dpsi / dx; backward
            v[i, j] = (- (PSI[i, j] -PSI[i, j - 1]) / dy)

            # Error
            error[i, j] = np.absolute(PSI[i, j] - psi[i, j])

    iter += 1
    sum = np.sum(error)

    # Condition to break the loop

    if (sum < max_error):
        print("The error is", format(sum, '.4f'),"at iteration", iter, ".")
        break

# Graph method
cmap = plt.cm.get_cmap("RdYlBu_r")
fig = plt.figure(figsize = (15, 12))
gs = grdsp.GridSpec(nrows = 2, ncols = 2, figure = fig)

streamlines = fig.add_subplot(gs[0, 0])
strm_funct = streamlines.contourf(X, Y, PSI, 100, cmap = cmap)
fig.colorbar(strm_funct)
streamlines.set_title('Stream Function')
streamlines.set_xlabel('x')
streamlines.set_ylabel('y')

vel = fig.add_subplot(gs[0, 1])
strm = vel.streamplot(X, Y, u, v, color = v, linewidth = 2.5, cmap = cmap)
fig.colorbar(strm.lines)
vel.set_title('Velocity components')
vel.set_xlabel('x')
vel.set_ylabel('y')

vect = fig.add_subplot(gs[1, 0])
vect.contourf(X, Y, PSI, 100, cmap = cmap)
vect.quiver(X, Y, u, v)
fig.colorbar(strm_funct)
vect.set_title('Velocity components')
vect.set_xlabel('x')
vect.set_ylabel('y')

plt.show()
