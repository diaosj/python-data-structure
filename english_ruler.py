"""
Consider how to draw the markings of a typical English ruler.
For each inch, we place a tick with a numeric label. Denote the length of the tick designating a whole inch as the
major tick length. Between the marks for whole inches, the ruler contains a series of minor ticks, placed at intervals
of 1/2 inch, 1/4 inch, and so on. As the size of the interval decreases by half, the tick length decreases by one.
---- 0
-
--
-
---
-
--
-
---- 1
-
--
-
---
-
--
-
---- 2
A 2-inch ruler with major tick length 4.

In general, an interval with a central tick length L>=1 is composed of:
* An interval with a central tick length L-1
* A single tick of length L
* An interval with a central tick length L-1
"""


def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print line


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
