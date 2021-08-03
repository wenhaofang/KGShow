<template>
  <div class="kg">
    <div class="bg" v-show="!loading" v-bind:style="size" id="graph"></div>
    <div class="bg" v-show=" loading" v-bind:style="size">Loading ...</div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
export default {
  name: 'KG', // knowledge graph
  props: {
    loading: {
      type: Boolean,
      default: false
    },
    width: {
      type: String, // e.g. 1000px
      require: true
    },
    height: {
      type: String, // e.g. 400px
      require: true
    },
    nodes: {
      type: Array, // [{id: String, name: String, label: String}, ...]
      require: true
    },
    edges: {
      type: Array, // [{id: String, source: String, target: String, relationship: String}, ...]
      require: true
    }
  },
  data: function () {
    return {
      el: null
    }
  },
  computed: {
    size: function () {
      return {
        width: this.width,
        height: this.height
      }
    },
    style: function () {
      const labels = Array.from(new Set(this.nodes.map(val => val.label)))
      const colors = [
        '#DAE3F3', '#FBE5D6', '#EDEDED', '#FFF2CC', '#DEEBF7', '#E2F0D9',
        '#B4C7E7', '#F8CBAD', '#DBDBDB', '#FFE699', '#BDD7EE', '#C5E0B4',
        '#8FAADC', '#F4B183', '#C9C9C9', '#FFD966', '#9DC3E6', '#A9D18E',
        '#FF0000', '#FFC000', '#FFFF00', '#92D050', '#00B050', '#00B0F0', '#0070C0', '#7030A0'
      ]
      const nodeStyle = labels.map((val, idx) => ({
        selector: `node[label = "${val}"]`,
        css: {
          content: 'data(name)',
          'background-color': colors[idx] || '#000000'
        }
      }))
      const edgeStyle = {
        selector: 'edge',
        css: {
          content: 'data(relationship)',
          'line-style': 'solid',
          'line-color': '#DCDCDC',
          'arrow-scale': 1,
          'target-arrow-color': '#DCDCDC',
          'target-arrow-shape': 'triangle',
          'font-size': 10,
          'text-opacity': 0.8,
          'curve-style': 'bezier',
          'control-point-step-size': 20
        }
      }
      return [...nodeStyle, edgeStyle]
    },
    layout: function () {
      const nodeNum = this.nodes.length
      let scale = 1
      if (nodeNum === 0) {
        scale = 1
      } else if (nodeNum <= 5) {
        scale = 2.5
      } else if (nodeNum <= 10) {
        scale = 1.7
      } else if (nodeNum <= 15) {
        scale = 1.2
      } else {
        scale = 1
      }
      return {
        // reference: https://js.cytoscape.org/#layouts
        fit: true,
        name: 'concentric',
        minNodeSpacing: 30,
        spacingFactor: scale,
        animate: true,
        animationDuration: 1000
      }
    }
  },
  watch: {
    nodes: {
      handler: function () {
        this.render()
      },
      deep: true
    },
    edges: {
      handler: function () {
        this.render()
      },
      deep: true
    }
  },
  methods: {
    render: function () {
      const renderX = parseFloat(this.width) / 2
      const renderY = parseFloat(this.height) / 2
      const cy = cytoscape({
        pan: { x: renderX, y: renderY },
        zoom: 1,
        minZoom: 0.1,
        maxZoom: 10,
        container: this.el,
        style: this.style,
        layout: this.layout,
        elements: {
          nodes: this.nodes.map(item => ({ data: item })),
          edges: this.edges.map(item => ({ data: item }))
        }
      })
      const that = this
      cy.nodes().on('click', function () {
        that.nodeClick(this.id())
      })
      cy.edges().on('click', function () {
        that.edgeClick(this.id())
      })
    },
    nodeClick: function (nodeID) {
      this.$emit('nodeClick', nodeID)
    },
    edgeClick: function (edgeID) {
      this.$emit('edgeClick', edgeID)
    }
  },
  mounted: function () {
    this.el = document.getElementById('graph')
    this.render()
  }
}
</script>

<style scoped lang="less">
.bg {
  border: 1px solid black;
  background: white;
  margin: 0;
  padding: 0;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
