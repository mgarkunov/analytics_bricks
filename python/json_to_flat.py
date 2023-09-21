#%%

def json_flat(in_dict:dict, pref:str='', flat_arr:bool=False) -> dict:
    """
    Функция конвертации многоуровневых JSON / Python dict массивов в плоскую таблицу.  

    Аргументы:
        - in_dict - JSON / Python dict массив для разбора
        - pref - префикс для названий значений
        - flat_arr - преобразование массиов в отдельные поля / столбцы
    """
    
    if not isinstance(in_dict, dict):
        raise Exception("Не верный тип данных для in_dict")
     
    if not isinstance(pref, str):
        raise Exception("Не верный тип данных для pref")

    if not isinstance(flat_arr, bool):
        raise Exception("Не верный тип данных для flat_arr")
    
    out_dict = {}

    def flatten(value, pref:str='', flat_arr:bool=False) -> dict:

        if pref and pref[-1] != '_':
            pref = pref + '_'

        if type(value) is dict:
            for a in value:
                flatten(value[a], pref + a, flat_arr)
        elif type(value) is list and flat_arr == True:
            i = 0
            for a in value:
                flatten(a, pref + str(i), flat_arr)
                i += 1
        else:
            out_dict[pref[:-1]] = value

    flatten(in_dict, pref, flat_arr)
    return out_dict



test_dict = {
    'one_id': 1,
    'one_value': 'test',
    'one_arr': [1,2,3,4],
    'one_dict': {
        'two_id': 10,
        'two_value': 'test',
        'two_arr': [1,2,3,4],
        'two_dict': {
            'three_id': 100,
            'three_value': 'test',
            'three_arr': [1,2,3,4],
            'three_dict': {
                'four_id': 100,
                'four_value': 'test',
                'four_arr': [1,2,3,4]
            }
        }
    }
}

json_flat(
    in_dict=test_dict,
    pref='',
    flat_arr=False
)
