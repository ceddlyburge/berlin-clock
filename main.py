def get_berlin_clock_text_representation(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))
    
    seconds_row =     get_seconds_row_lights(seconds % 2)
    five_hour_row =   get_row_lights      (time_per_light=5,        value=hours,   light_colour="R", lights_in_row=4)
    one_hour_row =    get_child_row_lights(parent_time_per_light=5, value=hours,   light_colour="R")
    five_minute_row = get_row_lights      (time_per_light=5,        value=minutes, light_colour="Y", lights_in_row=11)
    one_minute_row =  get_child_row_lights(parent_time_per_light=5, value=minutes, light_colour="Y")
    
    return [
        seconds_row, 
        five_hour_row,
        one_hour_row, 
        five_minute_row, 
        one_minute_row]

def get_seconds_row_lights(seconds):
    return ["Y", "O"][seconds % 2]

def get_row_lights(
        time_per_light, 
        value, 
        light_colour, 
        lights_in_row):   
    return row_lights(
        light_colour=light_colour, 
        lights_on=value // time_per_light, 
        lights_in_row=lights_in_row)

def get_child_row_lights(
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
    result = get_berlin_clock_text_representation(time)
    print ("\n".join(result))

