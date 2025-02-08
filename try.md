# Particle in a Box Quantum Mechanical Problem

The particle in a box (also known as the infinite potential well) is a fundamental problem in quantum mechanics that illustrates the quantization of energy levels. It describes a particle free to move in a small space surrounded by impenetrable barriers.

## Problem Setup

Consider a particle of mass \( m \) confined in a one-dimensional box of length \( L \). The potential energy \( V(x) \) is defined as:

$$
V(x) = \begin{cases} 
0 & \text{if } 0 < x < L \\
\infty & \text{otherwise}
\end{cases}
$$

This means the particle can only exist within the region \( 0 < x < L \) and cannot penetrate the walls of the box.

## Schrödinger Equation

The time-independent Schrödinger equation for the particle is:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} + V(x) \psi(x) = E \psi(x)
$$

Within the box, where \( V(x) = 0 \), the equation simplifies to:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} = E \psi(x)
$$

Rearranging, we get:

$$
\frac{d^2 \psi(x)}{dx^2} = -\frac{2mE}{\hbar^2} \psi(x)
$$

Let \( k = \sqrt{\frac{2mE}{\hbar^2}} \), then:

$$
\frac{d^2 \psi(x)}{dx^2} = -k^2 \psi(x)
$$

The general solution to this differential equation is:

$$
\psi(x) = A \sin(kx) + B \cos(kx)
$$

## Boundary Conditions

The boundary conditions are \( \psi(0) = 0 \) and \( \psi(L) = 0 \) because the wavefunction must be zero at the walls of the box.

1. At \( x = 0 \):
   $$
   \psi(0) = A \sin(0) + B \cos(0) = B = 0
   $$

2. At \( x = L \):
   $$
   \psi(L) = A \sin(kL) = 0
   $$

For a non-trivial solution (\( A \neq 0 \)), \( \sin(kL) = 0 \), which implies:

$$
kL = n\pi \quad \text{where } n = 1, 2, 3, \ldots
$$

Thus, \( k = \frac{n\pi}{L} \).

## Quantized Energy Levels

The energy levels are quantized and given by:

$$
E_n = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2}{2m} \left( \frac{n\pi}{L} \right)^2 = \frac{n^2 \pi^2 \hbar^2}{2mL^2}
$$

where \( n \) is a positive integer (quantum number).

## Wavefunctions

The normalized wavefunctions corresponding to these energy levels are:

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left( \frac{n\pi x}{L} \right)
$$

## Summary

The particle in a box problem demonstrates that a particle confined to a finite region of space can only have specific, discrete energy levels. The wavefunctions associated with these energy levels are sinusoidal functions that satisfy the boundary conditions of the problem.