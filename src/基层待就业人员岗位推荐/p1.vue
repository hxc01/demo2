<template>
  <div id="page" style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;">
    <div style="position: absolute; width: 99%; left: 0.5%; top: 22px; height: 96.5%;">
      <button class="select" id="sm1" style="left: 42%; top: 1.5%; background-color: #00f; color: #fff">GDP</button>
      <button class="select" id="sm2" style="left: 47%; top: 1.5%">薪资分布</button>
      <button class="select" id="sm3" style="left: 52%; top: 1.5%">岗位分布</button>
      <div class="divs" style="position: absolute;width: 51%; height: 70%; left: 24%; top: 1%">
        <div class="charts" id="map" style="height: 90%"></div>
      </div>

      <!--    统计呈现公司类型、岗位分布、地域分布；挖掘热/冷门行业和高薪、新兴行业-->
      <select id="s1" class="select" style="left: 1%; top: 1.5%"></select>
      <div class="divs" style="width: 23.5%; height: 44.5%; left: 0; top: 1%">
        <div class="titles" id="t1"></div>
        <div class="charts" id="div1"></div>
      </div>

      <!--    分析薪资待遇和其余各种因素之间的关联关系-->
      <select id="s2_1" class="select" style="left: 1%; top: 47%"></select>
      <select id="s2_2" class="select" style="left: 18%; top: 47%"></select>

      <div class="divs" style="width: 23.5%; height: 24.5%; left: 0; top: 46.5%">
        <div class="titles" id="t2"></div>
        <div class="charts" id="div2"></div>
      </div>
      <select id="s3" class="select" style="left: 1%; top: 72.5%"></select>
      <div class="divs" style="width: 43.5%; height: 27.5%; left: 0; top: 72%">
        <div class="titles" id="t3"></div>
        <div class="charts" id="div3"></div>
      </div>

      <!--    提炼各岗位的优势和职责，支持过滤，提供查找和推荐功能-->
      <select id="jobTypes" class="select" @change="changeDiv4" style="left: 76%; top: 1.5%"></select>
      <select id="workTypes" class="select" @change="changeDiv4" style="left: 81%; top: 1.5%"></select>
      <select id="workYears" class="select" @change="changeDiv4" style="left: 86%; top: 1.5%"></select>
      <select id="educations" class="select" @change="changeDiv4" style="left: 91%; top: 1.5%"></select>
      <div class="divs" style="width: 24.5%; height: 59.5%; right: 0; top: 1%">
        <div class="charts" id="div4">
          <div id="div4_2">
            <el-table id="tableData"
                      :data="this.tableData"
                      border
                      style="width: 100%;height: 10%"
                      max-height="360">
              <el-table-column
                  fixed
                  prop="Id"
                  label="Id"
                  width="50">
              </el-table-column>
              <el-table-column prop="岗位名称" label="岗位名称" width="120"></el-table-column>
              <el-table-column prop="公司名称" label="公司名称" width="120"></el-table-column>
              <el-table-column prop="平均薪资" label="平均薪资" width="120"></el-table-column>
              <el-table-column
                  fixed="right"
                  label="操作"
                  width="50">
                <template slot-scope="scope">
                  <el-button @click="div8(scope.row)" type="text" size="small">查看</el-button>
                  <el-button @click="div6(scope.row)" type="text" size="small">分析</el-button>
                  <!--                  <el-button type="text" size="small">导航</el-button>-->
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>
        <div class="titles" id="t4"></div>
      </div>

      <select id="s5" class="select" style="left: 45%; top: 72.5%"></select>
      <div class="divs" style="width: 31%; height: 27.5%; left: 44%; top: 72%">
        <div class="charts" id="div5"></div>
        <div class="titles" id="t5"></div>
      </div>

      <!--    面向求职者提供竞争优势分析和成功率估算，以及通勤线路和拥堵情况-->
      <div class="divs" style="width: 24%; height: 37.5%; right: 0; top: 62%">
        <div class="charts" id="div6"></div>
        <div class="titles" id="t6"></div>
      </div>
      <div v-show="false" class="divs" style="width: 7.5%; height: 37.5%; right: 0; top: 62%">
        <div class="charts" id="div7"></div>
        <div class="titles" id="t7"></div>
      </div>

      <!--    招聘具体信息-->
      <div v-if=this.f8 style="position:absolute; width: 49.5%; height: 59.5%; right: 28%; top: 0;">
        <button id="b8" @click="closeDiv8"
                style="visibility:hidden; position:absolute; background-color: #0000ff; width: 3%; height:5%; right: 3%; top: 5%; color: #ffffff; z-index: 9999">
          x
        </button>
        <div id="div8" class="divs"
             style="visibility:hidden; width: 80%; height: 90%; right: 5%; top: 10%; font-size: 3px; color: #000000">
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {HeatmapLayer, Scene} from '@antv/l7';
import {GaodeMap} from '@antv/l7-maps';
import {Bar, Column, Heatmap, Liquid, Pie, Radar, WordCloud} from "@antv/g2plot";
import insertCss from "insert-css";
import {each, groupBy} from "@antv/util";


let scene, layerm1, layer2, layer3;
let f1 = 1, f2 = 0, f3 = 0;
let localhost = "http://127.0.0.1:3050/"
// let colors = [
//   '#174c83',
//   '#4a96a4',
//   '#7eb6d4',
//   '#efefeb',
//   '#efa759',
//   '#bf9739',
//   '#9b4d16'
// ]
let colors = [
  '#3377cc',
  '#4488cc',
  '#5599dd',
  '#66aadd',
  '#77bbee',
  '#88ccee',
].reverse()
let jobType = "店长"
let jobTypes = ['店长', '导购员', '客服', '理货员', '物流运营', '物流跟单', '报检报关', '仓储管理', '英语老师', '课程顾问', '教务', '助教', '编导', '编剧', '后期制作', '化妆师', '广告创意', '美术指导', '文案', '媒介', '网页设计', '插画师', '工业设计', '视觉设计', '教师', '英语', '美术老师', '幼教', '小学教师', '班主任', '摄影师', '摄影', '制片', '记者', '剪辑', '策划经理', '广告制作', '广告审核', '平面设计', '美容师', '医美', '导游', '旅游计调', '旅游销售', '收银员', '收银', '月嫂', '保姆', '家政', '婚礼策划', '育婴师', '催乳师', '美容导师', '纹绣师', '美甲师', '健身教练', '旅游顾问', '签证', '票务', '服务业', '酒店前台', '酒店管理', '餐饮管理', '保安', '保洁', '司机', '市场策划', '市场顾问', '市场推广', 'sem', '网络营销', '活动策划', '销售经理', '销售代表', '大客户销售', '电话销售', '商品经理', '广告销售', '销售总监', '市场营销', '市场总监', 'seo', '品牌经理', '商务渠道', 'app推广', '销售专员', '客户代表', 'bd经理', '渠道销售', '销售助理', '销售顾问', '营销主管', '商务总监', '城市经理', '招聘', '人力资源专员', '绩效考核', '人力资源经理', '员工关系', '出纳', '税务', '财务经理', '财务分析', '法务专员', '法律顾问', '法务主管', '前台', '经理助理', '行政经理', '行政总监', '人力资源主管', 'hrbp', '培训', '薪资福利', '人力资源总监', '组织发展', '会计', '财务顾问', '结算', '风控', '财务主管', '律师', '物仓调度']
let workTypes = ['全职', '兼职/临时', '实习', '校园']
let workYears = ['1-3年', '1年以下', '不限', '3-5年', '5-10年', '无经验', '10年以上']
let educations = ['大专', '学历不限', '本科', '高中', '中专/中技', '初中及以下', '硕士', 'MBA/EMBA', '博士', '中技']
let div6JsonData = []

function init() {

  addListOption('s1', ['岗位类型', '工作类型'])
  addListOption('s2_1', ['学历', '工作经验'])
  addListOption('s2_2', ['城市', '工作类型'])
  addListOption('s3', ['学历', '工作经验', '城市'])
  addListOption('s5', ['技能需求', '岗位描述'])
  addListOption('jobTypes', jobTypes)
  addListOption('workTypes', workTypes)
  addListOption('workYears', workYears)
  addListOption('educations', educations)


  document.getElementById('s1').onchange = function () {
    div1()
  }
  document.getElementById('s2_1').onchange = function () {
    div2()
  }
  document.getElementById('s2_2').onchange = function () {
    div2()
  }
  document.getElementById('s3').onchange = function () {
    div3()
  }
  document.getElementById('s5').onchange = function () {
    div5()
  }
  document.getElementById('sm1').onclick = function () {
    if (f1 === 0) {
      layerm1.show();
      document.getElementById('sm1').style.background = "#0000ff"
      document.getElementById('sm1').style.color = "#ffffff"
      f1 = 1
    } else {
      layerm1.hide();
      document.getElementById('sm1').style.background = "#ffffff"
      document.getElementById('sm1').style.color = "#000000"
      f1 = 0
    }
  }
  document.getElementById('sm2').onclick = function () {
    if (f2 === 0) {
      layer2.show();
      document.getElementById('sm2').style.background = "#0000ff"
      document.getElementById('sm2').style.color = "#ffffff"
      f2 = 1
    } else {
      layer2.hide();
      f2 = 0
      document.getElementById('sm2').style.background = "#ffffff"
      document.getElementById('sm2').style.color = "#000000"
    }
  }
  document.getElementById('sm3').onclick = function () {
    if (f3 === 0) {
      document.getElementById('sm3').style.background = "#0000ff"
      document.getElementById('sm3').style.color = "#ffffff"
      layer3.show();
      f3 = 1
    } else {
      layer3.hide();
      document.getElementById('sm3').style.background = "#ffffff"
      document.getElementById('sm3').style.color = "#000000"
      f3 = 0
    }
  }

  creatMap()

  div1()
  div2()
  div3()
  // div4()
  div5()
  div6()
  div7()

  m1()
  m2()
  m3()
}

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

function selectTxt(div) {
  return document.getElementById(div).options[document.getElementById(div).options.selectedIndex].text
}

function creatMap(div = 'map') {
  scene = new Scene({
    id: div,
    map: new GaodeMap({
      // style: 'light',
      style: 'amap://styles/45acf9c63991132cf759a67613e1f2d5?isPublic=true',
      pitch: 62.875,
      center: [121.499035, 31.115548],
      zoom: 9.42,
    })
  });
}

function div1(url = localhost + selectTxt('s1') + "div1", div = 'div1') {
  fetch(url)
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1').innerHTML = selectTxt('s1') + "热度情况"
        document.getElementById(div).innerHTML = ""
        const column = new Bar(div, {
          data,
          yField: 'name',
          xField: 'value',
          yAxis: {
            grid: null
          },
          xAxis: {
            grid: null
          },
          seriesField: 'value',
          color: colors,
          scrollbar: {
            type: 'vertical',
          },
          barStyle: {
            radius: [20, 20, 20, 20],
          },
        });

        let jsonData = {}
        column.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        column.on('plot:click', ev => {
          console.log(ev)
          jobType = jsonData['name']
          div5()
          fetch(localhost + jobType + "m1")
              .then((res) => res.json())
              .then((data) => {
                layer2.setData(data)
              });
          fetch(localhost + jobType + "m3")
              .then((res) => res.json())
              .then((data) => {
                layer3.setData(data)
              });
        });
        column.render();
      });
}

function div2(url = localhost + selectTxt('s2_1') + selectTxt('s2_2') + "div2", div = 'div2') {
  fetch(url)
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t2').innerHTML = selectTxt('s2_1') + selectTxt('s2_2') + "关联关系"
        document.getElementById(div).innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById(div), {
          data,
          xField: 'name1',
          yField: 'name2',
          colorField: 'value',
          sizeField: 'value',
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          shape: 'square',
          color: [
            '#3377cc',
            '#4488cc',
            '#5599dd',
            '#66aadd',
            '#77bbee',
            '#88ccee',
          ].reverse(),
          meta: {
            'Month of Year': {
              type: 'cat',
            },
          },
        });
        heatmapPlot.render();
      });
}

function div3(url = localhost + selectTxt('s3') + "div3", div = 'div3') {
  insertCss(`
        #container {
          display: flex;
          flex-direction: column !important;
          padding: 8px;
        }
        #container1, #container2 {
          flex: 1;
        }
      `);

  fetch(url)
      .then((data) => data.json())
      .then((data) => {
        document.getElementById(div).innerHTML = ""
        document.getElementById('t3').innerHTML = selectTxt('s3') + "平均薪资"
        const pieData = ((originData) => {
          const groupData = groupBy(originData, 'type');
          const result = [];
          each(groupData, (values, k) => {
            result.push({type: k, value: values.reduce((a, b) => a + b.value, 0)});
          });
          return result;
        })(data);


        let div1 = document.createElement('div')
        let div2 = document.createElement('div')
        document.getElementById(div).appendChild(div1)
        document.getElementById(div).appendChild(div2)
        div1.id = div + "div1"
        div1.style.position = 'absolute'
        div1.style.width = '25%'
        div1.style.height = '90%'
        div1.style.left = '1%'
        div1.style.top = '1%'
        div2.id = div + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '73%'
        div2.style.height = '73%'
        div2.style.left = '26%'
        div2.style.top = '26%'
        const pie = new Pie(div + "div1", {
          data: pieData,
          colorField: 'type',
          color: colors,
          angleField: 'value',
          label: false,
          tooltip: false,
          state: {
            // 设置【active】激活状态样式 - 无描边
            active: {
              style: {
                lineWidth: 0,
              },
            },
          },
          interactions: [
            {
              type: 'element-highlight',
              cfg: {
                showEnable: [{trigger: 'element:mouseenter', action: 'cursor:pointer'}],
                end: [
                  {trigger: 'element:mouseleave', action: 'cursor:default'},
                  {trigger: 'element:mouseleave', action: 'element-highlight:reset'},
                ],
              },
            },
          ],
        });

        const column = new Column(div + "div2", {
          data,
          // isStack: true,
          isGroup: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color: colors,
          legend: false,
          columnStyle: {
            radius: [4, 4, 0, 0],
          },
          slider: {
            start: 0,
            end: 0.05
          },
          yAxis: false,
          xAxis: false,
        });
        let jsonData = {}
        column.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        column.on('plot:click', ev => {
          console.log(ev)
          jobType = jsonData['name']
          div5()
          fetch(localhost + jobType + "m1")
              .then((res) => res.json())
              .then((data) => {
                layer2.setData(data)
              });
          fetch(localhost + jobType + "m3")
              .then((res) => res.json())
              .then((data) => {
                layer3.setData(data)
              });
        });
        column.render();

        pie.render();
        column.render();

        pie.on('element:mouseover', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            column.setState('selected', (datum) => datum.type === type);
            column.setState('selected', (datum) => datum.type !== type, false);
          }
        });
        pie.on('element:mouseleave', () => {
          // 取消 selected 选中状态
          column.setState('selected', () => true, false);
        });

        pie.on('element:click', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            pie.chart.changeData(pieData.filter((datum) => datum.type === type));
            column.chart.changeData(data.filter((datum) => datum.type === type));
          }
        });
        // 双击，还原数据
        pie.on('element:dblclick', () => {
          pie.chart.changeData(pieData);
          column.chart.changeData(data);
        });
      });
}

// function div4(url = localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4") {
//   fetch(url)
//       .then((res) => res.json())
//       .then((data) => {
//         this.tableData = data
//       });
// }

function div5(url = localhost + jobType + selectTxt('s5') + "div5", div = 'div5') {
  fetch(url)
      .then((res) => res.json())
      .then((data) => {
        document.getElementById(div).innerHTML = ""
        const wordCloud = new WordCloud(div, {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'value',
          color: colors,
          wordStyle: {
            fontFamily: '宋体',
            fontSize: [8, 32],
            rotation: 45,
          },
        });

        wordCloud.render();
      });
}

function div6(div = 'div6') {
  document.getElementById(div).innerHTML = ""
  const radarPlot = new Radar(div, {
    data: div6JsonData,
    xField: 'item',
    yField: 'score',
    seriesField: 'user',
    color: colors,
    meta: {
      score: {
        min: 0,
        max: 80,
      },
    },
    xAxis: {
      line: null,
      tickLine: null,
      grid: {
        line: {
          style: {
            lineDash: null,
          },
        },
      },
    },
    yAxis: {
      line: null,
      tickLine: null,
      grid: {
        line: {
          type: 'line',
          style: {
            lineDash: null,
          },
        },
        alternateColor: 'rgba(0, 0, 0, 0.04)',
      },
    },
    // 开启辅助点
    point: {
      size: 2,
    },
  });
  radarPlot.render();
}

function div7(percent = 0.75, div = 'div7') {
  document.getElementById(div).innerHTML = ""
  const liquidPlot = new Liquid(div, {
    percent: percent,
    shape: 'rect',
    outline: {
      border: 2,
      distance: 4,
    },
    wave: {
      length: 128,
    },
    color: colors[0],
    statistic: {
      content: {
        style: {
          fontSize: '10px',
          color: colors[3],
        }
      }
    }
  });

  liquidPlot.render();
}

function m1(url = localhost + jobType + "m1") {
  scene.on('loaded', () => {
    fetch(url)
        .then(res => res.json())
        .then(data => {
          layerm1 = new HeatmapLayer({})
              .source(data)
              .shape('he')
              .size('mag', [0, 1.0]) // weight映射通道
              .style({
                intensity: 2,
                radius: 50,
                opacity: 0.9,
                rampColors: {
                  // colors: [
                  //   '#FF4818',
                  //   '#F7B74A',
                  //   '#FFF598',
                  //   '#91EABC',
                  //   '#2EA9A1',
                  //   '#206C7C'
                  // ].reverse(),
                  colors: [
                    '#3377cc',
                    '#4488cc',
                    '#5599dd',
                    '#66aadd',
                    '#77bbee',
                    '#88ccee',
                  ].reverse(),
                  positions: [0, 0.2, 0.4, 0.6, 0.8, 1.0]
                }
              });
          scene.addLayer(layerm1);
        });
  });
}

function m3(url = localhost + jobType + "m3") {
  scene.on('loaded', () => {
    fetch(url)
        .then(res => res.json())
        .then(data => {
          layer3 = new HeatmapLayer({})
              .source(data)
              .shape('he')
              .size('mag', [0, 1.0]) // weight映射通道
              .style({
                intensity: 2,
                radius: 40,
                opacity: 0.9,
                rampColors: {
                  // colors: [
                  //   '#FF4818',
                  //   '#F7B74A',
                  //   '#FFF598',
                  //   '#91EABC',
                  //   '#2EA9A1',
                  //   '#206C7C'
                  // ].reverse(),
                  colors: [
                    '#3377cc',
                    '#4488cc',
                    '#5599dd',
                    '#66aadd',
                    '#77bbee',
                    '#88ccee',
                  ].reverse(),
                  positions: [0, 0.2, 0.4, 0.6, 0.8, 1.0]
                }
              });
          scene.addLayer(layer3);
          layer3.hide()
        });
  });
}

function m2(url = localhost + "m2") {
  scene.on('loaded', () => {
    fetch(url)
        .then(res => res.json())
        .then(data => {
          layer2 = new HeatmapLayer({})
              .source(data)
              .shape('he')
              .size('mag', [0, 1.0]) // weight映射通道
              .style({
                intensity: 2,
                radius: 40,
                opacity: 0.9,
                rampColors: {
                  // colors: [
                  //   '#FF4818',
                  //   '#F7B74A',
                  //   '#FFF598',
                  //   '#91EABC',
                  //   '#2EA9A1',
                  //   '#206C7C'
                  // ].reverse(),
                  colors: [
                    '#3377cc',
                    '#4488cc',
                    '#5599dd',
                    '#66aadd',
                    '#77bbee',
                    '#88ccee',
                  ].reverse(),
                  positions: [0, 0.2, 0.4, 0.6, 0.8, 1.0]
                }
              });
          scene.addLayer(layer2);
          layer2.hide()
        });
  });
}


export default {
  name: "jicengdaijiuye",
  data() {
    return {
      tableData: [],
      f8: 0
    }
  },
  mounted() {
    init()
    this.changeDiv4()
    this.inits()
    // this.div6({
    //   "Id": 19480
    // })
    document.getElementById('jobTypes').onchange = function () {
      fetch(localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4")
          .then((res) => res.json())
          .then((data) => {
            this.tableData = data
            div6JsonData = []
          });
    }
  },

  methods: {
    inits() {
      fetch(localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4")
          .then((res) => res.json())
          .then((data) => {
            this.tableData = data
            div6JsonData = []
          });
    },
    changeDiv4: function () {
      fetch(localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4")
          .then((res) => res.json())
          .then((data) => {
            this.tableData = data
          });
    },
    div6: function (ev) {
      let Id = ev['Id']
      fetch(localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4")
          .then((res) => res.json())
          .then((data) => {
            for (let i = 0; i <= 30; i += 1) {
              if (data[i]['Id'] === Id) {
                div6JsonData.push(
                    {"item": "平均薪资", "user": data[i]['岗位名称'], "score": data[i]['平均薪资'] / 1000},
                    {"item": "工作经验", "user": data[i]['岗位名称'], "score": data[i]['工作经验等级']},
                    {"item": "学历", "user": data[i]['岗位名称'], "score": data[i]['学历等级']},
                    {"item": "招聘人数", "user": data[i]['岗位名称'], "score": data[i]['招聘人数'] / 10},
                    {"item": "工作类型", "user": data[i]['岗位名称'], "score": data[i]['工作类型等级']},
                )
                console.log(div6JsonData)
                document.getElementById('t6').innerHTML = "岗位信息雷达图"
                document.getElementById('div6').innerHTML = ""
                const radarPlot = new Radar('div6', {
                  data: div6JsonData,
                  xField: 'item',
                  yField: 'score',
                  seriesField: 'user',
                  color: colors,
                  meta: {
                    score: {},
                  },
                  xAxis: {
                    line: null,
                    tickLine: null,
                    grid: {
                      line: {
                        style: {
                          lineDash: null,
                        },
                      },
                    },
                  },
                  yAxis: {
                    line: null,
                    tickLine: null,
                    grid: {
                      line: {
                        type: 'line',
                        style: {
                          lineDash: null,
                        },
                      },
                      alternateColor: 'rgba(0, 0, 0, 0.04)',
                    },
                  },
                  // 开启辅助点
                  point: {
                    size: 2,
                  },
                });
                radarPlot.render();

              }
            }
          })
    },
    div8: function (ev) {
      let Id = ev['Id']
      this.f8 = 1
      fetch(localhost + selectTxt('jobTypes') + "/" + selectTxt('workTypes') + "/" + selectTxt('workYears') + "/" + selectTxt('educations') + "/div4")
          .then((res) => res.json())
          .then((data) => {
            for (let i = 0; i <= 30; i += 1) {
              if (data[i]['Id'] === Id) {
                document.getElementById('div8').style.visibility = ""
                document.getElementById('b8').style.visibility = ""
                document.getElementById('div8').innerHTML = "技能需求:" +
                    data[i]['技能需求'] + "<br>"
                document.getElementById('div8').innerHTML += "岗位描述:" +
                    data[i]['岗位描述']
              }
            }
          });
    },
    closeDiv8: function () {
      this.f8 = 0
      // document.getElementById('div8').style.visibility = "hidden"
      // document.getElementById('b8').style.visibility = "hidden"
    }
  },

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
