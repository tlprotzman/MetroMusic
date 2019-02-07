# MetroMusic
Algorithmically developed music based around the metropolis algorithm

# About
The Metropolis algorithm is commonly used for generating new configurations of lattice fields,
such as in the case of the Ising model.  It loosely works by making a change to the lattice at 
random and sampling if energy would increase or decrease as a result of the change.  Should it
decrease, the change is accepted unconditionally.  However, if it were to increase, it is accepted
probabilistically based on the current temperature of the system.  I think this can be applied
to music as well.  Notes that fit in to traditional music rules would be associated with low
energy values, and transitions to notes with such patters would be favored.  However, if the 
music is generated at a higher 'temperature', the algorithim would select more unconventional
patterns which could be interesting.
