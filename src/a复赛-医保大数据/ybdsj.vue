<template>
  <dv-border-box-11
      style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #eff"
      title="医保大数据可视化平台"
      :color="['#0bd', '#09d']">

    <ybdsjp1 v-show="p1"></ybdsjp1>
    <ybdsjp2 v-show="p2"></ybdsjp2>
    <ybdsjp3 v-show="p3"></ybdsjp3>
    <ybdsjp4 v-show="p4"></ybdsjp4>
    <ybdsjp5 v-show="p5"></ybdsjp5>
    <ybdsjp6 v-show="p6"></ybdsjp6>


    <button id="b1" @click="fp1" class="selects" style="left: 30%; top: 8%;">属性分析</button>
    <button id="b2" @click="fp2" class="selects" style="left: 35%; top: 8%; ">政策分析</button>
    <button id="b3" @click="fp3" class="selects" style="left: 40%; top: 8%; ">民生分析</button>
    <button id="b4" @click="fp4" class="selects" style="left: 60%; top: 8%; ">趋势发展</button>
    <button id="b5" @click="fp5" class="selects" style="left: 65%; top: 8%; color: #eff; background-color: #09d;" >病症分析
    </button>
    <button id="b6" @click="fp6" class="selects" style="left: 70%; top: 8%; ">信息管理
    </button>

  </dv-border-box-11>
</template>

<script>
import ybdsjp1 from "@/a复赛-医保大数据/ybdsjp1";
import ybdsjp2 from "@/a复赛-医保大数据/ybdsjp2";
import ybdsjp3 from "@/a复赛-医保大数据/ybdsjp3";
import ybdsjp4 from "@/a复赛-医保大数据/ybdsjp4";
import ybdsjp5 from "@/a复赛-医保大数据/ybdsjp5";
import ybdsjp6 from "@/a复赛-医保大数据/ybdsjp6";


export default {
  name: 'app',
  components: {
    ybdsjp1,
    ybdsjp2,
    ybdsjp3,
    ybdsjp4,
    ybdsjp5,
    ybdsjp6
  },
  data() {
    return {
      p1: 0,
      p2: 0,
      p3: 0,
      p4: 0,
      p5: 1,
      p6: 0
    }
  },
  mounted() {


  },
  methods: {
    buttonSelecting(id) {
      document.getElementById(id).style.backgroundColor = '#09d'
      document.getElementById(id).style.color = '#eff'
    },
    buttonSelected(id) {
      document.getElementById(id).style.backgroundColor = '#eff'
      document.getElementById(id).style.color = '#003'
    },
    fp1() {
      this.p1 = 1;
      this.p2 = 0;
      this.p3 = 0;
      this.p4 = 0;
      this.p5 = 0;
      this.p6 = 0;
      this.buttonSelecting('b1')
      let Selecteds = ['b2', 'b3', 'b4', 'b5', 'b6']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
    },
    fp2() {
      this.p1 = 0;
      this.p2 = 1;
      this.p3 = 0;
      this.p4 = 0;
      this.p5 = 0;
      this.p6 = 0;
      this.buttonSelecting('b2')
      let Selecteds = ['b1', 'b3', 'b4', 'b5', 'b6']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
    },
    fp3() {
      this.p1 = 0;
      this.p2 = 0;
      this.p3 = 1;
      this.p4 = 0;
      this.p5 = 0;
      this.p6 = 0;
      this.buttonSelecting('b3')
      let Selecteds = ['b1', 'b2', 'b4', 'b5', 'b6']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
    },
    fp4() {
      this.p1 = 0;
      this.p2 = 0;
      this.p3 = 0;
      this.p4 = 1;
      this.p5 = 0;
      this.p6 = 0;
      this.buttonSelecting('b4')
      let Selecteds = ['b1', 'b2', 'b3', 'b5', 'b6']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
    },
    fp5() {
      this.p1 = 0;
      this.p2 = 0;
      this.p3 = 0;
      this.p4 = 0;
      this.p5 = 1;
      this.p6 = 0;
      this.buttonSelecting('b5')
      let Selecteds = ['b1', 'b2', 'b3', 'b4', 'b6']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
    },
    fp6() {
      this.p1 = 0;
      this.p2 = 0;
      this.p3 = 0;
      this.p4 = 0;
      this.p5 = 0;
      this.p6 = 1;
      this.buttonSelecting('b6')
      let Selecteds = ['b1', 'b2', 'b3', 'b4', 'b5']
      for (let i in Selecteds) {
        this.buttonSelected(Selecteds[i])
      }
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