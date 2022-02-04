from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
from jbi100_app.data import get_range_data


class Stackbar(html.Div):
    def __init__(self, name, param_per_val_name, param_color_name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = param_per_val_name
        self.feature_y = param_color_name

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )



    # to use names instead of values for X axis (from "Road-Safety-Open-Dataset-Data-Guide_modified.xlsx")
    def get_dict_for_param_name(self, param_per_val_name):
         # use 'N/A' as 'not applicable' instead of 'Data missing or out of range'
         # use 'unknown' instead of 'unknown (self reported)'
        if param_per_val_name == 'road_type':
            dict = {'-1': 'N/A', '1': 'Roundabout', '2': 'One way street', '3': 'Dual carriageway', '6': 'Single carriageway', '7': 'Slip Road', '9': 'Unknown', '12': 'One way street/Slip road'}

        elif param_per_val_name == 'day_of_week':
            dict = {'1': 'Sunday', '2': 'Monday', '3': 'Tuesday', '4': 'Wednesday', '5': 'Thursday', '6': 'Friday', '7': 'Saturday'}

        elif param_per_val_name == 'accident_severity' or param_per_val_name == 'casualty_severity':
            dict = {'1': 'Fatal', '2': 'Serious', '3': 'Slight'}

        elif param_per_val_name == 'first_road_class':
            dict = {'1': 'Motorway', '2': 'A(M)', '3': 'A', '4': 'B', '5': 'C', '6': 'Unclassified'}

        elif param_per_val_name == 'speed_limit':
            dict = {'-1': 'N/A', '20': '20', '30': '30', '40': '40', '50': '50', '60': '60', '70': '70', '99': 'unknown'}

        elif param_per_val_name == 'junction_detail':
            dict = {'-1': 'N/A', '0': 'Not at junction or within 20 metres', '1': 'Roundabout', '2': 'Mini-roundabout', '3': 'T or staggered junction', '5': 'Slip road', '6': 'Crossroads', '7': 'More than 4 arms (not roundabout)', '8': 'Private drive or entrance', '9': 'Other junction', '99': 'unknown'}

        elif param_per_val_name == 'junction_control':
            dict = {'-1': 'N/A', '0': 'Not at junction or within 20 metres', '1': 'Authorised person', '2': 'Auto traffic signal', '3': 'Stop sign', '4': 'Give way or uncontrolled', '9': 'unknown'}

        elif param_per_val_name == 'second_road_class':
            dict = {'-1': 'N/A', '0': 'Not at junction or within 20 metres', '1': 'Motorway', '2': 'A(M)', '3': 'A', '4': 'B', '5': 'C', '6': 'Unclassified'}

        elif param_per_val_name == 'pedestrian_crossing_human_control':
            dict = {'-1': 'N/A', '0': 'None within 50 metres', '1': 'Control by school crossing patrol', '2': 'Control by other authorised person', '9': 'unknown'}

        elif param_per_val_name == 'pedestrian_crossing_physical_facilities':
            dict = {'-1': 'N/A', '0': 'No physical crossing facilities within 50 metres', '1': 'Zebra', '4': 'Pelican, puffin, toucan or similar non-junction pedestrian light crossing', '5': 'Pedestrian phase at traffic signal junction', '7': 'Footbridge or subway', '8': 'Central refuge', '9': 'unknown'}

        elif param_per_val_name == 'light_conditions':
            dict = {'-1': 'N/A', '1': 'Daylight', '4': 'Darkness - lights lit', '5': 'Darkness - lights unlit', '6': 'Darkness - no lighting', '7': 'Darkness - lighting unknown'}

        elif param_per_val_name == 'weather_conditions':
            dict = {'-1': 'N/A', '1': 'Fine no high winds', '2': 'Raining no high winds', '3':'Snowing no high winds', '4': 'Fine + high winds', '5': 'Raining + high winds', '6': 'Snowing + high winds', '7': 'Fog or mist', '8': 'Other', '9': 'Unknown'}

        elif param_per_val_name == 'road_surface_conditions':
            dict = {'-1': 'N/A', '1': 'Dry', '2': 'Wet or damp', '3':'Snow', '4': 'Frost or ice', '5': 'Flood over 3cm. deep', '6': 'Oil or diesel', '7': 'Mud', '9': 'unknown'}

        elif param_per_val_name == 'special_conditions_at_site':
            dict = {'-1': 'N/A', '0': 'None', '1': 'Auto traffic signal - out', '2': 'Auto signal part defective', '3':'Road sign or marking defective or obscured', '4': 'Roadworks', '5': 'Road surface defective', '6': 'Oil or diesel', '7': 'Mud', '9': 'unknown'}

        elif param_per_val_name == 'carriageway_hazards':
            dict = {'-1': 'N/A', '0': 'None', '1': 'Vehicle load on road', '2': 'Other object on road', '3':'Previous accident', '4': 'Dog on road', '5': 'Other animal on road', '6': 'Pedestrian in carriageway - not injured', '7': 'Any animal in carriageway (except ridden horse)', '9': 'unknown'}

        elif param_per_val_name == 'urban_or_rural_area':
            dict = {'-1': 'N/A', '1': 'Urban', '2': 'Rural', '3':'Unallocated'}

        elif param_per_val_name == 'did_police_officer_attend_scene_of_accident':
            dict = {'-1': 'N/A', '1': 'Yes', '2': 'No', '3':'No - accident was reported using a self completion  form (self rep only)'}

        elif param_per_val_name == 'trunk_road_flag':
            dict = {'-1': 'N/A', '1': 'Trunk (Roads managed by Highways England)', '2': 'Non-trunk'}

        elif param_per_val_name == 'towing_and_articulation':
            dict = {'-1': 'N/A', '0': 'No tow/articulation', '1': 'Articulated vehicle', '2': 'Double or multiple trailer', '3':'Caravan', '4': 'Single trailer', '5': 'Other tow', '9': 'unknown'}

        elif param_per_val_name == 'vehicle_direction_from' or param_per_val_name == 'vehicle_direction_to':
            dict = {'0': 'Parked', '1': 'North', '2': 'North East', '3':'East', '4': 'South East', '5': 'South East', '6':'South West', '7':'West', '8':'North West', '9': 'unknown'}

        elif param_per_val_name == 'vehicle_location_restricted_lane':
            dict = {'-1': 'N/A', '0': 'On main c\'way - not in restricted lane', '1': 'Tram/Light rail track', '2': 'Bus lane', '3': 'Busway (including guided busway)', '4': 'Cycle lane (on main carriageway)', '5': 'Cycleway or shared use footway (not part of  main carriageway)', '6': 'On lay-by or hard shoulder', '7': 'Entering lay-by or hard shoulder', '8': 'Leaving lay-by or hard shoulder', '9': 'Footway (pavement)', '10': 'Not on carriageway', '99': 'unknown'}

        elif param_per_val_name == 'junction_location':
            dict = {'-1': 'N/A', '0': 'Not at or within 20 metres of junction', '1': 'Approaching junction or waiting/parked at junction approach', '2': 'Cleared junction or waiting/parked at junction exit', '3': 'Leaving roundabout', '4': 'Entering roundabout', '5': 'Leaving main road', '6': 'Entering main road', '7': 'Entering from slip road', '8': 'Mid Junction - on roundabout or on main road', '9': 'unknown'}

        elif param_per_val_name == 'skidding_and_overturning':
            dict = {'-1': 'N/A', '0': 'None', '1': 'Skidded', '2': 'Skidded and overturned', '3': 'Jackknifed', '4': 'Jackknifed and overturned', '5': 'Overturned', '9': 'unknown'}

        elif param_per_val_name == 'hit_object_in_carriageway':
            dict = {'-1': 'N/A', '0': 'None', '1': 'Previous accident', '2': 'Road works', '4': 'Parked vehicle', '5': 'Bridge (roof)', '6': 'Bridge (side)', '7': 'Bollard or refuge', '8': 'Open door of vehicle', '9': 'Central island of roundabout', '10': 'Kerb', '11': 'Other object', '12': 'Any animal (except ridden horse)', '99': 'unknown'}

        elif param_per_val_name == 'vehicle_leaving_carriageway':
            dict = {'-1': 'N/A', '0': 'Did not leave carriageway', '1': 'Nearside', '2': 'Nearside and rebounded', '3': 'Straight ahead at junction', '4': 'Offside on to central reservation', '5': 'Offside on to centrl res + rebounded', '6': 'Offside - crossed central reservation', '7': 'Offside', '8': 'Offside and rebounded', '9': 'unknown'}

        elif param_per_val_name == 'hit_object_off_carriageway':
            dict = {'-1': 'N/A', '0': 'None', '1': 'Road sign or traffic signal', '2': 'Lamp post', '3': 'Telegraph or electricity pole', '4': 'Tree', '5': 'Bus stop or bus shelter', '6': 'Central crash barrier', '7': 'Near/Offside crash barrier', '8': 'Submerged in water', '9': 'Entered ditch', '10': 'Other permanent object', '11': 'Wall or fence', '99': 'unknown'}

        elif param_per_val_name == 'first_point_of_impact':
            dict = {'-1': 'N/A', '0': 'Did not impact', '1': 'Front', '2': 'Back', '3': 'Offside', '4': 'Nearside', '9': 'unknown'}

        elif param_per_val_name == 'vehicle_left_hand_drive':
            dict = {'-1': 'N/A', '1': 'No', '2': 'Yes', '9': 'Unknown'}

        elif param_per_val_name == 'journey_purpose_of_driver':
            dict = {'-1': 'N/A', '1': 'Journey as part of work', '2': 'Commuting to/from work', '3': 'Taking pupil to/from school', '4': 'Pupil riding to/from school', '5': 'Other', '6': 'Not known', '15': 'Other/Not known'}

        elif param_per_val_name == 'sex_of_driver':
            dict = {'-1': 'N/A', '1': 'Male', '2': 'Female', '9': 'Not known'}

        elif param_per_val_name == 'age_band_of_driver' or param_per_val_name == 'age_band_of_casualty':
            dict = {'-1': 'N/A', '1': '0 - 5', '2': '6 - 10', '3': '11 - 15', '4': '16 - 20', '5': '21 - 25', '6': '26 - 35', '7': '36 - 45', '8': '46 - 55', '9': '56 - 65', '10': '66 - 75', '11': 'Over 75'}

        elif param_per_val_name == 'propulsion_code':
            dict = {'-1': 'Undefined', '1': 'Petrol', '2': 'Heavy oil', '3': 'Electric', '4': 'Steam', '5': 'Gas', '6': 'Petrol/Gas (LPG)', '7': 'Gas/Bi-fuel', '8': 'Hybrid electric', '9': 'Gas Diesel', '10': 'New fuel technology', '11': 'Fuel cells', '12': 'Electric diesel'}

        elif param_per_val_name == 'driver_imd_decile' or param_per_val_name == 'casualty_imd_decile':
            dict = {'-1': 'N/A', '1': 'Most deprived 10%', '2': 'More deprived 10-20%', '3': 'More deprived 20-30%', '4': 'More deprived 30-40%', '5': 'More deprived 40-50%', '6': 'Less deprived 40-50%', '7': 'Less deprived 30-40%', '8': 'Less deprived 20-30%', '9': 'Less deprived 10-20%', '10': 'Least deprived 10%'}

        elif param_per_val_name == 'driver_home_area_type' or param_per_val_name == 'casualty_home_area_type':
            dict = {'-1': 'N/A', '1': 'Urban area', '2': 'Small town', '3': 'Rural'}

        elif param_per_val_name == 'casualty_class':
            dict = {'1': 'Driver or rider', '2': 'Passenger', '3': 'Pedestrian'}

        elif param_per_val_name == 'sex_of_casualty':
            dict = {'-1': 'N/A', '1': 'Male', '2': 'Female', '9': 'unknown'}

        elif param_per_val_name == 'pedestrian_location':
            dict = {'-1': 'N/A', '0': 'Not a Pedestrian', '1': 'Crossing on pedestrian crossing facility', '2': 'Crossing in zig-zag approach lines', '3': 'Crossing in zig-zag exit lines', '4': 'Crossing elsewhere within 50m. of pedestrian crossing', '5': 'In carriageway, crossing elsewhere', '6': 'On footway or verge', '7': 'On refuge, central island or central reservation', '8': 'In centre of carriageway - not on refuge, island or central reservation', '9': 'In carriageway, not crossing', '10': 'Unknown or other'}

        elif param_per_val_name == 'pedestrian_movement':
            dict = {'-1': 'N/A', '0': 'Not a Pedestrian', '1': 'Crossing from driver\'s nearside', '2': 'Crossing from nearside - masked by parked or stationary vehicle', '3': 'Crossing from driver\'s offside', '4': 'Crossing from offside - masked by  parked or stationary vehicle', '5': 'In carriageway, stationary - not crossing  (standing or playing)', '6': 'In carriageway, stationary - not crossing  (standing or playing) - masked by parked or stationary vehicle', '7': 'Walking along in carriageway, facing traffic', '8': 'Walking along in carriageway, back to traffic', '9': 'Unknown or other'}

        elif param_per_val_name == 'car_passenger':
            dict = {'-1': 'N/A', '0': 'Not car passenger', '1': 'Front seat passenger', '2': 'Rear seat passenger', '9': 'unknown'}

        elif param_per_val_name == 'bus_or_coach_passenger':
            dict = {'-1': 'N/A', '0': 'Not a bus or coach passenger', '1': 'Boarding', '2': 'Alighting', '3': 'Standing passenger', '4': 'Seated passenger', '9': 'unknown'}

        elif param_per_val_name == 'pedestrian_road_maintenance_worker':
            dict = {'-1': 'N/A', '0': 'No / Not applicable', '1': 'Yes', '2': 'Not Known', '3': 'Probable'}

        else: # use param_per_val values for x
            dict = None

        return dict



    # parameter_per_val_name: variable for X axis parameter
    # parameter_color_name: variable for colors at one value of X axis parameter
    # chosen_date_range - provides two index values in a list (about start date and end date) from 1 to 365 including
    def update(self, param_per_val_name, param_color_name, chosen_date_range):
        param_per_val_name = param_per_val_name.lower().replace(" ", "_")
        param_color_name = param_color_name.lower().replace(" ", "_")

        self.feature_x = param_per_val_name
        self.feature_y = param_color_name

        # Prepare a sorted list with all unique dates from database

        df_date = get_range_data(self.df, chosen_date_range)

        if param_per_val_name != param_color_name:
            # let use dataframe only with 2 input parameters, which have to be with different values
            df = df_date[[param_per_val_name, param_color_name]]
        else:
            df = df_date

        # get list of values for param_per_val_name
        param_per_val = df[param_per_val_name]
        # list with all items, not unique
        param_per_val_list = df[param_per_val_name].tolist()

        param_per_val_unique = param_per_val.unique()

        param_per_val_unique_list = param_per_val_unique.tolist()

        param_per_val_unique_sorted_list = sorted(param_per_val_unique_list)


        # Get globally full list of item values for param_color,
        # because some of these values could be missing for separated row
        g_param_color = df[param_color_name]

        g_param_color_list = df[param_color_name].tolist()

        g_param_color_unique = g_param_color.unique()

        g_param_color_unique_list = g_param_color_unique.tolist()

        g_param_color_unique_sorted_list = sorted(g_param_color_unique_list)


        # Calculates the number of accidents per category

        accident_count = 0
        accident_count_list = []
        accident_count_list_2_full = []
        for x in param_per_val_unique_sorted_list:
            accident_count = param_per_val_list.count(x)
            accident_count_list.append(accident_count)

            df_rows = df.loc[param_per_val == x]

            param_color_list = df_rows[param_color_name].tolist()

            accident_count_3 = 0
            accident_count_list_3 = []

            # check in global full color items list
            for z in g_param_color_unique_sorted_list:
                accident_count_3 = param_color_list.count(z)
                accident_count_list_3.append(accident_count_3)

            # add list of accidents, corresponding to each param_per_val_name
            accident_count_list_2_full.append(accident_count_list_3)


        # prepare list of different(unique) param_color_names to be used
        param_color_list_unique = df[param_color_name].unique().tolist()
        param_color_list_unique_sorted = sorted(param_color_list_unique)
        param_color_string = []
        # convert to string
        for i in param_color_list_unique_sorted:
            param_color_string.append(str(i))


        param_per_val_string = []
        # convert to string
        for i in param_per_val_unique_sorted_list:
            param_per_val_string.append(str(i))


        # to use names (if they are known) instead of values for legend
        dict = self.get_dict_for_param_name(param_color_name)
        if dict == None: # use param_color_string values for legend
            legend_string = param_color_string
        else:
            param_color_string_dict_names = [dict[x] for x in param_color_string]
            legend_string = param_color_string_dict_names


        # to use names (if they are known) instead of values for X axis
        dict = self.get_dict_for_param_name(param_per_val_name)
        if dict == None: # use param_per_val values for X axis
            x_range_string = param_per_val_string
        else:
            param_per_val_string_dict_names = [dict[x] for x in param_per_val_string]
            x_range_string = param_per_val_string_dict_names


        # let use short name of this variable
        acl = accident_count_list_2_full


        dict_stack = {
            param_per_val_name : x_range_string, # x_range_string: call with param_per_val_string in general or special case with road_type_string
            }

        # add dictionary items for each param_per_val_name with full list of related param_color_names
        for x_per_val in acl:

            # i is index of items in x_per_val
            i = 0

            # if the value is real index of color list
            if "-1" in param_color_string:
                ret = dict_stack.get("-1")
                if ret is None:
                    lst = []
                else:
                    lst = ret
                lst.append(x_per_val[i])
                dict_stack.update({ "-1" : lst })
                i += 1

            # get max value of param color list, located at the last positkion of sorted list
            max_i_color = int(param_color_string[len(param_color_string)-1])

            # go until max_i_color including it
            for i_color in range(max_i_color+1):
                # i_color is the number of item in param_color_string,
                # because the values could be not consecutive

                if str(i_color) not in param_color_string:
                    # skipp values, which are missing in param_color_string
                    continue

                ret = dict_stack.get(str(i_color))
                if ret is None:
                    # use empty dictionarry if names are not known
                    lst = []
                else:
                    lst = ret
                lst.append(x_per_val[i])
                dict_stack.update({ str(i_color) : lst })
                i += 1


        self.fig = go.Figure()


        # draw a bar
        for i in range(len(param_color_string)):
            # add a serie for corresponding (i) color value
            self.fig.add_trace(go.Bar(
                x=x_range_string,
                y=dict_stack.get(param_color_string[i]),
                name=legend_string[i],
            ))


        # add a title, update axis titles, make the bar stacked, show legend
        self.fig.update_layout(
            title="Number of Accidents per '" + param_per_val_name + "' and '" + param_color_name + "'",
            xaxis_title=self.feature_x,
            yaxis_title="number_of_accidents",
            barmode="stack",
            showlegend=True,
            legend_title_text=self.feature_y,
        )

        return self.fig
