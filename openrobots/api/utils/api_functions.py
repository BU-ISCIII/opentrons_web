from openrobots.models import *
from datetime import datetime
from openrobots.openrobots_config import *
def check_valid_date_format (date):
    '''
    Function:
        check if date has the right format
    Return:
        True/False
    '''
    try:
        datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        return True
    except:
        return False

def convert_to_date_format(start_date, finish_date):
    '''
    Function:
        convert the date into datetime object
        If start date has not a valid format it will be set to None
        If finish_date is not valid it will be set to the time now
    Inputs:
        start_date
        finish_date
    Functions:
        check_valid_date_format     # located at this file
    Return:
        formated_date
    '''
    if check_valid_date_format(start_date):
        converted_start_date = datetime.strptime(start_date, '%Y/%m/%d %H:%M:%S')
    else:
        converted_start_date = None
    if check_valid_date_format(finish_date):
        converted_finish_date = datetime.strptime(finish_date, '%Y/%m/%d %H:%M:%S')
    else:
        converted_finish_date = datetime.now()
    return converted_start_date, converted_finish_date

def get_file_mapping_obj_from_protocol_id(protocol_id):
    '''
    Function:
        The function get the file mapping object from the protocol id
    Inputs:
        protocol_id     # protocol id for getting the file mapping
    Return:
        file_mapping_obj. None if not match
    '''
    if FileIDUserRequestMapping.objects.filter(fileID__exact = protocol_id).exists():
        return FileIDUserRequestMapping.objects.filter(fileID__exact = protocol_id).last()
    return None


def get_robot_station(robot_id):
    '''
    Function:
        The function get the station type which robot belongs to
    Inputs:
        robot_id     # robot id to find the station
    Return:
        file_mapping_obj. None if not match
    '''
    if RobotsInventory.objects.filter(robots__exact = robot_id).exists() :
        return RobotsInventory.objects.filter(robots__exact = robot_id).last().get_station_name()
    else:
        return None


def get_station_and_protocol(protocol_id):
    '''
    Function:
        The function get the station number and the prototocol used for the protocol id
    Inputs:
        protocol_id     # protocol id for getting the station and protocol
    Return:
        station_name, protocol_name .None if does not exist
    '''
    if FileIDUserRequestMapping.objects.filter(fileID__exact = protocol_id).exists():
        file_maping_obj = FileIDUserRequestMapping.objects.filter(fileID__exact = protocol_id).last()
        return (file_maping_obj.get_station(), file_maping_obj.get_station_protocol())
    return (None, None)

def store_and_find_changes_parameter_values(parameters, robot_action_obj):
    '''
    Function:
        store the parameters checking if the parameter value was changed from the
        data recorded when protocol file was recorded.
    Inputs:
        parameters      # in the POST request
        robot_action_obj    # object of the robot_action
    Functions:
        check_valid_date_format     # located at this file
    Return:
        True if all parameters remains unchanged. False at least one parameter was changed
    '''
    protocol_id = robot_action_obj.get_protocol_id()
    file_mapping_obj = get_file_mapping_obj_from_protocol_id (protocol_id)
    station , station_protocol = get_station_and_protocol(protocol_id)
    import pdb; pdb.set_trace()
    if station == 'Station C':
        pass
    elif station == 'Station B':
        pass
    elif station == 'Station A':
        if station_protocol == '1':
            if RequestForStationA_Prot1.objects.filter(protocolID__exact = protocol_id).exists():
                req_station_obj = RequestForStationA_Prot1.objects.filter(protocolID__exact = protocol_id).last()
                mapping_variables_dict = dict(MAP_PROTOCOL_PARAMETER_TO_DATABASE_STATION_A_PROT_1)
        elif station_protocol == '2':
            if RequestForStationA_Prot2.objects.filter(protocolID__exact = protocol_id).exists():
                req_station_obj = RequestForStationA_Prot2.objects.filter(protocolID__exact = protocol_id).last()
                mapping_variables_dict = dict(MAP_PROTOCOL_PARAMETER_TO_DATABASE_STATION_A_PROT_2)
        else:
            if RequestForStationA_Prot3.objects.filter(protocolID__exact = protocol_id).exists():
                req_station_obj = RequestForStationA_Prot3.objects.filter(protocolID__exact = protocol_id).last()
                mapping_variables_dict = dict(MAP_PROTOCOL_PARAMETER_TO_DATABASE_STATION_A_PROT_3)
    modified = False
    for par in parameters.keys():
        request_data = {}
        request_data['robotActionPost'] = robot_action_obj
        request_data['protocolFileID'] = file_mapping_obj
        request_data['parameterName'] = par
        request_data['parameterValue'] = parameters[par]
        try:
            ### use the object attribute to get the value
            if str(parameters[par]) ==  str(getattr(req_station_obj, mapping_variables_dict[par])):
                request_data['modified'] = False
            else :
                request_data['modified'] = True
                modified = True
        except:
            request_data['modified'] = True
            modified = True
        new_parameter = ParametersRobotAction.objects.create_parameter(request_data)
    return modified
