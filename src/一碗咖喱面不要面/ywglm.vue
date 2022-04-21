<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #fff">

    <div style="position: absolute; width: 100%; height: 8%; left: 0; top: 0; background-color: #88ADA8">
      <div class="content" style="width: 15%; height: 50%; left: 0; top: 25%; font-size: 20px">车流量管理系统</div>
    </div>

    <div style="position: absolute; width: 15%; height: 92%; left: 0; top: 8%; background-color: #333333">
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 5%; background-color: #444444;">
        <div id="bp1" @click="fp1"
             style="position:absolute;width:80%; left:10%; height: 50%; top: 20%; color: #ffffff; font-size: 15px;">
          流量气象分析
        </div>
      </div>
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 15%; background-color: #444444;">
        <div id="bp2" @click="fp2"
             style="position:absolute;width:80%; left:10%; height: 50%; top: 20%; color: #ffffff; font-size: 15px;">
          时间对比分析
        </div>
      </div>
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 25%; background-color: #444444;">
        <div id="bp3" @click="fp3"
             style="position:absolute;width:80%; left:10%; height: 50%; top: 20%; color: #ffffff; font-size: 15px;">
          站点对比分析
        </div>
      </div>
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 35%; background-color: #444444;">
        <div id="bp4" @click="fp4"
             style="position:absolute;width:80%; left:10%; height: 50%; top: 20%; color: #ffffff; font-size: 15px;">
          卡口对比分析
        </div>
      </div>
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 45%; background-color: #444444;">
        <div id="bp5" @click="fp5"
             style="position:absolute;width:50%; left:25%; height: 50%; top: 20%; color: #ffff00; font-size: 15px;">
          管理规划
        </div>
      </div>
      <div class="divs"
           style="position: absolute; width: 80%; height: 5%; left: 10%; top: 55%; background-color: #444444;">
        <div id="bp6" @click="fphone"
             style="position:absolute;width:50%; left:25%; height: 50%; top: 20%; color: #ffffff; font-size: 15px;">
          app路线规划
        </div>
      </div>
    </div>


    <div v-show="this.p1&&!phone"
         style="position: absolute; width: 85%; height: 92%; left: 15%; top: 8%; background-color: #ffffff">
      <div class="divs" style="position:absolute; left: 1%; top: 1%; width: 8.5%; height: 28%">
        <div class="title" id="t101"></div>
        <div class="content" id="d101"></div>
      </div>
      <div class="divs" style="position:absolute; left: 10%; top: 1%; width: 18.5%; height: 28%">
        <div class="title" id="t102"></div>
        <div class="content" id="d102"></div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 30%; width: 27.5%; height: 20.4%">
        <div class="title" id="t103"></div>
        <div class="content" id="d103"></div>
      </div>


      <div class="divs" style="position:absolute; left: 1%; top: 54%; width: 48%; height: 23%">
        <div class="title" id="t104"></div>
        <div class="content" id="d104"></div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 79.5%; width: 15%; height: 17.5%">
        <div class="title" id="t105"></div>
        <div class="content" id="d105"></div>
      </div>
      <div class="divs" style="position:absolute; left: 17%; top: 79.5%; width: 15%; height: 17.5%">
        <div class="title" id="t106"></div>
        <div class="content" id="d106"></div>
      </div>
      <div class="divs" style="position:absolute; left: 33%; top: 79.5%; width: 16%; height: 17.5%">
        <div class="title" id="t107"></div>
        <div class="content" id="d107"></div>
      </div>


      <div class="divs" style="position:absolute; left: 70.5%; top: 1%; width: 16%; height: 52.8%">
        <div class="title" id="t108"></div>
        <div class="content" id="d108"></div>
      </div>
      <div class="divs" style="position:absolute; left: 87%; top: 1%; width: 12.5%; height: 11.5%">
        <div class="title" id="t109"></div>
        <div class="content" id="d109"></div>
      </div>
      <div class="divs" style="position:absolute; left: 87%; top: 13.5%; width: 12.5%; height: 11.5%">
        <div class="title" id="t110"></div>
        <div class="content" id="d110"></div>
      </div>
      <div class="divs" style="position:absolute; left: 87%; top: 26%; width: 12.5%; height: 11.5%">
        <div class="title" id="t111"></div>
        <div class="content" id="d111"></div>
      </div>
      <div class="divs" style="position:absolute; left: 87%; top: 39%; width: 12.5%; height: 10.5%">
        <div class="title" id="t112"></div>
        <div class="content" id="d112"></div>
      </div>

      <div class="divs" style="position:absolute; left: 50%; top: 54%; width: 24%; height: 46%">
        <div class="title" id="t113"></div>
        <div class="content" id="d113"></div>
      </div>
      <div class="divs" style="position:absolute; left: 75%; top: 54%; width: 24%; height: 23%">
        <div class="title" id="t114"></div>
        <div class="content" id="d114"></div>
      </div>
      <div class="divs" style="position:absolute; left: 75%; top: 79%; width: 24%; height: 18%">
        <div class="title" id="t115"></div>
        <div class="content" id="d115"></div>
      </div>

    </div>
    <div v-show="this.p2&&!phone"
         style="position: absolute; width: 85%; height: 92%; left: 15%; top: 8%; background-color: #ffffff">
      <div class="divs" style="position:absolute; left: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t201"></div>
        <div class="content" id="d201"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t202"></div>
        <div class="content" id="d202"></div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t203"></div>
        <div class="content" id="d203"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t204"></div>
        <div class="content" id="d204"></div>
      </div>
    </div>
    <div v-show="this.p3&&!phone"
         style="position: absolute; width: 85%; height: 92%; left: 15%; top: 8%; background-color: #ffffff">
      <div class="divs" style="position:absolute; left: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t301"></div>
        <div class="content" id="d301"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t302"></div>
        <div class="content" id="d302"></div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t303"></div>
        <div class="content" id="d303"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t304"></div>
        <div class="content" id="d304"></div>
      </div>
    </div>
    <div v-show="this.p4&&!phone"
         style="position: absolute; width: 85%; height: 92%; left: 15%; top: 8%; background-color: #ffffff">
      <div class="divs" style="position:absolute; left: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t401"></div>
        <div class="content" id="d401"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t402"></div>
        <div class="content" id="d402"></div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t403"></div>
        <div class="content" id="d403"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 54%; width: 48.5%; height: 45%">
        <div class="title" id="t404"></div>
        <div class="content" id="d404"></div>
      </div>
    </div>
    <div v-show="this.p5&&!phone"
         style="position: absolute; width: 85%; height: 92%; left: 15%; top: 8%; background-color: #ffffff">
      <div class="divs" style="position:absolute; left: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t501"></div>
        <div class="content" id="d501"></div>
      </div>
      <div class="divs" style="position:absolute; right: 1%; top: 1%; width: 28%; height: 52.7%">
        <div class="title" id="t502"></div>
        <div class="content" id="d502">
          <button @click="tijiao" class="selects" style="right: 2%; top: 1%">提交</button>
        </div>
      </div>
      <div class="divs" style="position:absolute; left: 1%; top: 53%; width: 98%; height: 47%">
        <div class="title" id="t503">选中卡口流量画像</div>
        <div class="content" id="d503"></div>
      </div>
    </div>

    <div v-show="!phone" class="divs" style="position:absolute; left: 40%; top: 8.9%; width: 34.5%; height: 48.5%">
      <div class="title">
        <button @click="reduceHour"
                style="position: absolute; width: 8%; height: 98%; left: 1%; top: 1%; background-color: #fff; color: #000; text-align: center">
          《
        </button>
        <button @click="addHour"
                style="position: absolute; width: 8%; height: 98%; right: 1%; top: 1%; background-color: #fff; color: #000; text-align: center">
          》
        </button>
        <div class="title" style="width: 60%; left: 20%" id="time"></div>
      </div>
      <div class="content" id="map">
        <button @click="fl1" class="selects" style="left: 1%; top: 1%">污染情况</button>
        <button @click="fl2" class="selects" style="left: 16%; top: 1%">过车数量</button>
        <button @click="fl4" class="selects" style="left: 31%; top: 1%">流量热力</button>
      </div>
    </div>

    <select v-show="(p2||p3)&&!phone" id="s1" class="selects" style="left: 16%; top: 12.5%" @change="fAir"></select>
    <select v-show="(p2||p4)&&!phone" id="s2" class="selects" style="right: 1%; top: 12.5%" @change="fCar"></select>


    <phone v-if="this.phone"></phone>

  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, LineLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Pie, G2, Radar, Liquid, Gauge, Area, Bar, Heatmap, Rose, Violin, RadialBar, Progress} from '@antv/g2plot';
// eslint-disable-next-line no-unused-vars
import {PivotSheet} from '@antv/s2';
// eslint-disable-next-line no-unused-vars
import {Line} from '@antv/g2plot';
import {DrawControl} from "@antv/l7-draw";
import * as echarts from "echarts";
import phone from './phone'

// eslint-disable-next-line no-unused-vars
let l1, l2, l3, l4, l5, l6, l7, l8, l9

// eslint-disable-next-line no-unused-vars
let y = 2021, m = 5, d = 7, h = 8, s = '7:00-9:00'

// eslint-disable-next-line no-unused-vars
let airType = 'CO', p1 = '海关', p2 = '区政府', p3 = '聊大东校', carType1 = '小型普通客车', carType2 = '重型栏板货车',
    carType3 = '大型汽车', carType4 = '小型汽车', types1 = 'AQI',
    // eslint-disable-next-line no-unused-vars
    types2 = "降水量", types3 = "气温", k1 = '黄河10', k2 = '辽河91', k3 = '黄河403',
    k_arry = ['黄河35', '辽河91', '黄河152', '北环155', '辽河176', '辽河203', '辽河204', '辽河236', '辽河239', '辽河243', '光岳286', '黄河293', '光岳315', '东环419', '东环464', '光岳559', '东环623', '滨河669', '黄河10']


// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:4999/"

// eslint-disable-next-line no-unused-vars
let scene, drawControl, lng1, lat1, lng2, lat2

// eslint-disable-next-line no-unused-vars
let color = [
  '#66cc77',
  '#44bb99',
  '#22aaaa',
  '#0099bb',
  '#0077dd',
  '#0088ee'
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
function d101() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + p1 + "/d101")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t101').innerHTML = p1 + "污染指数"
        document.getElementById('d101').innerHTML = ""
        const liquidPlot = new Liquid('d101', {
          percent: data['value'],
          shape: 'rect',
          outline: {
            border: 1,
            distance: 1,
          },
          color: color[0],
          statistic: {
            content: {
              style: {
                fontSize: 5,
                color: '#000'
              }
            }
          },
          wave: {
            length: 128,
          },
        });
        liquidPlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d102() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + p1 + "/d102")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t102').innerHTML = d + "日含量对比"
        document.getElementById('d102').innerHTML = ""
        const area = new Area('d102', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          smooth: true,
          areaStyle: {
            fillOpacity: 0.7,
          },

          isPercent: true,
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          h = jsonData['name'].replace("时", '')
          fHour()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d103() {
  fetch(localhost + y + "/" + m + "/" + p1 + "/" + airType + "/d103")
      .then((response) => response.json())
      .then((data) => {
        document.getElementById('t103').innerHTML = m + "月" + airType + "含量变化"
        document.getElementById('d103').innerHTML = ""
        const violinPlot = new Violin('d103', {
          data: data,
          xField: 'x',
          yField: 'y',
          color,
          legend: false,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
        });
        violinPlot.render();
        let jsonData = {}
        violinPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        violinPlot.on('plot:click', () => {
          d = jsonData['x'].replace("日", '')
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d104() {
  fetch(localhost + y + "/" + airType + "/d104")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t104').innerHTML = y + "年" + airType + "各站点含量对比"
        document.getElementById('d104').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d104'), {
          data,
          xField: '月',
          yField: '站点',
          colorField: 'value',
          sizeField: 'value',
          shape: 'circle',
          color,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          label: false,
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          m = jsonData['月'].replace("月", '')
          p3 = p2
          p2 = p1
          p1 = jsonData['站点']
          fMonth()
          fzhandian()
        });
      });
}


// eslint-disable-next-line no-unused-vars
function d105() {
  fetch(localhost + y + '/' + m + "/" + d + "/" + h + "/" + p1 + "/d10567")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t105').innerHTML = p1 + "空气质量模型"
        document.getElementById('d105').innerHTML = ""
        const bar = new RadialBar('d105', {
          data,
          xField: 'name',
          yField: 'value',
          color: color[0],
          radius: 0.8,
          innerRadius: 0.2,
          tooltip: {
            formatter: (datum) => {
              return {name: '污染气体', value: datum.value};
            },
          },
        });
        bar.render();
        let jsonData = {}
        bar.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bar.on('plot:click', () => {
          airType = jsonData['name']
          fairType()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d106() {
  fetch(localhost + y + '/' + m + "/" + d + "/" + h + "/" + p2 + "/d10567")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t106').innerHTML = p2 + "空气质量模型"
        document.getElementById('d106').innerHTML = ""
        const bar = new RadialBar('d106', {
          data,
          xField: 'name',
          yField: 'value',
          color: color[0],
          radius: 0.8,
          innerRadius: 0.2,
          tooltip: {
            formatter: (datum) => {
              return {name: '污染气体', value: datum.value};
            },
          },
        });
        bar.render();
        let jsonData = {}
        bar.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bar.on('plot:click', () => {
          airType = jsonData['name']
          fairType()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d107() {
  fetch(localhost + y + '/' + m + "/" + d + "/" + h + "/" + p3 + "/d10567")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t107').innerHTML = p3 + "空气质量模型"
        document.getElementById('d107').innerHTML = ""
        const bar = new RadialBar('d107', {
          data,
          xField: 'name',
          yField: 'value',
          color: color[0],
          radius: 0.8,
          innerRadius: 0.2,
          tooltip: {
            formatter: (datum) => {
              return {name: '污染气体', value: datum.value};
            },
          },
        });
        bar.render();
        let jsonData = {}
        bar.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bar.on('plot:click', () => {
          airType = jsonData['name']
          fairType()
        });
      })
}


// eslint-disable-next-line no-unused-vars
function d108() {
  fetch(localhost + y + "/" + m + '/' + d + "/" + k1 + "/d108")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t108').innerHTML = k1 + "今日车型数量波动"
        document.getElementById('d108').innerHTML = ""
        const barPlot = new Bar('d108', {
          data: data.reverse(),
          xField: 'value',
          yField: 'name',
          isRange: true,
          label: {
            position: 'middle',
            layout: [{type: 'adjust-color'}],
          },
          color: color[0],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          legend: false
        });
        barPlot.render();
        let jsonData = {}
        barPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        barPlot.on('plot:click', () => {
          carType4 = carType3
          carType3 = carType2
          carType2 = carType1
          carType1 = jsonData['name']
          fcarType()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d109() {
  fetch(localhost + y + '/' + m + "/" + d + '/' + k1 + '/' + carType1 + "/d109abc")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t109').innerHTML = carType1 + "占比"
        document.getElementById('d109').innerHTML = ""
        const progress = new Progress('d109', {
          percent: data['value'],
          autoFit: true,
          color: [color[0], '#fff'],
        });
        progress.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d110() {
  fetch(localhost + y + '/' + m + "/" + d + '/' + k1 + '/' + carType2 + "/d109abc")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t110').innerHTML = carType2 + "占比"
        document.getElementById('d110').innerHTML = ""
        const progress = new Progress('d110', {
          percent: data['value'],
          autoFit: true,
          color: [color[0], '#fff'],
        });
        progress.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d111() {
  fetch(localhost + y + '/' + m + "/" + d + '/' + k1 + '/' + carType3 + "/d109abc")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t111').innerHTML = carType3 + "占比"
        document.getElementById('d111').innerHTML = ""
        const progress = new Progress('d111', {
          percent: data['value'],
          autoFit: true,
          color: [color[0], '#fff'],
        });
        progress.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d112() {
  fetch(localhost + y + '/' + m + "/" + d + '/' + k1 + '/' + carType4 + "/d109abc")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t112').innerHTML = carType4 + "占比"
        document.getElementById('d112').innerHTML = ""
        const progress = new Progress('d112', {
          percent: data['value'],
          autoFit: true,
          color: [color[0], '#fff'],
        });
        progress.render();
      })
}


// eslint-disable-next-line no-unused-vars
function d113() {
  fetch(localhost + y + "/" + types1 + "/d113")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t113').innerHTML = y + "年" + types1 + "变化情况"
        document.getElementById('d113').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d113'), {
          autoFit: true,
          data: data['data'],
          xField: '日',
          yField: '月',
          colorField: 'value',
          legend: false,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
      });
}

// eslint-disable-next-line no-unused-vars
function d114() {
  fetch(localhost + y + "/" + types2 + "/d1145")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t114').innerHTML = types2 + "变化情况"
        document.getElementById('d114').innerHTML = ""
        const piePlot = new Pie('d114', {
          appendPadding: 5,
          data,
          angleField: 'value',
          colorField: 'name',
          color,
          radius: 0.75,
          label: {
            type: 'spider',
            labelHeight: 28,
            content: '{name}',
          },
          interactions: [{type: 'element-selected'}, {type: 'element-active'}],
        });
        piePlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d115() {
  fetch(localhost + y + "/" + types3 + "/d1145")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t115').innerHTML = types3 + "变化情况"
        document.getElementById('d115').innerHTML = ""
        const piePlot = new Pie('d115', {
          appendPadding: 5,
          data,
          angleField: 'value',
          colorField: 'name',
          color,
          radius: 0.75,
          label: {
            type: 'spider',
            labelHeight: 28,
            content: '{name}',
          },
          interactions: [{type: 'element-selected'}, {type: 'element-active'}],
        });
        piePlot.render();
      })
}


// eslint-disable-next-line no-unused-vars
function d201() {
  fetch(localhost + y + "/" + p1 + "/" + airType + "/d201")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t201').innerHTML = y + "年" + p1 + airType + "变化图"
        document.getElementById('d201').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d201'), {
          data: data['data'],
          xField: '日',
          yField: '月',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          m = jsonData['月'].replace("月", "")
          d = jsonData['日'].replace("日", "")
          d203()
          d204()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d202() {
  fetch(localhost + y + "/" + k1 + "/" + carType1 + "/d202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = y + "年" + k1 + carType1 + "流量变化图"
        document.getElementById('d202').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d202'), {
          data: data['data'],
          xField: '日',
          yField: '月',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          m = jsonData['月'].replace("月", "")
          d = jsonData['日'].replace("日", "")
          d203()
          d204()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d203() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + airType + "/d203")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t203').innerHTML = m + "月" + d + "日" + airType + "变化情况"
        document.getElementById('d203').innerHTML = ""
        const area = new Area('d203', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          isPercent: true,
          smooth: true,
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          h = jsonData['name'].replace("时", "")
          fHour()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d204() {
  fetch(localhost + y + "/" + m + "/" + k1 + "/d204")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t204').innerHTML = y + "年" + m + "月" + k1 + "车流量变化情况"
        document.getElementById('d204').innerHTML = ""
        const area = new Area('d204', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          smooth: true,
          slider: {
            start: 0,
            end: 0.25,
          },
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          d = jsonData['name'].split("日")[0]
          s = jsonData['name'].split("日")[1]
          fDay()
        });
      });
}


// eslint-disable-next-line no-unused-vars
function d301() {
  fetch(localhost + y + "/" + m + "/" + p1 + "/" + airType + "/d301_2")
      .then((res) => res.json())
      .then((data) => {
        let maxl = 50
        if (airType === 'CO') {
          maxl = 1.5
        }
        document.getElementById('t301').innerHTML = m + "月" + p1 + airType + "变化图"
        document.getElementById('d301').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d301'), {
          data,
          xField: '日',
          yField: '时',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: maxl,
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d = jsonData['日'].replace("日", '')
          h = jsonData['时'].replace("时", '')
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d302() {
  fetch(localhost + y + "/" + m + "/" + p2 + "/" + airType + "/d301_2")
      .then((res) => res.json())
      .then((data) => {
        let maxl = 50
        if (airType === 'CO') {
          maxl = 1.5
        }
        document.getElementById('t302').innerHTML = m + "月" + p2 + airType + "变化图"
        document.getElementById('d302').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d302'), {
          data,
          xField: '日',
          yField: '时',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: maxl,
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d = jsonData['日'].replace("日", '')
          h = jsonData['时'].replace("时", '')
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d303() {
  fetch(localhost + y + "/" + p1 + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t303').innerHTML = y + "年" + p1 + "污染数据变化情况"
        document.getElementById('d303').innerHTML = ""
        const area = new Area('d303', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          smooth: true,
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          m = jsonData['name'].replace("月", '')
          d301()
          d302()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d304() {
  fetch(localhost + y + "/" + p2 + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t304').innerHTML = y + "年" + p2 + "污染数据变化情况"
        document.getElementById('d304').innerHTML = ""
        const area = new Area('d304', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          smooth: true,
          areaStyle: {
            fillOpacity: 0.7,
          },
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          m = jsonData['name'].replace("月", '')
          d301()
          d302()
        });
      });
}


// eslint-disable-next-line no-unused-vars
function d401() {
  fetch(localhost + y + "/" + m + "/" + k1 + "/" + carType1 + "/d401_2")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t401').innerHTML = k1 + carType1 + "变化图"
        document.getElementById('d401').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d401'), {
          data: data['data'],
          xField: '日',
          yField: '时段',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d = jsonData['日'].replace("日", '')
          s = jsonData['时段']
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d402() {
  fetch(localhost + y + "/" + m + "/" + k2 + "/" + carType1 + "/d401_2")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t402').innerHTML = k2 + carType1 + "变化图"
        document.getElementById('d402').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d402'), {
          data: data['data'],
          xField: '日',
          yField: '时段',
          colorField: 'value',
          legend: true,
          color,
          coordinate: {
            // 坐标轴属性配置
            type: 'polar', // 极坐标
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0.8,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 12,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: {
              offset: 0,
              style: {
                fill: '#fff',
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)',
              },
            },
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d = jsonData['日'].replace("日", '')
          s = jsonData['时段']
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d403() {
  fetch(localhost + y + "/" + k1 + "/d403_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t403').innerHTML = y + "年" + k1 + "车流量变化情况"
        document.getElementById('d403').innerHTML = ""
        const area = new Area('d403', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          smooth: true,
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          m = jsonData['name'].replace("月", '')
          d401()
          d402()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d404() {
  fetch(localhost + y + "/" + k2 + "/d403_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t404').innerHTML = y + "年" + k2 + "车流量变化情况"
        document.getElementById('d404').innerHTML = ""
        const area = new Area('d404', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          smooth: true,
          areaStyle: {
            fillOpacity: 0.7,
          },
          yAxis: {
            label: {
              formatter: (value) => {
                return value * 100;
              },
            },
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          m = jsonData['name'].replace("月", '')
          d401()
          d402()
        });
      });
}


// eslint-disable-next-line no-unused-vars
function d501() {
  let chartDom = document.getElementById('d501');
  document.getElementById('t501').innerHTML = k1 + "卡口相似关系图"
  let myChart = echarts.init(chartDom);
  let option;

  // myChart.showLoading();
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + k1 + "/d501")
      .then((res) => res.json())
      .then((graph) => {
        // myChart.hideLoading();
        option = {
          title: false,
          tooltip: {},
          color,
          legend: [
            {
              selectedMode: 'single',
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
                  width: 3
                }
              }
            }
          ]
        };
        myChart.setOption(option);
        option && myChart.setOption(option);
      });
}

// eslint-disable-next-line no-unused-vars
function d502() {
  let carTypes = ['小型汽车', '大型汽车', '小型普通客车', '重型栏板货车', '普通二轮摩托车', '其它', '微型栏板货车', '大型普通客车', '中型栏板货车', '中型轿车', '轻型栏板货车', '大型轿车', '重型栏板半挂车', '中型普通客车']
  document.getElementById('t502').innerHTML = k1 + "流量管控"

  for (let i in carTypes) {
    let carName = carTypes[i]
    let div = document.createElement('div')
    let divId = 'd502' + i + 'p'
    document.getElementById('d502').appendChild(div)
    div.id = divId
    div.style.position = 'absolute'
    div.style.width = '38%'
    div.style.height = '6.5%'
    div.style.left = '1%'
    div.style.top = (i * 7 + 1).toString() + "%"
    div.style.color = '#000'
    div.innerHTML = carName + ":"

    div = document.createElement('input')
    divId = 'd502' + i + 'in'
    document.getElementById('d502').appendChild(div)
    div.id = divId
    div.style.position = 'absolute'
    div.style.width = '30%'
    div.style.height = '5%'
    div.style.right = '25%'
    div.style.top = (i * 7 + 1).toString() + "%"
    div.style.color = '#000'
    div.innerHTML = carName + ":"
    fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + k1 + "/" + carName + "/d502")
        .then((res) => res.json())
        .then((data) => {
          div.value = data['value']
        })
  }
}

// eslint-disable-next-line no-unused-vars
function d503() {
  for (let i = 1; i <= Math.min(k_arry.length, 18); i += 1) {
    // eslint-disable-next-line no-unused-vars
    let kakou = k_arry[i]
    // eslint-disable-next-line no-unused-vars
    let id = i
    let div = document.createElement('div')
    let divId = 'd503' + id
    document.getElementById('d503').appendChild(div)
    div.id = divId
    div.style.position = 'absolute'
    div.style.width = '16%'
    div.style.height = '33%'
    let columnId = id % 6
    let rowId = Math.ceil(id / 6) - 1
    div.style.left = (columnId * 16.6).toString() + "%"
    div.style.top = (rowId * 33).toString() + "%"
    div.style.borderStyle = 'inset'
    div.style.borderWidth = '2px'
    fetch(localhost + y + "/" + m + "/" + kakou + "/d503")
        .then((res) => res.json())
        .then((data) => {
          document.getElementById(divId).innerHTML = ""
          const radarPlot = new Radar(divId, {
            data: data['data'],
            autoFit: true,
            xField: 'name',
            yField: 'value',
            seriesField: 'type',
            meta: {
              score: {
                min: 0,
                max: data['max']
              },
            },
            color: color[0],
            xAxis: false,
            yAxis: false,
            // 开启辅助点
            point: {
              size: 2,
            },
          });
          radarPlot.render();
        })
  }
}


// eslint-disable-next-line no-unused-vars
function dl1() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + airType + "/l1")
      .then(res => res.json())
      .then(data => {
        l1.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function dl2() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/l2")
      .then((res) => res.json())
      .then((data) => {
        l2.setData(data)
        let jsonData = []
        drawControl.on('draw.create', (e) => {
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          jsonData = []
          k_arry = []
          for (let i in data) {
            if (Math.min(lng1, lng2) <= data[i]['jd'] && data[i]['jd'] <= Math.max(lng1, lng2)) {
              if (Math.min(lat1, lat2) <= data[i]['wd'] && data[i]['wd'] <= Math.max(lat1, lat2)) {
                jsonData.push(data[i])
                k_arry.push(data[i]['name'])
              }
            }
          }
          d503()
          l3 = new PointLayer({})
              .source(jsonData, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('words', 'text')
              .size('value', [8, 15])
              .color('value', ['#013', '#124', '#236'])
              .style({
                textAnchor: 'center', // 文本相对锚点的位置 center|left|right|top|bottom|top-left
                textOffset: [0, 0], // 文本相对锚点的偏移量 [水平, 垂直]
                spacing: 2, // 字符间距
                padding: [0.2, 0.2], // 文本包围盒 padding [水平，垂直]，影响碰撞检测结果，避免相邻文本靠的太近
                stroke: '#000', // 描边颜色
                strokeWidth: 0, // 描边宽度
                strokeOpacity: 0.7
              });
          scene.addLayer(l3);
        });
        drawControl.on('draw.update', (e) => {
          scene.removeLayer(l3)
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          jsonData = []
          k_arry = []
          for (let i in data) {
            if (Math.min(lng1, lng2) <= data[i]['jd'] && data[i]['jd'] <= Math.max(lng1, lng2)) {
              if (Math.min(lat1, lat2) <= data[i]['wd'] && data[i]['wd'] <= Math.max(lat1, lat2)) {
                jsonData.push(data[i])
                k_arry.push(data[i]['name'])
              }
            }
          }
          d503()
          l3 = new PointLayer({})
              .source(jsonData, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('words', 'text')
              .size('value', [8, 15])
              .color('value', ['#013', '#124', '#236'])
              .style({
                textAnchor: 'center', // 文本相对锚点的位置 center|left|right|top|bottom|top-left
                textOffset: [0, 0], // 文本相对锚点的偏移量 [水平, 垂直]
                spacing: 2, // 字符间距
                padding: [0.2, 0.2], // 文本包围盒 padding [水平，垂直]，影响碰撞检测结果，避免相邻文本靠的太近
                stroke: '#000', // 描边颜色
                strokeWidth: 0, // 描边宽度
                strokeOpacity: 0.7
              });
          scene.addLayer(l3);
        });
        drawControl.on('draw.delete', function () {
          scene.removeLayer(l3)
        });
      });
}

// eslint-disable-next-line no-unused-vars
function dl4() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType1 + "/l4")
      .then(res => res.json())
      .then(data => {
        l4.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function ftime() {
  document.getElementById('time').innerHTML = y + "-" + m + "-" + d + "  " + h + ":00:00"
}

// eslint-disable-next-line no-unused-vars
function fYear() {
  ftime()

  d101()
  d102()
  d103()
  d104()
  d105()
  d106()
  d107()
  d108()
  d109()
  d110()
  d111()
  d112()
  d113()
  d114()
  d115()

  dl1()
  dl2()
  dl4()

  d201()
  d202()
  d203()
  d204()


  d503()
  d502()
}

// eslint-disable-next-line no-unused-vars
function fMonth() {
  ftime()

  d101()
  d102()
  d103()
  d105()
  d106()
  d107()
  d108()
  d109()
  d110()
  d111()
  d112()

  dl1()
  dl2()
  dl4()

  d203()
  d204()

  d502()
  d503()
}

// eslint-disable-next-line no-unused-vars
function fDay() {
  ftime()

  dl1()
  dl2()
  dl4()


  d101()
  d102()
  d105()
  d106()
  d107()
  d108()
  d109()
  d110()
  d111()
  d112()

  d203()

  d502()
}

// eslint-disable-next-line no-unused-vars
function fHour() {
  if (h >= 2 && h <= 4) {
    s = '2:00-4:00';
    fShiduan()
  }
  if (h >= 7 && h <= 9) {
    s = '7:00-9:00';
    fShiduan()
  }
  if (h >= 10 && h <= 12) {
    s = '10:00-12:00';
    fShiduan()
  }
  if (h >= 17 && h <= 19) {
    s = '17:00-19:00';
    fShiduan()
  }


  dl1()
  dl4()

  ftime()
  d101()
  d105()
  d106()
  d107()


}

// eslint-disable-next-line no-unused-vars
function fShiduan() {
  dl2()

  d502()
}

// eslint-disable-next-line no-unused-vars
function fairType() {
  d103()
  d104()
  dl1()

  d201()
  d203()

  d301()
  d302()
}

// eslint-disable-next-line no-unused-vars
function fcarType() {
  dl4()

  d109()
  d110()
  d111()
  d112()

  d202()

  d401()
  d402()
}

// eslint-disable-next-line no-unused-vars
function fkakou() {
  d108()
  d109()
  d110()
  d111()
  d112()

  d202()
  d204()

  d401()
  d402()
  d403()
  d404()

  d501()
  d502()
}

// eslint-disable-next-line no-unused-vars
function fzhandian() {
  d101()
  d102()
  d103()

  d105()
  d106()
  d107()

  d201()

  d301()
  d302()
  d303()
  d304()

}

// eslint-disable-next-line no-unused-vars
function init() {
  addListOption('s2', ['小型汽车', '大型汽车', '小型普通客车', '重型栏板货车', '普通二轮摩托车', '其它', '微型栏板货车', '大型普通客车', '中型栏板货车', '中型轿车', '轻型栏板货车', '大型轿车', '重型栏板半挂车', '中型普通客车'])
  addListOption('s1', ['SO2', 'CO', 'NO2', 'O3', 'PM10', 'PM2.5'])


  ftime()

  d101()
  d102()
  d103()
  d104()
  d105()
  d106()
  d107()
  d108()
  d109()
  d110()
  d111()
  d112()
  d113()
  d114()
  d115()

  d201()
  d202()
  d203()
  d204()

  d301()
  d302()
  d303()
  d304()

  d401()
  d402()
  d403()
  d404()


  d501()
  d502()
  d503()


  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + airType + "/l1")
      .then(res => res.json())
      .then(data => {
        l1 = new PointLayer({})
            .source(data, {
              parser: {
                type: 'json',
                x: 'jd',
                y: 'wd'
              }
            })
            .shape('circle')
            .size('value', [8, 16])
            .color('value', color)
            .active(true)
            .style({
              opacity: 0.5,
              strokeWidth: 0
            });
        scene.addLayer(l1);
        l1.on('click', ev => {
          p3 = p2
          p2 = p1
          p1 = ev.feature['name']
          fzhandian()
          const popup = new Popup({
            offsets: [0, 0],
            closeButton: false
          })
              .setLnglat(ev.lngLat)
              .setHTML(
                  `<span style="color: #777">${ev.feature['name']}</span>`
              );
          scene.addPopup(popup);
        })
      });


  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/l2")
      .then((res) => res.json())
      .then((data) => {
        l2 = new PointLayer({})
            .source(data, {
              parser: {
                type: 'json',
                x: 'jd',
                y: 'wd'
              }
            })
            .shape('circle')
            .size('value', [8, 32])
            .color('value', color)
            .active(true)
            .animate({})
            .style({
              opacity: 0.9,
              strokeWidth: 0
            });
        scene.addLayer(l2)
        l2.hide()
        l2.on('click', ev => {
          k3 = k2
          k2 = k1
          k1 = ev['feature']['name']
          fkakou()
          const popup = new Popup({
            offsets: [0, 0],
            closeButton: false
          })
              .setLnglat(ev.lngLat)
              .setHTML(
                  `<span style="color: #777">${ev.feature['name']}</span>`
              );
          scene.addPopup(popup);
        })
      })


  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType1 + "/l4")
      .then(res => res.json())
      .then(data => {
        l4 = new HeatmapLayer({})
            .source(data, {
              parser: {
                x: 'jd',
                y: 'wd',
                type: 'json'
              }
            })
            .shape('arc3d')
            .size('value', [0, 1.0]) // weight映射通道
            .style({
              intensity: 2,
              radius: 20,
              opacity: 1.0,
              rampColors: {
                colors: color,
                positions: [0, 0.2, 0.4, 0.6, 0.8, 1.0]
              }
            });
        scene.addLayer(l4);
        l4.hide()
      });

  dl2()
}

export default {
  name: "app",
  components: {
    phone
  },
  data() {
    return {
      p1: 0,
      p2: 0,
      p3: 0,
      p4: 0,
      p5: 1,

      phone: 0,

      l1: 1,
      l2: 0,
      l4: 0,

      buttonColor1: '#ffff00',
      buttonColor2: '#ffffff',


    }
  },
  methods: {
    fphone() {
      this.phone = !this.phone
    },
    fp1: function () {
      document.getElementById('bp1').style.color = this.buttonColor1
      document.getElementById('bp2').style.color = this.buttonColor2
      document.getElementById('bp3').style.color = this.buttonColor2
      document.getElementById('bp4').style.color = this.buttonColor2
      document.getElementById('bp5').style.color = this.buttonColor2

      this.p1 = 1
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
      this.p5 = 0
    },
    fp2: function () {
      document.getElementById('bp1').style.color = this.buttonColor2
      document.getElementById('bp2').style.color = this.buttonColor1
      document.getElementById('bp3').style.color = this.buttonColor2
      document.getElementById('bp4').style.color = this.buttonColor2
      document.getElementById('bp5').style.color = this.buttonColor2

      this.p1 = 0
      this.p2 = 1
      this.p3 = 0
      this.p4 = 0
      this.p5 = 0
    },
    fp3: function () {
      document.getElementById('bp1').style.color = this.buttonColor2
      document.getElementById('bp2').style.color = this.buttonColor2
      document.getElementById('bp3').style.color = this.buttonColor1
      document.getElementById('bp4').style.color = this.buttonColor2
      document.getElementById('bp5').style.color = this.buttonColor2

      this.p1 = 0
      this.p2 = 0
      this.p3 = 1
      this.p4 = 0
      this.p5 = 0
    },
    fp4: function () {
      document.getElementById('bp1').style.color = this.buttonColor2
      document.getElementById('bp2').style.color = this.buttonColor2
      document.getElementById('bp3').style.color = this.buttonColor2
      document.getElementById('bp4').style.color = this.buttonColor1
      document.getElementById('bp5').style.color = this.buttonColor2

      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 1
      this.p5 = 0
    },
    fp5: function () {
      document.getElementById('bp1').style.color = this.buttonColor2
      document.getElementById('bp2').style.color = this.buttonColor2
      document.getElementById('bp3').style.color = this.buttonColor2
      document.getElementById('bp4').style.color = this.buttonColor2
      document.getElementById('bp5').style.color = this.buttonColor1

      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
      this.p5 = 1
    },


    fAir() {
      airType = selectTxt('s1')
      fairType()
    },
    fCar() {
      carType4 = carType3
      carType3 = carType2
      carType2 = carType1
      carType1 = selectTxt('s2')
      fcarType()
    },
    tijiao() {
      this.$message({
        showClose: true,
        message: '提交成功',
        type: 'success'
      });
    },


    fl1() {
      this.l1 = !this.l1
      let flag = !this.l1
      if (flag) {
        l1.hide()
      } else {
        l1.show()
      }
    },
    fl2() {
      this.l2 = !this.l2
      let flag = !this.l2
      if (flag) {
        l2.hide()
      } else {
        l2.show()
      }
    },
    fl4() {
      this.l4 = !this.l4
      let flag = !this.l4
      if (flag) {
        l4.hide()
      } else {
        l4.show()
      }
    },

    addHour() {
      h += 1
      h %= 24
      fHour()
    },
    reduceHour() {
      h += 23
      h %= 24
      fHour()
    },

  },
  mounted() {

    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        style: '',
        center: [116.025774, 36.460699],
        pitch: 30,
        zoom: 9
      })
    });

    drawControl = new DrawControl(scene, {
      position: 'topright',
      layout: 'horizontal', // horizontal vertical
      controls: {
        point: false,
        polygon: false,
        line: false,
        circle: false,
        rect: true,
        delete: true
      }
    });
    scene.addControl(drawControl);


    init()

  }

}
</script>

<style scoped>
html, body {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  color: #000
}

.content {
  position: absolute;
  width: 100%;
  height: 90%;
  left: 0;
  top: 25px;
  text-align: center;
  font-size: 20%;
  color: #fff;
  font-weight: bold;
  border-style: groove;
  border-width: 1px;
}

.title {
  position: absolute;
  width: 100%;
  height: 24px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 16px;
  color: #fff;
  background-color: #88ADA8;
  font-weight: bold;
  border-style: groove;
  border-width: 1px;
}

.divs {
  position: absolute;
  /*background-color: #fff;*/
  text-align: center;
  border-width: 1px;
  border-color: #222;
}

.selects {
  position: absolute;
  width: 70px;
  height: 20px;
  background-color: #fff;
  border-color: #0ab;
  border-width: 2px;
  /*border-style: inset;*/
  color: #005;
  border-radius: 5px;
  z-index: 9999;
  font-size: 5px;
  font-weight: bold;
  text-align: center;
}
</style>