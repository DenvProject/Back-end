import json
import os
cur_path = os.path.dirname(__file__)

def get_json_data(json_name : str) -> dict:
    new_path = os.path.join(cur_path, f'../data/{json_name}')
    with open(new_path) as json_data:
        json_data = json.load(json_data)
    return json_data

def handle_gastos_publicos_json():
    result = {}
    gastos_publicos = get_json_data('gastos_publicos.json')
    anos_meses = list(gastos_publicos.keys())
    anos_meses = anos_meses[1:-2]

    for index,un_fed in gastos_publicos['Unidade da Federação'].items():
        result[un_fed] = {}
        result[un_fed]['regiao'] = gastos_publicos['Região'][index]
        result[un_fed]["total"] = gastos_publicos['Total'][index]

        for ano_mes in anos_meses:
            ano,_ = ano_mes.split('/')
            result[un_fed][ano] = result[un_fed].get(ano, []) + [gastos_publicos[ano_mes][index]]

    return result






