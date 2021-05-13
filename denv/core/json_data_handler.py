import json
import os
import pprint 
pp = pprint.PrettyPrinter(indent=4)

cur_path = os.path.dirname(__file__)

def get_json_data(json_name : str) -> dict:
    """
    usando um nome de arquivo, essa função retorna os dados
    lidos do arquivo que deve estar contido no diratório Data
    :param json_name:
    :return: dict
    """
    new_path = os.path.join(cur_path, f'../data/{json_name}')
    with open(new_path) as json_data:
        json_data = json.load(json_data)
    return json_data

def handle_gastos_publicos_json():
    """
    lida com a estrutura do json de gastos_públicos e retorna uma nova estrutura organizada.
    :return: dict
    """
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


def handle_tuberculose_json() -> dict:
    """
    lida com a estrutura do json de dados de tuberculose e retorna uma nova estrutura
    :return: dict
    """

    result = {}

    tuberculose_data = get_json_data('tuberculose_processed.json')

    indices = list(tuberculose_data.keys())
    anos = indices[1: -2]

    for index,un_fed in tuberculose_data['UF de notificacão'].items():
        result[un_fed] = {}
        result[un_fed]['regiao'] = tuberculose_data['Região'][index]
        result[un_fed]["total"] = tuberculose_data['Total'][index]
        result[un_fed]['casos_anuais'] = {}
        for ano in anos:
            result[un_fed]['casos_anuais'][ano] = tuberculose_data[ano][index]
    
    return result



