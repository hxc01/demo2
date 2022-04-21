<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0; background-color: #fff">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1" @click="fp1">机构选择</el-menu-item>
      <el-menu-item index="2" @click="fp2">评价浏览</el-menu-item>
      <el-menu-item index="3" @click="fp3">健身应用</el-menu-item>
    </el-menu>

    <user1 v-if="p1" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></user1>
    <user2 v-if="p2" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></user2>
    <user3 v-if="p3" style="position: absolute; width: 100%; height: 91.3%; left: 0; top: 8.7%;"></user3>

  </div>
</template>

<script>
import user1 from "./user1";
import user2 from "./user2";
import user3 from "./user3";


export default {
  name: 'app',
  components: {
    user1,
    user2,
    user3
  },
  data() {
    return {
      activeIndex: '1',

      p1: 1,
      p2: 0,
      p3: 0
    }
  },
  mounted() {

  },
  methods: {
    fp1() {
      this.p1 = 1
      this.p2 = 0
      this.p3 = 0
    },
    fp2() {
      this.p1 = 0
      this.p2 = 1
      this.p3 = 0
    },
    fp3(){
      this.p1 = 0
      this.p2 = 0
      this.p3 = 1
    }

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
  background-color: #fff;
  border-radius: 5px;
  border-width: 1px;
  border-style: outset;
  border-color: #ddd;
  opacity: 0.99;
  z-index: 3000;
}

.selects {
  position: absolute;
  width: 5%;
  height: 3%;
  background-color: #eee;
  color: #000;
  font-size: 7px;
  border-radius: 3px;
  border-width: 1px;
  border-style: outset;
  border-color: #ddd;
  text-align: center;
  z-index: 9999;
}
</style>
