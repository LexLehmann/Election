# Election

This is an implementation of several different voting systems that can be run in tandem on the same set of voting data. The data can have ties in the votes.

the Meek Single Transferable Vote voting system is where this started. Comes with configurable accuracy and precision.

Also includes Borda, Copeland, Purality, Baldwin, Bucklin and Minimax. 

Each System also includes 2 verions of the ordering across all of the candidates. One that is from the concept that the voting system cares about extended into all of the candidates and one that removes the top candidate and runs the algorithm again.

Also has some less serious voting systems like formula one and Reverse Plurality
