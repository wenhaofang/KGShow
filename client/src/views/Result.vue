<template>
  <div class="wrapper">
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
      edges: []
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
        this.loading = false
      })
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
  justify-content: center;
  align-items: center;

  .title {
    font-size: 30px;
    font-weight: 500;
    color: #00aaff;
    margin-bottom: 30px;
  }
}
</style>
