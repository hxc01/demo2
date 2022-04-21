<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div style="position: absolute;width: 98%;height: 85%;left: 1%;top: 12%;">
      <div class="divs" style="width: 24%; height: 99%; left: 0; top: 0">
        <div id="d501" class="content">
          <div class="divs" style="position: absolute; width: 100%; height: 40%; left: 0; top: 5%">
            <div id="d5011" class="content" style="color: #003;"></div>
            <div id="t5011" class="title"></div>
          </div>
          <div class="divs" style="position: absolute; width: 100%; height: 50%; left: 0; top: 50%">
            <div id="d5012" class="content"></div>
            <div id="t5012" class="title"></div>
          </div>
        </div>
        <div id="t501" class="title"></div>
      </div>
      <div class="divs" style="width: 49%; height: 59%; left: 25%; top: 0">
        <div id="d502" class="content"></div>
        <div id="t502" class="title"></div>
      </div>
      <div class="divs" style="width: 24%; height: 59%; left: 75%; top: 0">
        <div id="d503" class="content"></div>
        <div id="t503" class="title"></div>
      </div>
      <div class="divs" style="width: 74%; height: 39%; left: 25%; top: 60%">
        <div id="d504" class="content"></div>
        <div id="t504" class="title"></div>
      </div>
    <select id="s501" @change="f501" class="selects" style="left: 2%; top: 55%"></select>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {
  Funnel,
  RadialBar,
  Sankey,
} from '@antv/g2plot';
import * as echarts from "echarts";

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene

// eslint-disable-next-line no-unused-vars
let color = [
  '#00eeff',
  '#00ccee',
  '#0099dd',
  '#0066cc',
  '#0033bb',
  '#0000aa'
]

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
let zdmc = '严重精神障碍（系统治疗三个月以上）', age = '50', jzCity = '日照市东港区', ryCity = '日照市东港区'

// eslint-disable-next-line no-unused-vars
function fAge() {
  c502()
}

// eslint-disable-next-line no-unused-vars
function fZdmc() {
  c5011()
}

// eslint-disable-next-line no-unused-vars
function fJzCity() {
  c503()
}

// eslint-disable-next-line no-unused-vars
function c5011() {
  fetch(localhost + zdmc + "/d5011")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t5011').innerHTML = zdmc + "特征分析"
        document.getElementById('d5011').innerHTML = data['s1'] + '<br>' + data['s2'] + '<br>' + data['s3'] + '<br>' + data['s4'] + '<br>' + data['s5'] + '<br>' + data['s6'] + '<br>' + data['s7']
      })
}

// eslint-disable-next-line no-unused-vars
function c5012() {
  fetch(localhost + selectTxt('s501') + "/" + zdmc + "/d5012")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t5012').innerHTML = selectTxt('s501') + "年" + zdmc + "就诊人数"
        document.getElementById('d5012').innerHTML = ""
        const bar = new RadialBar('d5012', {
          data,
          isStack: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          maxAngle: 270, //最大旋转角度,
          radius: 0.8,
          innerRadius: 0.2,
          colorField: 'type',
          color: ({type}) => {
            if (type === '女') {
              return '#36c361';
            } else {
              return '#2194ff';
            }
          },
        });
        bar.render();
      });
}

// eslint-disable-next-line no-unused-vars
function c502() {
  let chartDom = document.getElementById('d502');
  let myChart = echarts.init(chartDom);
  let option;

  // myChart.showLoading();
  fetch(localhost + age + "/d502")
      .then((res) => res.json())
      .then((graph) => {
        document.getElementById('t502').innerHTML = age + "岁疾病地理分布"
        // myChart.hideLoading();
        option = {
          title: false,
          tooltip: {},
          legend: [
            {
              // selectedMode: 'single',
              data: graph.categories.map(function (a) {
                return a.name;
              })
            }
          ],
          animationDuration: 1500,
          animationEasingUpdate: 'quinticInOut',
          series: [
            {
              name: '',
              type: 'graph',
              layout: 'none',
              data: graph.nodes,
              links: graph.links,
              categories: graph.categories,
              roam: true,
              label: {
                position: 'right',
                formatter: '{b}'
              },
              lineStyle: {
                color: 'source',
                curveness: 0.3
              },
              emphasis: {
                focus: 'adjacency',
                lineStyle: {
                  width: 1
                }
              }
            }
          ]
        };
        myChart.setOption(option);
        option && myChart.setOption(option);
      });
  myChart.on('click', ev => {
    if (ev['data']['name'] in ['日照市市辖区', '日照市经济开发区', '日照市东港区', '日照市岚山区', '日照市莒县', '日照市五莲县', '日照市山海天旅游度假区', '济南市']) {
      zdmc = zdmc + ""
    } else {
      zdmc = ev['data']['name']
      c503()
      c504()
      c5011()
      c5012()
    }
  })
}

// eslint-disable-next-line no-unused-vars
function c503() {
  fetch(localhost + jzCity + "/" + zdmc + "/d503")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t503').innerHTML = jzCity + zdmc + "年龄分布模型"
        document.getElementById('d503').innerHTML = ""
        const funnelPlot = new Funnel('d503', {
          data,
          xField: 'name',
          yField: 'value',
          legend: false,
          label: false,
          color,
          colorField: 'value',
          conversionTag: false
        });

        funnelPlot.render();
        let hoverData = {}
        funnelPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        funnelPlot.on('plot:click', ev => {
          ev = ""
          age = hoverData['name'] + ev
          fAge()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function c504() {
  fetch(localhost + zdmc + "/d504")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t504').innerHTML = zdmc + "人员流向图"
        document.getElementById('d504').innerHTML = ""
        const sankey = new Sankey(document.getElementById('d504'), {
          data,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          nodeWidthRatio: 0.008,
          nodePaddingRatio: 0.03,
        });
        sankey.render();
        let hoverData = {}
        sankey.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        sankey.on('plot:click', ev => {
          ev = ""
          if (hoverData['target'] === '日照市市辖区') {
            jzCity = hoverData['source'] + ev
          } else {
            jzCity = hoverData['target'] + ev
          }
          fJzCity()
        });
      })
}


export default {
  name: 'p5',
  data() {
    return {}
  },
  mounted() {


    addListOption('s501', ['2021', '2020', '2019', '2018', '2017'])


    c5011()
    c5012()
    c502()
    c503()
    c504()


  },
  methods: {
    f501() {
      c5012()
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
  height: 90%;
  left: 5%;
  top: 20px;
  text-align: center;
  font-size: 20%;
  color: #003;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 100%;
  height: 20px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 20%;
  color: #eff;
  font-weight: bold;
  background-color: #38b;
}

.divs {
  position: absolute;
  text-align: center;
  background-color: #eff;
  border-width: 3px;
  border-style: outset;
  border-color: #cdd;
  opacity: 0.99;
  /*border-radius: 5px;*/
  z-index: 3000;
}

.selects {
  position: absolute;
  width: 5%;
  height: 3%;
  background-color: #eff;
  border-color: #dee;
  border-width: 1px;
  color: #000;
  border-radius: 5px;
  z-index: 9999;
  font-size: 9px;
  text-align: center;
}
</style>