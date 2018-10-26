# passwordize
Python script to create random passwords of given length using a Pseudo Random-Number Generator (PRNG) based on a Linear Congruential Number Generator (LCNG) [Lehmer 1949] and on suggestions by J.J. Schneider [Schneider and Kirkpatrick 2006, 32-37] adapted to a 64-bit system. Implemented by Thomas Bukur, November 2013.

Lehmer, D. H. (1949). Mathematical methods in large-scale computing units. In Proc. 2nd Symp. on Large-Scale Digital Calculating Machinery, Cambridge, MA, pages 141-146. Harvard University Press

Schneider, J. J. and Kirkpatrick, S. (2006). Stochastic Optimization. Springer

Usage:
python passwordize.py <length_of_password>
