function getKGData () {
  const nodes = [{
    id: 'n1',
    name: '李白',
    label: '人物'
  }, {
    id: 'n2',
    name: '杜甫',
    label: '人物'
  }, {
    id: 'n3',
    name: '《静夜思》',
    label: '作品'
  }, {
    id: 'n4',
    name: '《茅屋为秋风所破歌》',
    label: '作品'
  }]
  const edges = [{
    id: 'e1',
    source: 'n1',
    target: 'n2',
    relationship: '李杜'
  }, {
    id: 'e2',
    source: 'n1',
    target: 'n3',
    relationship: '作品'
  }, {
    id: 'e3',
    source: 'n2',
    target: 'n4',
    relationship: '作品'
  }]
  return [nodes, edges]
}

export {
  getKGData
}
