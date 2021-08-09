<template>
  <div class="wrapper">
    <div class="title">知识图谱查询</div>
    <div class="search">
      <input  class="search-box" v-on:keyup.enter="search" v-model.trim="query" ref="searchbox" placeholder="请输入查询项">
      <button class="search-btn" v-on:click="search">搜 索</button>
    </div>
    <BubbleUp />
  </div>
</template>

<script>
import BubbleUp from '@/components/BubbleUp'
export default {
  name: 'Search',
  components: {
    BubbleUp
  },
  data: function () {
    return {
      query: ''
    }
  },
  methods: {
    checkInfo: function () {
      if (this.query === '') {
        return [false, 'searchbox']
      }
      return [true, 'None']
    },
    postData: function () {
      this.$router.push({
        name: 'Result',
        params: {
          query: this.query
        }
      })
    },
    shakeBox: function (elemID) {
      const box = this.$refs[elemID]
      box.classList.add('shake')
      setTimeout(() => { box.classList.remove('shake') }, 800)
    },
    search: function () {
      const checkRes = this.checkInfo()
      if (checkRes[0]) {
        this.postData()
      } else {
        this.shakeBox(checkRes[1])
      }
    }
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

  .search {
    width: 80%;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    .search-box {
      width: 600px;
      height: 45px;
      padding: 5px;
      min-width: 600px;
      min-height: 30px;
      margin-right: 5px;
    }

    .search-box:focus {
      outline: none;
    }

    .search-btn {
      width: 60px;
      height: 45px;
      padding: 5px;
      min-width: 60px;
      min-height: 45px;
      margin-left: 5px;

      border: none;
      background-color: #14b7f4;
    }

    .search-btn:hover {
      color: #ffffff;
      cursor: pointer;

      box-shadow : 1px 1px 8px rgba(255, 255, 255, 0.4) inset;
      text-shadow: 1px 1px 4px rgba(248, 248, 255, 0.4);
    }
  }
}

.shake {
  animation: shake 800ms ease-in-out;
}
@keyframes shake {
  10%, 90% { transform: translate3d(0, -1px, 0); }
  20%, 80% { transform: translate3d(0, +2px, 0); }
  30%, 70% { transform: translate3d(0, -4px, 0); }
  40%, 60% { transform: translate3d(0, +4px, 0); }
  50% { transform: translate3d(0, -4px, 0); }
}
</style>
