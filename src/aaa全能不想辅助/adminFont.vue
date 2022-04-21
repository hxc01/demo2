<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0; background-color: #fff">
    <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
      <el-menu-item index="1" @click="fp1">人口预测</el-menu-item>
      <el-menu-item index="2" @click="fp2">医保数据</el-menu-item>
      <el-menu-item index="3" @click="fp3">签约数据</el-menu-item>
      <el-menu-item index="4" @click="fp4">机构信息</el-menu-item>
    </el-menu>

    <admin1 v-if="p1" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></admin1>
    <admin2 v-if="p2" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></admin2>
    <admin3 v-if="p3" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></admin3>
    <!--      <admin4 v-if="p4" style="position: absolute; width: 100%; height: 91.3%; top: 8.7%; left: 0"></admin4>-->
  </div>
</template>

<script>
import admin1 from "./admin1";
import admin2 from "./admin2";
import admin3 from "./admin3";

export default {
  name: 'app',
  components: {
    admin1,
    admin2,
    admin3
  },
  data() {
    return {
      activeIndex: '1',
      p1: 1,
      p2: 0,
      p3: 0,
      p4: 0

    }
  },
  mounted() {

  },
  methods: {
    fp1() {
      this.p1 = 1
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
    },
    fp2() {
      this.p1 = 0
      this.p2 = 1
      this.p3 = 0
      this.p4 = 0
    },
    fp3() {
      this.p1 = 0
      this.p2 = 0
      this.p3 = 1
      this.p4 = 0
    },
    fp4() {
      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 1
    },

  }
}

</script>

<style scoped>
html {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  color: #000
}

.content {
  position: absolute;
  width: 90%;
  height: 80%;
  left: 5%;
  top: 15%;
  text-align: center;
  font-size: 20%;
  color: #fff;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 100%;
  height: 6%;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 20%;
  color: #000;
  font-weight: bold;

}

.divs {
  position: absolute;
  text-align: center;
  background-color: #eff;
  border-radius: 5px;
  border-width: 1px;
  border-style: outset;
  border-color: #cdd;
  opacity: 0.99;
  z-index: 3000;
}

.selects {
  position: absolute;
  width: 5%;
  height: 3%;
  background-color: #eff;
  color: #003;
  font-size: 7px;
  border-radius: 3px;
  border-width: 1px;
  border-style: outset;
  border-color: #cdd;
  text-align: center;
  z-index: 9999;
}
</style>
