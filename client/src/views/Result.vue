<template>
  <div class="wrapper">
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
import { getKGData } from '@/utils/mock'
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
      console.log(nodeID)
    },
    handleEdgeClick: function (edgeID) {
      console.log(edgeID)
    }
  },
  mounted: function () {
    const datas = getKGData()
    this.nodes = datas[0]
    this.edges = datas[1]
    this.loading = false
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
}
</style>
