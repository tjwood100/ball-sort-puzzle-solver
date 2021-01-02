# Solver for Ball Sort Puzzle

## What?

A program that will solve "Ball Sort Puzzle" games (such as the ones in [this Android app](https://play.google.com/store/apps/details?id=com.spicags.ballsort&hl=en_GB&gl=US)).

There is also separate program that will generate random puzzles (with the specified number of colours, and specified tube height).
These can be used to test the solver. Random puzzles do not necessarily have a solution.

## Why?

Because I've enjoyed playing these puzzles and I was curious as to how a solver would work.
I don't often write code (for fun, or at work these days) so it's good to challenge yourself occasionally.

## How does it work?

It's a brute force recursive algorithm using depth first search.
That is, it will try a move, see if that solved the puzzle, if not try another move, and so on recursively.
If a dead end is reached (i.e. the puzzle is not solved but no further legal moves are possible) it will backtrack and try a different move.
It remembers each position it has visited before (disregarding the order of the tubes themselves),
and won't make a move that takes it back to a position it has already been in, to avoid going round in circles.
There are a couple of other optimisations but otherwise it's pretty naive.

## How long does it take to run?

That depends on your computer and the size of the puzzle. 14 colours and 4 balls per tube can normally be solved in less than a second.
Could the code be more efficient? Yes, definitely.
It could also be made to run more quickly with a divide and conquer approach to take advantage of parallel processing.

## Requirements

Python 3 - tested on Python 3.8.5 (Ubuntu 20.04).

## How do you run it?

* ballsolver.py solves puzzles
* randomballs.py generates random puzzles

Run either with the -h option for usage intructions. Note the --show-working option for ballsolver if you want to see each move of the solution.

## Format of the JSON file

The JSON file represents the puzzle, either a fresh puzzle, or one that has been partially solved. The JSON must contain a single element called "tubes" which is a two-dimensional array.

The tubes will be assumed to be the same height h as the (length of the) longest tube in the structure.
There can be any number (n) of tubes.
There must be (n-2) colours of ball and h balls of each colour.

Here's an example where n=4 and h=4. The lowest ball in the tube is on the left (index 0), the top ball in the tube on the right (index len-1).
You should make sure you include empty tubes as shown.

Instead of a, b, c etc to represent the colours, you can use any characters (e.g. r, g, b, c, m, y, ...). You could actually use multi-character strings ("red", "green" etc) although currently these won't look right when printed).

```json
{
    "tubes": [
        ["a","b","b","a"],
        ["b","a","a","b"],
        [],
        []
    ]
}
```
