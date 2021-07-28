<template>
  <ul class="bubble-wrapper">
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
    <li class="bubble-item"></li>
  </ul>
</template>

<script>
export default {
  name: 'BubbleUp'
}
</script>

<style scoped lang="less">
.bubble-wrapper {
  position: absolute;
  top: 0;
  left: 0;

  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;

  z-index: -1;
  overflow: hidden;
}

.bubble-item {
  display: block;
  list-style: none;

  position: absolute;
  bottom: -100px;

  border-radius: 100%;
  background-color: rgba(0, 191, 255, 0.2);

  animation: bubble-up linear infinite;
}

.bubble-item::before {
  content: "";
  display: block;

  position: absolute;
  left: 20%;
  top: 20%;

  width: 25%;
  height: 25%;
  border-radius: 100%;
  background-color: rgba(248, 248, 255, 0.4);
}

.bubble-item:nth-child(1) {
  left: 10%;

  width: 80px;
  height: 80px;

  animation-duration: 14s;
  animation-delay: 0s;
}

.bubble-item:nth-child(2) {
  left: 20%;

  width: 60px;
  height: 60px;

  animation-duration: 20s;
  animation-delay: 8s;
}

.bubble-item:nth-child(3) {
  left: 30%;

  width: 70px;
  height: 70px;

  animation-duration: 12s;
  animation-delay: 2s;
}

.bubble-item:nth-child(4) {
  left: 45%;

  width: 90px;
  height: 90px;

  animation-duration: 16s;
  animation-delay: 6s;
}

.bubble-item:nth-child(5) {
  left: 60%;

  width: 70px;
  height: 70px;

  animation-duration: 14s;
  animation-delay: 10s;
}

.bubble-item:nth-child(6) {
  left: 70%;

  width: 50px;
  height: 50px;

  animation-duration: 12s;
  animation-delay: 8s;
}

.bubble-item:nth-child(7) {
  left: 80%;

  width: 90px;
  height: 90px;

  animation-duration: 12s;
  animation-delay: 4s;
}

@keyframes bubble-up {
  0% {
    transform: translateY(0);
    -webkit-transform: translateY(0);
  }
  100% {
    transform: translateY(-2400px);
    -webkit-transform: translateY(-2400px);
  }
}
</style>
