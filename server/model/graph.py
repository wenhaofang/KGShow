import configparser

import pandas as pd

config = configparser.ConfigParser()
config.read('./config.ini', 'utf-8')

entities_file_path = config['data']['entities_file_path']
relation_file_path = config['data']['relation_file_path']

entities_df = pd.read_csv(entities_file_path)
relation_df = pd.read_csv(relation_file_path)

def get_triple(query):
    selectedR = relation_df[
        (relation_df['entity'] == query) |
        (relation_df['entityTo'] == query)
    ]
    entities = (
        set(selectedR['entity'].drop_duplicates().values.tolist()) |
        set(selectedR['entityTo'].drop_duplicates().values.tolist())
    )
    selectedE = entities_df[
        entities_df['entity'].isin(entities)
    ]
    selectedE.insert(selectedE.shape[1], 'label', ['person' for _ in range(selectedE.shape[0])])
    selectedE = selectedE.rename(columns = {'entity': 'name'})
    selectedR = selectedR.rename(columns = {'entity': 'source', 'relation': 'relationship', 'entityTo': 'target'})
    selectedE = selectedE.to_json(orient = 'records', force_ascii = False)
    selectedR = selectedR.to_json(orient = 'records', force_ascii = False)
    return selectedE, selectedR

if __name__ == '__main__':
    entity = entities_df.iloc[0, 1]
    nodes, edges = get_triple(entity)
    print(nodes)
    print(edges)