<template>
  <div id="page" style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;">
    <p1 v-if="p1" style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;"></p1>
    <p2 v-if="p2" style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;"></p2>
    <div class="titles" style="font-size: 21px; border-radius: 0">
      基 层 岗 位 可 视 分 析 平 台
    </div>
    <button style="left: 1%; top: 1px; height: 23px" class="select" @click="ffp1">查找</button>
    <button style="left: 6%; top: 1px; height: 23px" class="select" @click="ffp2">推荐</button>
  </div>
</template>


<script>
import p1 from './p1'
import p2 from './p2'

export default {
  name: 'app',
  components: {
    p1, p2
  },
  mounted() {

  },
  data() {
    return {
      p1: 1,
      p2: 0
    }
  },
  methods: {
    ffp1() {
      this.p1 = 1
      this.p2 = 0
    },
    ffp2() {
      this.p1 = 0
      this.p2 = 1
    }
  }
}
</script>

<style scoped>
#page {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  background-color: #bcc;
  color: #000000;
}

.charts {
  position: absolute;
  width: 96%;
  height: 80%;
  left: 2%;
  top: 30px;
  text-align: center;
  font-size: 20%;
  color: #000;
  font-weight: bold;
}

.titles {
  position: absolute;
  width: 100%;
  height: 28px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 15px;
  font-family: 宋体;
  color: #fff;
  background-color: #446699;
  font-weight: bold;


  border-top-right-radius: 15px;
  border-top-left-radius: 15px;

}

.divs {
  position: absolute;
  text-align: center;
  background-color: #eff;
  /*border-radius: 0;*/
  /*border-style: outset;*/
  /*border-width: 2px;*/
  /*border-color: #f9f9f9;*/
  /*box-shadow: #999 0 0 1px 1px;*/
  color: #000;
  opacity: unset;
  z-index: 100;

  border-radius: 15px;
}

.select {
  position: absolute;
  width: 4.5%;
  height: 2.7%;
  background-color: #fff;
  border-color: #eeeeee;
  z-index: 9999;
  font-size: 5px;
  border-radius: 10px;
}

</style>