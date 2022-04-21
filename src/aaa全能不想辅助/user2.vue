<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0">

    <select @change="f1_1" id="s1_1" class="selects" style="position: absolute;left: 0.5%; top: 12%"></select>
    <div id="div1_1"
         style="position: absolute; top: 11%; left: 0; width: 100%; height: 100%"
    >
      <img
          src="./logo/机构名称.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 1%;top: 5%"
      >
      <div
          id="jigoumingcheng1"
          style="position: absolute;width: 8%;height: 9%;left: 5%;top: 7.5%"
          class="title"
      />
      <img
          src="./logo/兴办主体.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 1%;top: 14%"
      >
      <div
          id="xingbanzhuti1"
          style="position: absolute;width: 8%;height: 9%;left: 5%;top: 16.5%"
          class="title"
      />
      <img
          src="./logo/机构类别.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 1%;top: 23%"
      >
      <div
          id="jigouleibie1"
          style="position: absolute;width: 8%;height: 9%;left: 5%;top: 25.5%"
          class="title"
      />
      <img
          src="./logo/运营方式.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 1%;top: 32%"
      >
      <div
          id="yunyingfangshi1"
          style="position: absolute;width: 8%;height: 9%;left: 5%;top: 34.5%"
          class="title"
      />
      <img
          src="./logo/床位总数.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 14%;top: 4.5%"
      >
      <div
          id="chuangweizongshu1"
          style="position: absolute;width: 8%;height: 9%;left: 16%;top: 7%"
          class="title"
      />
      <img
          src="./logo/护理床位.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 14%;top: 13.5%"
      >
      <div
          id="hulichuangwei1"
          style="position: absolute;width: 8%;height: 9%;left: 16%;top: 16%"
          class="title"
      />
      <img
          src="./logo/入住人数.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 14%;top: 22.5%"
      >
      <div
          id="ruzhurenshu1"
          style="position: absolute;width: 8%;height: 9%;left: 16%;top: 25%"
          class="title"
      />
      <img
          src="./logo/从业人数.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 14%;top: 31.5%"
      >
      <div
          id="congyerenshu1"
          style="position: absolute;width: 8%;height: 9%;left: 16%;top: 34%"
          class="title"
      />

      <div id="div504"
           style="position: absolute; width:10%;height:20%;left: 22%;top: 25%; color: #030; z-index: 5000"></div>

      <div style="position: absolute; width:10%;height:25%;left: 22%;top: 0;">
        <div id="t2" class="title"></div>
        <div id="div2" class="content"></div>
      </div>
    </div>
    <div id="div1_2"
         style="position: absolute; width: 18%; height: 8%;left: 1%;top: 50%">
      <div style="position: absolute;width: 33%;left: 0;height: 100%">
        <div id="div1_2_1" class="content"></div>
      </div>
      <div style="position: absolute;width: 33%;left: 34%;height: 100%">
        <div id="div1_2_2" class="content"></div>
      </div>
      <div style="position: absolute;width: 33%;left: 67%;height: 100%">
        <div id="div1_2_3" class="content"></div>
      </div>
    </div>


    <div class="block" style="position:absolute;width: 22%;height: 10%; left: -5%; top: 68%; z-index: 4000">
      <span class="title" style="top: -20%">环境评分</span>
      <el-rate
          v-model="value1"
          :colors="colors">
      </el-rate>
    </div>
    <div class="block" style="position:absolute;width: 22%;height: 10%; left: 15%; top: 68%; z-index: 4000">
      <span class="title" style="top: -20%">设施评分</span>
      <el-rate
          v-model="value2"
          :colors="colors">
      </el-rate>
    </div>
    <div class="block" style="position:absolute;width: 22%;height: 10%; left: -5%; top: 78%; z-index: 4000">
      <span class="title" style="top: -20%">服务评分</span>
      <el-rate
          v-model="value3"
          :colors="colors">
      </el-rate>
    </div>
    <div class="block" style="position:absolute;width: 22%;height: 10%; left: 15%; top: 78%; z-index: 4000">
      <span class="title" style="top: -20%">伙食评分</span>
      <el-rate
          v-model="value4"
          :colors="colors">
      </el-rate>
    </div>


    <el-input style="position:absolute;width: 30%;height: 25%; left: 1%; top: 82%; z-index: 4000"
              type="textarea"
              placeholder="请输入内容"
              v-model="textarea"
              maxlength="300"
              show-word-limit
    >
    </el-input>
    <div style="position:absolute;width: 30%;height: 20%; left: 1%; top: 93%; z-index: 4000">
      <el-row>
        <el-button type="warning" icon="el-icon-star-off" circle></el-button>
        <el-button type="success" icon="el-icon-check" circle @click="Fsuccess"></el-button>
        <el-button type="danger" icon="el-icon-delete" circle @click="danger"></el-button>
      </el-row>
    </div>

    <dv-border-box13
        style="position: absolute; width: 33%; height: 50%; left: 0; top: 10%"
        :color="['#aaaaaa', '#eeeeee']"
    >
      <div id="t501" class="title">养老机构信息</div>
    </dv-border-box13>
    <dv-border-box12
        style="position: absolute; width: 33%; height: 40%; left: 0; top: 60%"
        :color="['#aaaaaa', '#eeeeee']"
    >
      <div id="t502" class="title">评价和建议</div>
    </dv-border-box12>
    <dv-border-box11
        v-if="vr"
        title="机构环境游览"
        style="position: absolute; width: 66%; height: 88%; left: 33%; top: 11%; color: #000000"
        :color="['#aaaaaa', '#666666', '#000000']"
    >
      <div v-show="vr1">
        <iframe class="content" src="scene1.html"></iframe>
      </div>
      <div v-show="vr2">
        <iframe class="content" src="scene2.html"></iframe>
      </div>
      <div v-show="vr3">
        <iframe class="content" src="scene3.html"></iframe>
      </div>
      <div v-show="vr4">
        <iframe class="content" src="scene4.html"></iframe>
      </div>
      <div v-show="vr5">
        <iframe class="content" src="scene5.html"></iframe>
      </div>
      <div v-show="vr6">
        <iframe class="content" src="scene6.html"></iframe>
      </div>

    </dv-border-box11>

  </div>
</template>

<script>


// eslint-disable-next-line no-unused-vars
import * as THREE from 'three';
// eslint-disable-next-line no-unused-vars
import {Bar, Gauge, WordCloud} from "@antv/g2plot";
// eslint-disable-next-line no-unused-vars
import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";


let localhost = 'http://127.0.0.1:5000/'


// eslint-disable-next-line no-unused-vars
let colors1 = [
  '#33aa33',
  '#776677',
  '#449944',
  '#885588',
  '#558855',
  '#667766',
  '#994499',
]
// eslint-disable-next-line no-unused-vars
let colors2 = [
  '#33aa33',
  '#994499',
  '#33aaaa',
  '#3a3aaa',
  '#aaaa33',
]
// eslint-disable-next-line no-unused-vars
let colors3 = [
  '#33aa33',
  '#449944',
  '#558855',
  '#667766',
  '#776677',
  '#885588',
  '#994499',
]


// eslint-disable-next-line no-unused-vars
function cmp(x, y) {
  return -x.value + y.value
}

// eslint-disable-next-line no-unused-vars
function selectTxt(div) {
  return document.getElementById(div).options[document.getElementById(div).options.selectedIndex].text
}

// eslint-disable-next-line no-unused-vars
function addListOption(selectId, listItems) {
  document.getElementById(selectId).innerHTML = ""
  for (let item in listItems) {
    let selectID = document.getElementById(selectId);
    let option = document.createElement("option");
    option.appendChild(document.createTextNode(listItems[item]));
    option.setAttribute("value", listItems[item]);
    selectID.appendChild(option);
  }
}

// eslint-disable-next-line no-unused-vars
function div1(name) {
  fetch(localhost + name + "/div1")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('jigoumingcheng1').innerHTML = data[0]['机构名称']
        document.getElementById('yunyingfangshi1').innerHTML = data[0]['运营方式']
        document.getElementById('jigouleibie1').innerHTML = data[0]['机构类别']
        document.getElementById('xingbanzhuti1').innerHTML = data[0]['兴办主体']
        document.getElementById('chuangweizongshu1').innerHTML = data[0]['床位总数'] + "张"
        document.getElementById('hulichuangwei1').innerHTML = data[0]['护理型床位数'] + "张"
        document.getElementById('ruzhurenshu1').innerHTML = data[0]['入住老年人数'] + "人"
        document.getElementById('congyerenshu1').innerHTML = data[0]['从业人员数'] + "人"
        document.getElementById('div1_2_1').innerHTML = ""
        document.getElementById('div1_2_2').innerHTML = ""
        document.getElementById('div1_2_3').innerHTML = ""
        let gauge1 = new Gauge('div1_2_1', {
          percent: data[0]['入住老年人数'] / data[0]['床位总数'],
          range: {
            color: 'l(0) 0:#B8FFE1 1:#3DDD76',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            title: {
              offsetY: -12,
              style: {
                fontSize: '18px',
                color: '#4B535E',
              },
              formatter: () => String((data[0]['入住老年人数'] / data[0]['床位总数']).toFixed(2) * 100).slice(0, 3) + "%",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => '入住比例',
            },
          },
        });
        gauge1.render();
        let gauge2 = new Gauge('div1_2_2', {
          percent: data[0]['从业人员数'] / data[0]['入住老年人数'],
          range: {
            color: 'l(0) 0:#B8FFE1 1:#3DDD76',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            title: {
              offsetY: -12,
              style: {
                fontSize: '18px',
                color: '#4B535E',
              },
              formatter: () => String((data[0]['从业人员数'] / data[0]['入住老年人数']).toFixed(2) * 100).slice(0, 3) + "%",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => '从业比例',
            },
          },
        });
        gauge2.render();
        let gauge3 = new Gauge('div1_2_3', {
          percent: data[0]['护理型床位数'] / data[0]['床位总数'],
          range: {
            color: 'l(0) 0:#B8FFE1 1:#3DDD76',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            title: {
              offsetY: -12,
              style: {
                fontSize: '18px',
                color: '#4B535E',
              },
              formatter: () => String((data[0]['护理型床位数'] / data[0]['床位总数']).toFixed(2) * 100).slice(0, 3) + "%",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => '护理床位比',
            },
          },
        });
        gauge3.render();


      })
}

// eslint-disable-next-line no-unused-vars
function div2() {
  fetch(localhost + selectTxt('s1_1') + "/reviewWords")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div2').innerHTML = ""
        const wordCloud = new WordCloud('div2', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'name',
          wordStyle: {
            fontFamily: 'Verdana',
            fontSize: [8, 32],
            rotation: 45,
          },
          // 返回值设置成一个 [0, 1) 区间内的值，
          // 可以让每次渲染的位置相同（前提是每次的宽高一致）。
          random: () => 0.5,
        });

        wordCloud.render();
      });
}

// eslint-disable-next-line no-unused-vars
function makeSkybox(urls, size) {
  let skyboxCubemap = new THREE.CubeTextureLoader().load(urls);
  skyboxCubemap.format = THREE.RGBFormat;

  let skyboxShader = THREE.ShaderLib['cube'];
  skyboxShader.uniforms['tCube'].value = skyboxCubemap;
  console.log('执行了添加天空盒子语句');

  return new THREE.Mesh(
      new THREE.BoxGeometry(size, size, size),
      new THREE.ShaderMaterial({
        fragmentShader: skyboxShader.fragmentShader,
        vertexShader: skyboxShader.vertexShader,
        uniforms: skyboxShader.uniforms,
        depthWrite: false,
        side: THREE.BackSide
      })
  );
}

// eslint-disable-next-line no-unused-vars
function Scores() {
  fetch(localhost + selectTxt('s1_1') + "/reviewScores")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div504').innerHTML = ""
        const bar = new Bar('div504', {
          data,
          xField: 'value',
          yField: 'name',
          seriesField: 'name',
          legend: {
            position: 'top-left',
          },
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          }
        });
        bar.render();
      });
}


export default {
  name: "yantaiyanglaofusaip5",
  mounted() {


    addListOption('s1_1', ['烟台市老年福利服务中心', '烟台市芝罘区益健老年人颐养中心', '烟台市芝罘区富昌老年公寓', '烟台舜世养老服务有限公司', '烟台市芝罘区宏盛养老院', '烟台市芝罘区老涞福老人公寓', '烟台市芝罘区幸福龙海老年人颐养中心', '烟台芝罘岛老年颐养中心', '烟台市芝罘区进德老年公寓', '烟台市芝罘区温暖老年公寓', '烟台市芝罘区金东养老服务中心', '烟台市芝罘区黄务老年公寓', '烟台市芝罘区金色家园老年公寓', '烟台市芝罘区德信老年颐养中心', '烟台润昌颐养院有限公司', '烟台市芝罘区福盛老年公寓', '烟台市芝罘区东方老年颐养中心', '烟台市芝罘区天慈颐养中心', '烟台城发榆悦康护医院有限公司', '烟台市芝罘区宝云颐养中心', '烟台市芝罘区奇山康宁老年公寓', '烟台珠玑老年公寓', '烟台只楚老年公寓有限公司', '烟台小小养老服务有限公司', '烟台市芝罘区恒爱亲情养老护理服务中心', '烟台市芝罘区康乐老年公寓', '烟台凤翔山庄养老服务中心有限公司', '烟台力高鹤安养老服务中心有限公司', '烟台市顺鑫养老服务有限公司', '烟台和悦天伦养老院有限公司', '烟台市芝罘区广济老年人颐养中心', '烟台润祥颐养院有限公司', '烟台市夕阳红老年公寓', '烟台市芝罘区君祥老年公寓', '烟台市九如城养老服务有限公司', '济南鲁商福瑞达护理院有限公司烟台分公司', '烟台万汇老年公寓有限公司', '烟台市牟平区温馨老年公寓', '烟台市牟平区社会福利中心', '烟台市牟平区德源老年公寓', '烟台为民养老服务有限公司', '烟台市牟平区福满老年公寓', '烟台市牟平区康悦老年公寓', '烟台市牟平区文化街道办事处敬老院', '烟台市牟平区福元老年公寓', '烟台市牟平区馨慧老年公寓', '烟台市牟平区福荣老年公寓', '烟台市牟平区桃源老年公寓', '烟台市牟平区社会救助综合服务中心', '烟台市牟平区兴华老年公寓', '烟台市牟平区姜格庄街道敬老院', '烟台市牟平区人民政府大窑街道敬老院', '烟台市牟平区紫宸老年公寓', '烟台市牟平区幸福老年公寓', '烟台市牟平区人民政府武宁街道敬老院', '烟台市牟平区福康老年看护服务中心', '烟台市牟平区浩岭湖养老院', '烟台市牟平区儒家老年公寓', '烟台市牟平区观水镇敬老院', '烟台市牟平区龙泉镇敬老院', '烟台市牟平区玉林店镇敬老院', '烟台市牟平区水道镇敬老院', '烟台市牟平区高陵镇下雨村敬老院', '烟台市牟平区王格庄镇敬老院', '烟台市牟平区莒格庄镇敬老院', '烟台莱山区红洁老年养护中心', '烟台莱山秀林老年福利服务中心', '烟台市莱山区清泉养生苑', '烟台圣莱恩养老院有限公司', '烟台市莱山区弘翔老年公寓', '烟台市莱山区圣恩老年公寓', '烟台市正大城发养老服务有限公司', '烟台市蓬莱区紫荆山街道舒怡苑老年公寓', '烟台市蓬莱区紫荆山老年社会福利中心', '烟台市蓬莱区紫荆山街道敬老院', '烟台市蓬莱涌泉康护中心', '蓬莱顺康养老服务有限公司', '蓬莱市夕阳红养老服务有限公司', '华录健康养老发展有限公司烟台分公司', '龙口市兰高镇敬老院', '龙口市诸由观镇敬老院', '龙口市芦头镇敬老院', '龙口市龙港街道敬老院', '龙口市七甲镇敬老院', '龙口市新嘉街道敬老院', '龙口市东江五里桥老年公寓', '龙口市同心老年公寓', '龙口市徐福街道敬老院', '龙口市下丁家镇敬老院', '龙口市枫晚老年公寓', '龙口市下丁家田原山庄老年公寓', '龙口市黄山馆镇敬老院', '龙口市康乐福老年公寓', '龙口市海岱老年公寓', '龙口市东莱街道遇家敬老院', '东江街道敬老院', '龙口市东莱街道敬老院', '龙口市恒康养老服务中心', '龙口市石良镇敬老院', '龙口市开元养老康复中心', '莱阳市金色晚年老年公寓', '莱阳市温馨老年公寓', '家和兴老年公寓', '莱阳市颐养院老年公寓', '莱阳德昭颐养中心', '莱阳德怡老年公寓', '莱阳鸿杰敬老公寓', '莱阳市安泰老年公寓', '益寿康老年公寓', '莱阳市天福老年公寓', '莱阳市康泰山庄老年公寓', '莱阳市天乐老年公寓', '莱阳市爱心老年公寓', '莱阳市康佳老年公寓', '莱阳市康达老年公寓', '莱阳市怡康老年公寓', '莱阳鸿杰龙旺庄养老公寓', '莱阳鸿福莱颐养中心', '莱阳市金安达老年服务中心', '莱阳市经济开发区祥福苑老年公寓', '莱阳鸿杰柏林庄养老公寓', '莱阳鸿杰沐浴店养老公寓', '万第老来乐老年公寓', '莱阳市夕阳红老年公寓有限公司', '高格庄康华老年公寓', '莱州市社会福利中心', '莱州市文昌敬老院', '莱州市永安路街道敬老院', '莱州市三山岛街道西由敬老院', '莱州市颐寿养老院', '莱州市三山岛街道过西敬老院', '莱州市西由颐寿园托老所', '莱州市老年康复中心', '莱州市城港路街道敬老院', '莱州桃源山庄老年公寓', '莱州市文峰路街道敬老院', '府林公寓', '沙河镇养老服务中心', '莱州市沙河镇敬老院', '莱州市朱桥镇敬老院', '莱州市郭家店镇敬老院', '莱州市柴棚养老院', '莱州市金城镇敬老院', '莱州市平里店镇敬老院', '莱州市驿道镇中心敬老院', '莱州市程郭镇敬老院', '莱州市虎头崖镇敬老院', '莱州市石都老年公寓', '莱州市柞村镇中心敬老院', '莱州市夏邱镇敬老院', '莱州市夏邱镇老年服务中心', '莱州市土山镇敬老院', '金岭镇敬老院', '招远市张星镇敬老院', '招远市东城老年公寓', '招远市阜山镇敬老院', '御华老年公寓', '招远市福康养老有限责任公司', '招远市康璐老年公寓', '招远市滨海老年公寓', '招远市轮胎西区老年公寓', '招远市多米养老服务有限公司', '招远市祥和圆老年公寓有限公司', '招远市金都老年福利中心', '招远市毕郭镇敬老院', '招远市蚕庄镇敬老院', '招远金汇老年公寓', '招远市夏甸镇敬老院', '招远金街养老服务中心', '招远市玲珑镇敬老院', '招远市金辉老年公寓有限公司', '招远市新亚永宁老年公寓', '招远市龙馨养老服务中心', '招远市金城老年福利服务中心', '招远市齐山镇敬老院', '招远市金康老年养护中心', '招远市锦江老年人日间照料中心', '招远市禄良养老服务有限公司', '栖霞市爱尚综合养老服务中心', '栖霞爱高养老公寓', '栖霞市翠屏街道御椿苑综合养老服务中心', '栖霞市盛健老年公寓', '栖霞市夕阳红老年公寓', '栖霞市桃村中心敬老院', '栖霞市杨础中心敬老院', '栖霞市瑞康养老服务有限公司', '栖霞平安老年公寓', '栖霞市鹤园颐养院', '栖霞市坤园老年公寓', '栖霞市凯晨老年公寓', '栖霞市福寿康养老中心', '栖霞市温心老年公寓', '海阳市康馨老年公寓', '海阳市幸福老年公寓', '海阳市盘石店镇敬老院', '海阳市坤元养老院', '海阳市康安老年公寓', '海阳市招虎山老年公寓', '海阳市方圆街道办事处敬老院', '海阳市夕阳红老年公寓', '海阳市留格庄镇敬老院', '海阳市辛安镇敬老院', '海阳市聚福德老年公寓', '海阳市鑫源老年公寓', '海阳市行村镇敬老院', '海阳市阳光老年公寓', '海阳市荣庆老年公寓', '海阳市大成老年公寓', '海阳市鹤童村老年护理中心', '海阳市福泰老年公寓', '海阳市盛泉养老院', '海阳市吉利老年公寓', '海阳市老年公寓', '海阳市和平南山老年公寓', '海阳市以马内利老年公寓', '海阳市医方养老院', '海阳市里店镇敬老院', '海阳市发城镇敬老院', '海阳市小纪镇敬老院', '海阳市徐家店镇敬老院', '海阳市生生老年公寓', '海阳市海大医养院', '烟台经济技术开发区金东颐养中心', '烟台经济技术开发区恒达颐养中心', '烟台开发区磁山颐生苑老年公寓', '烟台国康养老服务有限公司', '烟台经济技术开发区社会福利中心', '烟台高新区御花园老年养护中心', '烟台市蕾娜范颐养院', '南长山敬老院', '长岛县砣矶镇敬老院'])

    div1(selectTxt('s1_1'))
    div2()
    Scores()


  },
  methods: {
    f1_1: function () {
      div1(selectTxt('s1_1'))
      div2()
      Scores()
      if (this.vr1 === 1) {
        this.vr = 0
        this.vr1 = 0
        this.vr2 = 1
        this.vr = 1
      }
      if (this.vr2 === 1) {
        this.vr = 0
        this.vr2 = 0
        this.vr3 = 1
        this.vr = 1
      }
      if (this.vr3 === 1) {
        this.vr = 0
        this.vr3 = 0
        this.vr4 = 1
        this.vr = 1
      }
      if (this.vr4 === 1) {
        this.vr = 0
        this.vr4 = 0
        this.vr5 = 1
        this.vr = 1
      }
      if (this.vr5 === 1) {
        this.vr = 0
        this.vr5 = 0
        this.vr6 = 1
        this.vr = 1
      }
      if (this.vr6 === 1) {
        this.vr = 0
        this.vr6 = 0
        this.vr1 = 1
        this.vr = 1
      }

    },
    Fsuccess: function () {
      fetch(localhost + selectTxt('s1_1') + "/" + this.value1 + "/" + this.value2 + "/" + this.value3 + "/" + this.value4 + "/" + this.textarea + "/reviewIn")
          .then((res) => res.json())
          .then((data) => {
            data = ""
            localhost += data
            div2()
            Scores()
          })
    },
    danger: function () {
      this.value1 = ""
      this.value2 = ""
      this.value3 = ""
      this.value4 = ""
      this.textarea = ""
    }
  },
  data() {
    return {
      config: {
        data: [
          {
            name: '设施评分',
            value: 5
          },
          {
            name: '环境评价',
            value: 4
          },
          {
            name: '伙食评分',
            value: 3
          },
          {
            name: '服务评分',
            value: 4
          },
        ]
      },
      value1: null,
      value2: null,
      value3: null,
      value4: null,
      textarea: '',
      colors: [
        '#99ffbb',
        '#77bb88',
        '#559955',
        '#006600',
        '#003300',
      ],
      vr: 1,
      vr1: 1,
      vr2: 0,
      vr3: 0,
      vr4: 0,
      vr5: 0,
      vr6: 0,
    }
  }
}
</script>

<style scoped>
.content {
  position: absolute;
  width: 96%;
  height: 80%;
  left: 2%;
  top: 16%;
  text-align: center;
  font-size: 20%;
  color: #eeffee;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 50%;
  height: 6%;
  left: 25%;
  top: 7%;
  text-align: center;
  font-size: 20%;
  color: #007700;
  font-weight: bold;

}

.divs {
  position: absolute;
  background-color: #f9f9f9;
  text-align: center;
  border-width: 3px;
  border-color: #222222;
}

.selects {
  position: absolute;
  width: 5%;
  height: 3%;
  background-color: #fff;
  border-color: #ded;
  border-width: 1px;
  color: #070;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>