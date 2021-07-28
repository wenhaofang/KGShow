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
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '100%'
    },
    nodes: {
      type: Array,
      require: true,
      validator: function (array) {
        function typeOf (value) {
          return Object.prototype.toString.call(value).slice(8, -1)
        }
        return array.every(val => {
          return (
            typeOf(val) === 'Object' &&
            typeOf(val.id) === 'String' &&
            typeOf(val.name) === 'String' &&
            typeOf(val.label) === 'String'
          )
        })
      }
    },
    edges: {
      type: Array,
      require: true,
      validator: function (array) {
        function typeOf (value) {
          return Object.prototype.toString.call(value).slice(8, -1)
        }
        return array.every(val => {
          return (
            typeOf(val) === 'Object' &&
            typeOf(val.id) === 'String' &&
            typeOf(val.source) === 'String' &&
            typeOf(val.target) === 'String' &&
            typeOf(val.relationship) === 'String'
          )
        })
      }
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
          'control-point-step-size': 10
        }
      }
      return [...nodeStyle, edgeStyle]
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
      const cy = cytoscape({
        container: this.el,
        style: this.style,
        layout: {
          name: 'random'
        },
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
