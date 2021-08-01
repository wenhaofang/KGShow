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
  name: '静夜思',
  label: '诗歌'
}, {
  id: 'n4',
  name: '茅屋为秋风所破歌',
  label: '诗歌'
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

async function getKGData (query) {
  const queryNode = nodes.filter(node => node.name === query)[0]
  const queryNodeId = queryNode && queryNode.id
  const selectedEdges = edges.filter(edge => edge.source === queryNodeId || edge.target === queryNodeId)
  const sourceNodeIds = selectedEdges.map(edge => edge.source)
  const targetNodeIds = selectedEdges.map(edge => edge.target)
  const selectedNodeIds = [...sourceNodeIds, ...targetNodeIds]
  const selectedNodes = nodes.filter(node => selectedNodeIds.includes(node.id))
  return [selectedNodes, selectedEdges]
}

export {
  getKGData
}
