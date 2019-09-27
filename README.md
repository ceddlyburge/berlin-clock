# Berlin Clock Kata

This is some code from a simplified [Berlin Clock Kata](https://mheinzerling.de/blog/code-kata-berlin-clock/) that Max Kort and I did at a [Coding Dojo Meetup](https://www.meetup.com/london-software-craftsmanship/events/264532386/)

I tried hard to represent the domain concepts in the code, here is an excerpt of the top level function.

```python
def get_berlin_clock_text_representation(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))
    
    seconds_row =     get_seconds_row_lights(seconds % 2)
    five_hour_row =   get_row_lights      (time_per_light=5,        value=hours,   light_colour="R", lights_in_row=4)
    one_hour_row =    get_child_row_lights(parent_time_per_light=5, value=hours,   light_colour="R")
    five_minute_row = get_row_lights      (time_per_light=5,        value=minutes, light_colour="Y", lights_in_row=11)
    one_minute_row =  get_child_row_lights(parent_time_per_light=5, value=minutes, light_colour="Y")
```

I think it communicates a reasonable amount of the problem pretty well.

- The clock is made of up rows
- The time is represented by coloured lights in the rows, with each light representing an amount of time
- There are two rows for hours (and minutes), that have a parent / child type relationship
- The seconds row is a special case

Hopefully it is a simple and easy to understand solution.

However, the way it is written leads you to think that other configurations of lights and rows are possible, which is bascially true. You could pass different numbers in to the row functions and get a slightly different clock. However, there are many invalid configurations, that would not be able to represent the full range of times, and there is no help with this. The interpreter won't complain, no exceptions will be thrown, all the types passed in are unconstrained and suchlike. This isn't a problem at the moment, as the requirement was only to implement the Berlin Clock. However, if there became a requirement to support more clocks of a similar style, you would probably start to think about these things.

You might then want to communicate some of the following things

- Parent rows can only have one child row
- Child rows must have the same units (hours / minutes) as their parent 
- The combination of `time_per_light` and `lights_in_row` must be valid for parent rows.

To do this you might create a new class to store the definition of the clock, that could validate in the constructor, or maybe have a separate validate function. You could then pass this object to another class or function to render it as text.