import time
import urllib
import configparser

import requests
from lxml import etree
import pandas as pd

import logger

logger_name = 'util'
logger_path = 'util.log'
log = logger.get_logger(logger_name, logger_path)

config = configparser.ConfigParser()
config.read('./config.ini', 'utf-8')

entities_file_path = config['data']['entities_file_path']
relation_file_path = config['data']['relation_file_path']

def get_html(entity):
    baseURL = 'https://baike.baidu.com/item/' + urllib.parse.quote(entity)
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url = baseURL, headers = headers)
    return response.text.encode(response.encoding).decode('utf-8')

def get_data(html):
    html = etree.HTML(html)
    relation = html.xpath('//div[@id="slider_relations"]/ul/li/a/div/text()')
    entityTo = html.xpath('//div[@id="slider_relations"]/ul/li/a/div/em/text()')
    return list(zip(relation, entityTo))

def get_triple(entity_list):
    entities = []
    relation = []
    entities_done = set()
    entities_todo = set(entity_list)
    cnt = 0
    while len(entities_todo) != 0:
        cnt = cnt + 1
        log.info('======' + str(cnt) + '=====')
        entity = entities_todo.pop()
        log.info('done: ' + entity)
        entities_done.add(entity)
        try:
            html = get_html(entity)
            entities.append(entity)
            data = get_data(html)
            time.sleep(1)
        except:
            log.info('ERROR')
            continue
        for entityRe, entityTo in data:
            relation.append((entity, entityRe, entityTo))
            if entityTo not in entities_done:
                log.info('todo: ' + entityTo)
                entities_todo.add(entityTo)
    return entities, relation

if __name__ == '__main__':
    entity_list = [
        '李晨', '郑凯', '杨颖', '邓超', '陈赫', '王祖蓝', '王宝强', '包贝尔', '鹿晗', '迪丽热巴', '黄旭熙', '宋雨琦', '朱亚文', '王彦霖', '沙溢', '郭麒麟', '蔡徐坤',
        '周杰伦', '陈奕迅', '林俊杰', '薛之谦', '王力宏', '张学友', '张国荣', '谭咏麟', '李克勤', '林志炫', '李健', '周深', '邓紫棋', '张靓颖', '黄丽玲', '蔡健雅'
    ]
    entities, relation = get_triple(entity_list)
    entities_df = pd.DataFrame(entities, columns = ['entity'])
    relation_df = pd.DataFrame(relation, columns = ['entity', 'relation', 'entityTo'])
    entities_df.insert(0, 'id', ['e' + str(idx + 1) for idx in range(len(entities))], allow_duplicates = False)
    relation_df.insert(0, 'id', ['r' + str(idx + 1) for idx in range(len(relation))], allow_duplicates = False)
    entities_df.to_csv(entities_file_path, index = None)
    relation_df.to_csv(relation_file_path, index = None)