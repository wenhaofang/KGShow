<template>
  <div class="wrapper">
    <div class="section">
      <div class="title">知识图谱展示</div>
      <KG
        width="1000px"
        height="400px"
        :nodes="nodes"
        :edges="edges"
        :loading="loading"
        @nodeClick="handleNodeClick"
        @edgeClick="handleEdgeClick"
      />
    </div>
    <div class="section">
      <div class="title">知识表格展示</div>
      <a-table
        style="width:1000px"
        :loading="loading"
        :columns="columns"
        :pagination="pagination"
        :data-source="dataSource"
        :row-selection="{selectedRowKeys: dataSelect, onChange: handleSelect}"
        :rowKey="record => record.index"
      >
        <template v-slot:source="{text}"><div v-html="text"></div></template>
        <template v-slot:target="{text}"><div v-html="text"></div></template>
      </a-table>
      <button class="download" v-on:click="download">下 载</button>
    </div>
  </div>
</template>

<script>
import KG from '@/components/KG'
import { get } from '@/utils/api'
export default {
  name: 'Result',
  components: {
    KG
  },
  data: function () {
    return {
      loading: true,
      nodes: [],
      edges: [],
      dataSelect: [],
      dataOrigin: [],
      columns: [{
        title: '序号',
        dataIndex: 'index',
        key: 'index'
      }, {
        title: '主实体',
        dataIndex: 'source',
        key: 'source',
        slots: { customRender: 'source' }
      }, {
        title: '关系',
        dataIndex: 'relationship',
        key: 'relationship'
      }, {
        title: '从实体',
        dataIndex: 'target',
        key: 'target',
        slots: { customRender: 'target' }
      }],
      pagination: {
        pageSize: 10,
        showSizeChanger: true,
        pageSizeOptions: ['10', '20', '50'],
        showTotal: total => `总共有 ${total} 条数据`,
        showSizeChange: (_, pageSize) => { this.pageSize = pageSize }
      }
    }
  },
  computed: {
    dataSource: function () {
      const dataSource = JSON.parse(JSON.stringify(this.dataOrigin))
      dataSource.forEach(data => {
        data.source = `<a href="https://baike.baidu.com/item/${data.source}" target="_blank">${data.source}</a>`
        data.target = `<a href="https://baike.baidu.com/item/${data.target}" target="_blank">${data.target}</a>`
      })
      return dataSource
    }
  },
  methods: {
    handleNodeClick: function (nodeID) {
      const node = this.nodes.filter(node => node.id === nodeID)[0]
      this.getData(node.name)
    },
    handleEdgeClick: function (edgeID) {
      const edge = this.edges.filter(edge => edge.id === edgeID)[0]
      console.log(edge.relationship)
    },
    getData: function (query) {
      this.loading = true
      get('/graph', {
        query: query
      }).then(res => {
        const data = res.data
        this.nodes = data[0]
        this.edges = data[1]
        const mappingKey = this.nodes.map(node => node.id)
        const mappingVal = this.nodes.map(node => node.name)
        this.dataSelect = [] // clear
        this.dataOrigin = this.edges.map((edge, index) => ({
          index: index + 1,
          source: mappingVal[mappingKey.indexOf(edge.source)],
          relationship: edge.relationship,
          target: mappingVal[mappingKey.indexOf(edge.target)]
        }))
        this.loading = false
      })
    },
    handleSelect: function (selectedRowKeys) {
      this.dataSelect = selectedRowKeys
    },
    format: function (data) {
      return String(data).replace(/"/g, '""').replace(/(^[\s\S]*$)/, '"$1"')
    },
    download: function () {
      const wordSeparator = ','
      const lineSeparator = '\n'
      const reTitle = new Date().getTime().toString() + '.csv'
      const headBOM = '\ufeff'
      const head = this.columns.map(col => col.title)
      const keys = this.columns.map(col => col.dataIndex)
      const data = this.dataSelect.map(idx => keys.map(key => this.dataOrigin[idx - 1][key]))
      const headStr = head ? head.map(item => this.format(item)).join(wordSeparator) + lineSeparator : ''
      const dataStr = data ? data.map(item => item.map(item => this.format(item)).join(wordSeparator)).join(lineSeparator) : ''
      const a = document.createElement('a')
      a.href = 'data:text/csv;charset=utf-8,' + headBOM + encodeURIComponent(headStr + dataStr)
      a.download = reTitle
      a.click()
    }
  },
  mounted: function () {
    const name = this.$route.params.query
    this.getData(name)
  }
}
</script>

<style scoped lang="less">
.wrapper {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;

  .section {
    margin-bottom: 50px;

    .title {
      font-size: 30px;
      font-weight: 500;
      color: #00aaff;
      margin-bottom: 30px;
    }
  }

  .download {
    position: absolute;
    margin-top: -60px;

    width: 60px;
    height: 45px;
    padding: 5px;
    min-width: 60px;
    min-height: 45px;
    margin-left: 5px;

    border: none;
    background-color: #14b7f4;
  }

  .download:hover {
    color: #ffffff;
    cursor: pointer;

    box-shadow : 1px 1px 8px rgba(255, 255, 255, 0.4) inset;
    text-shadow: 1px 1px 4px rgba(248, 248, 255, 0.4);
  }
}
</style>
