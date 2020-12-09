import os
dir_path = os.path.dirname(os.path.realpath(__file__))

test = {
    'text' : {
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1,
        'height': 1,
	'max_lines': 3,
	'rand': True,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (0, 0),
        'relative': False,
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Montserrat/Montserrat-SemiBold.ttf'
    }, 
}

three_column_icon_wind_temp_precip = {
    'forecast_location' : { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1,
        'height': 3/32,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (0, 0),
        'relative': False,
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Montserrat/Montserrat-SemiBold.ttf'
    },
    # Column 0
    '000_data_next_1_hours_summary_symbol_code_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 9/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_data_next_1_hours_summary_symbol_code_image', 'forecast_location'],
    },
    '000_data_instant_details_wind_barb_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_data_instant_details_wind_barb_image', '000_data_next_1_hours_summary_symbol_code_image'],
    },
    '000_data_instant_details_wind_speed': {
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_instant_details_wind_barb_image', '000_data_next_1_hours_summary_symbol_code_image'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '000_data_instant_details_air_temperature': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_data_instant_details_air_temperature', '000_data_instant_details_wind_speed'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },

    '000_data_next_1_hours_details_precipitation_amount': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 5/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_data_next_1_hours_details_precipitation_amount', '000_data_instant_details_air_temperature'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '000_forecast_time_local': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 3/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_forecast_time_local', '000_data_next_1_hours_details_precipitation_amount'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Bold.ttf'
    },

    # Column 1
    '006_data_next_1_hours_summary_symbol_code_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 9/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_next_1_hours_summary_symbol_code_image', 'forecast_location'],
    },
    '006_data_instant_details_wind_barb_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_instant_details_wind_speed', '006_data_next_1_hours_summary_symbol_code_image'],
    },
    '006_data_instant_details_wind_speed': {
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['006_data_instant_details_wind_barb_image', '006_data_next_1_hours_summary_symbol_code_image'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '006_data_instant_details_air_temperature': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_instant_details_air_temperature', '006_data_instant_details_wind_speed'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },

    '000_data_next_6_hours_details_precipitation_amount': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 5/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_next_1_hours_details_precipitation_amount', '006_data_instant_details_air_temperature'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '006_forecast_time_local': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 3/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_forecast_time_local', '000_data_next_6_hours_details_precipitation_amount'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Bold.ttf'
    },    
    

    # Column 2
    '012_data_next_1_hours_summary_symbol_code_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 9/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['006_data_next_1_hours_summary_symbol_code_image', 'forecast_location'],
    },
    '012_data_instant_details_wind_barb_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['006_data_instant_details_wind_speed', '012_data_next_1_hours_summary_symbol_code_image'],
    },
    '012_data_instant_details_wind_speed': {
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/6,
        'height': 6/32,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['012_data_instant_details_wind_barb_image', '012_data_next_1_hours_summary_symbol_code_image'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '012_data_instant_details_air_temperature': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 6/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['006_data_instant_details_air_temperature', '012_data_instant_details_wind_speed'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },

    '011_data_next_1_hours_details_precipitation_amount': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 5/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_next_6_hours_details_precipitation_amount', '012_data_instant_details_air_temperature'],
        'max_lines': 2,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '012_forecast_time_local': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/3,
        'height': 3/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['006_forecast_time_local', '011_data_next_1_hours_details_precipitation_amount'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Bold.ttf'
    },    
}

two_column_icon_wind_temp_precip = {
    '000_data_next_1_hours_summary_symbol_code_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/2,
        'height': 15/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, 0),
    },
    '000_data_instant_details_wind_barb_image': { 
        'image': True,
        'inverse': False,
        'padding': 0,
        'width': 1/2,
        'height': 15/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['000_data_instant_details_wind_barb_image', '000_data_next_1_hours_summary_symbol_code_image'],
    },
    'forecast_location': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1,
        'height': 2/32,
        'hcenter': False,
        'vcenter': True,
        'abs_coordinates': (0, None),
        'relative': ['forecast_location', '000_data_instant_details_wind_barb_image'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Montserrat/Montserrat-SemiBold.ttf'
    },
    't_max': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/4,
        'height': 2/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, 0),
        'relative': ['000_data_next_1_hours_summary_symbol_code_image',  't_max'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    't_min': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/4,
        'height': 2/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, 0),
        'relative': ['t_max',  't_min'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '000_data_next_6_hours_details_air_temperature_min': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/4,
        'height': 8/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_next_1_hours_summary_symbol_code_image',  't_max'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '000_data_next_6_hours_details_air_temperature_max': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/4,
        'height': 8/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_next_6_hours_details_air_temperature_min',  't_max'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    't_precipitation': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/2,
        'height': 2/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_instant_details_wind_barb_image',  '000_data_next_6_hours_details_air_temperature_max'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
    '000_data_next_1_hours_details_precipitation_amount': { 
        'image': None,
        'inverse': False,
        'padding': 0,
        'width': 1/2,
        'height': 8/32,
        'hcenter': True,
        'vcenter': True,
        'abs_coordinates': (None, None),
        'relative': ['000_data_instant_details_wind_barb_image',  't_precipitation'],
        'max_lines': 1,
        'font': dir_path+'/../../fonts/Economica/Economica-Regular.ttf'
    },
}

# default layout
layout = three_column_icon_wind_temp_precip
