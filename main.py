def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

    return [
        seconds_row_lights(
            seconds % 2),
        parent_row_lights(
            time_per_light=5,
            value=hours, 
            light_colour="R",
            lights_in_row=4),
        child_remainder_row_lights(
            parent_time_per_light=5,
            value=hours,
            light_colour="R"),
        parent_row_lights(
            time_per_light=5,
            value=minutes, 
            light_colour="Y",
            lights_in_row=11),
        child_remainder_row_lights(
            parent_time_per_light=5,
            light_colour="Y",
            value=minutes)
    ]

def seconds_row_lights(seconds):
    return ["Y", "O"][seconds % 2]

def parent_row_lights(
        time_per_light, 
        value, 
        light_colour, 
        lights_in_row):   
    return row_lights(
        light_colour=light_colour, 
        lights_on=value // time_per_light, 
        lights_in_row=lights_in_row)

def child_remainder_row_lights(
        parent_time_per_light, 
        value, 
        light_colour):   
    return row_lights(
        light_colour=light_colour, 
        lights_on=value % parent_time_per_light, 
        lights_in_row=parent_time_per_light - 1)

def row_lights(
        light_colour, 
        lights_on, 
        lights_in_row):
    return light_colour * lights_on + "O" * (lights_in_row - lights_on)

if __name__ == "__main__":
    time = input()
    result = berlin_clock_time(time)
    print ("\n".join(result))

