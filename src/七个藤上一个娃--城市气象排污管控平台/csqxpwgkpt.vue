<template>
  <div class="divs" style="position: absolute;width: 99%; height: 100%; left: 0.5%; top: 0; background-color: #fff">
    <div class="titles">汽 车 排 气 污 染 管 控 平 台</div>
    <div class="contents">
      <div class="divs" style="position: absolute; left: 55%; top: 40%; width: 17%; height: 39%">
        <div class="titles">控制台</div>
        <div class="contents">
          <template>
            <el-button type="success" @click="fl1" size="mini">卡口流量散点</el-button>
            <el-button type="warning" @click="fl2" size="mini">检测站点气象</el-button>
            <br>
            <el-button type="info" @click="fl3" size="mini">流量转移飞线</el-button>
            <el-button type="danger" @click="fl4" size="mini">实时风场轨迹</el-button>
            <br>
            <div class="block">
              <el-date-picker
                  v-model="value"
                  align="right"
                  type="date"
                  placeholder="选择日期"
                  @change=getDate(value)
                  :picker-options="pickerOptions">
              </el-date-picker>
            </div>
            <el-time-select
                style="width: 110px"
                v-model="startHour"
                @change=getStartHour(startHour)
                :picker-options="{
                  start: '00:00',
                  step: '01:00',
                  end: '23:00'
                }"
                placeholder="起始时间">
            </el-time-select>
            <el-time-select
                @change=getEndHour(endHour)
                style="width: 110px"
                v-model="endHour"
                :picker-options="{
                  start: '00:00',
                  step: '01:00',
                  end: '23:00'
                }"
                placeholder="截止时间">
            </el-time-select>
            <br>
          </template>
        </div>
      </div>

      <div class="divs" style="position: absolute; left: 0; top: 0; width: 54%; height: 79%">
        <div class="titles"></div>
        <div class="contents" id="d101" style="height: 92%"></div>
      </div>
      <div class="divs" style="position: absolute; left: 0; top: 80%; width: 17.5%; height: 39%">
        <div class="titles" id="t102"></div>
        <div class="contents" id="d102"></div>
      </div>
      <div class="divs" style="position: absolute; left: 18%; top: 80%; width: 17.5%; height: 39%">
        <div class="titles" id="t103"></div>
        <div class="contents" id="d103"></div>
      </div>
      <div class="divs" style="position: absolute; left: 36%; top: 80%; width: 18%; height: 39%">
        <div class="titles" id="t104"></div>
        <div class="contents" id="d104"></div>
      </div>
      <div class="divs" style="position: absolute; left: 55%; top: 0; width: 22%; height: 39%">
        <div class="titles" id="t105"></div>
        <div class="contents" id="d105"></div>
      </div>
      <div class="divs" style="position: absolute; left: 78%; top: 0; width: 22%; height: 39%">
        <div class="titles" id="t106"></div>
        <div class="contents" id="d106"></div>
      </div>
      <div class="divs" style="position: absolute; left: 55%; top: 80%; width: 17%; height: 39%">
        <div class="titles" id="t107"></div>
        <div class="contents" id="d107"></div>
      </div>
      <div class="divs" style="position: absolute; left: 73%; top: 40%; width: 27%; height: 26%">
        <div class="titles" id="t108"></div>
        <div class="contents" id="d108"></div>
      </div>
      <div class="divs" style="position: absolute; left: 73%; top: 67%; width: 27%; height: 26%">
        <div class="titles" id="t109"></div>
        <div class="contents" id="d109"></div>
      </div>
      <div class="divs" style="position: absolute; left: 73%; top: 94%; width: 27%; height: 25%">
        <div class="titles" id="t110"></div>
        <div class="contents" id="d110" style="font-size: 2px; font-weight: bold"></div>
      </div>


      <div v-show="p11_15" class="divs"
           style="position: absolute; left: 0; top: 5%; width: 9%; height: 25%; opacity: 0.8">
        <div class="titles" id="t111"></div>
        <div class="contents" id="d111"></div>
      </div>
      <div v-show="p11_15" class="divs"
           style="position: absolute; left: 45%; top: 5%; width: 9%; height: 25%; opacity: 0.8">
        <div class="titles" id="t112"></div>
        <div class="contents" id="d112"></div>
      </div>
      <div v-show="p11_15" class="divs"
           style="position: absolute; left: 9%; top: 55%; width: 36%; height: 24%; opacity: 0.8">
        <div class="titles" id="t115"></div>
        <div class="contents" id="d115"></div>
      </div>
      <div v-show="p11_15" class="divs"
           style="position: absolute; left: 0; top: 30%; width: 9%; height: 49%; opacity: 0.8">
        <div class="titles" id="t113"></div>
        <div class="contents" id="d113"></div>
      </div>
      <div v-show="p11_15" class="divs"
           style="position: absolute; left: 45%; top: 30%; width: 9%; height: 49%; opacity: 0.8">
        <div class="titles" id="t114"></div>
        <div class="contents" id="d114"></div>
      </div>


      <div v-show="p16" class="divs"
           style="position: absolute; left: 55%; top: 0; width: 45%; height: 39%;">
        <div style="position:absolute; height: 100%; width: 25%; left: 0; top: 0">
          <div class="titles" id="t1161"></div>
          <div class="contents" id="d1161"></div>
        </div>
        <div style="position:absolute; height: 100%; width: 25%; left: 25%; top: 0">
          <div class="titles" id="t1162"></div>
          <div class="contents" id="d1162"></div>
        </div>
        <div style="position:absolute; height: 100%; width: 25%; left: 50%; top: 0">
          <div class="titles" id="t1163"></div>
          <div class="contents" id="d1163"></div>
        </div>
        <div style="position:absolute; height: 100%; width: 25%; left: 75%; top: 0">
          <div class="titles" id="t1164"></div>
          <div class="contents" id="d1164"></div>
        </div>
      </div>


      <div v-show="p1101" class="divs" style="position: absolute; left: 73%; top: 40%; width: 27%; height: 53%">
        <div class="titles" id="t1101"></div>
        <div class="contents" id="d1101" style="font-size: 2px; font-weight: bold"></div>
        <div class="selects" style="height: 6%; width: 9%; left: 1%; top: 1%;" @click="f1101">返回</div>
      </div>


      <select id="d104Type"
              @change=fD104Type
              class="selects"
              style="left: 56%; top: 67%;"></select>
      <select id="year"
              @change=fYear
              class="selects"
              style="left: 61%; top: 67%;"></select>

    </div>
  </div>
</template>

<script>

// eslint-disable-next-line no-unused-vars
import {GaodeMap, LineLayer} from "@antv/l7";

// eslint-disable-next-line no-unused-vars
import {Scene, PointLayer, Popup} from '@antv/l7';

// eslint-disable-next-line no-unused-vars
import {
  // eslint-disable-next-line no-unused-vars
  Chord,
  Radar,
  Sankey,
  Heatmap,
  Sunburst,
  Scatter,
  Bullet,
  // eslint-disable-next-line no-unused-vars
  CirclePacking,
  // eslint-disable-next-line no-unused-vars
  Rose,
  Bar,
  Liquid,
  Area
} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
import * as echarts from 'echarts';

// eslint-disable-next-line no-unused-vars
import {DrawControl} from "@antv/l7-draw";

// eslint-disable-next-line no-unused-vars
import {Mix} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
import insertCss from 'insert-css';


// eslint-disable-next-line no-unused-vars
let color = [
  '#086568',
  '#337060',
  '#656f55',
  '#917F54',
  '#9B8471',
  '#bb9979',
  '#ddaa88',
].reverse()

// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:2022/'

// eslint-disable-next-line no-unused-vars
let scene, l1, l2, l3, l4, l5

// eslint-disable-next-line no-unused-vars
let y = 2021, m = 6, d = 30, h = 8, s = '17:00-19:00', hLength1 = 0, hLength2 = 8

// eslint-disable-next-line no-unused-vars
let p1 = '海关', p2 = '区政府', d102Type = 'AQI', d104Type = '气温', d107Type = '降水量', airType = 'SO2', carType = '小型普通客车',
// eslint-disable-next-line no-unused-vars
    kakou = '黄河10', k1 = '黄河10', k2 = '东外33', k3 = '滦河66', k4 = '黄河258', kNum = 1

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
function d102() {
  fetch(localhost + y + '/d102')
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t102').innerHTML = y + "年降水量分布图"
        document.getElementById('d102').innerHTML = ""
        const plot = new Sunburst('d102', {
          data,
          innerRadius: 0.2,
          interactions: [{type: 'element-active'}],
          color,
        });
        plot.render();
        let jsonData = {}
        plot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        plot.on('plot:click', ev => {
          ev = ""
          if (jsonData['path'].indexOf("月") !== -1) {
            m = jsonData['path'].replace("月", '') + ev
            initM()
          }
          if (jsonData['path'].indexOf("日") !== -1) {
            d = jsonData['path'].replace("日", '') + ev
            initD()
          }
          if (jsonData['path'].indexOf("时") !== -1) {
            h = jsonData['path'].replace("时", '') + ev
            initH()
          }
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d103() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + p1 + "/" + p2 + "/d103")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t103').innerHTML = "站点污染模型"
        document.getElementById('d103').innerHTML = ""
        const radarPlot = new Radar('d103', {
          data: data['data'],
          xField: 'type',
          yField: 'value',
          seriesField: 'name',
          color: [color[0], color[5]],
          meta: {
            score: {
              min: 0,
              max: data['max'],
            },
          },
          xAxis: {
            line: null,
            tickLine: null,
            grid: null,
            label: {
              offset: 12,
              style: {
                fill: '#666',
                fontSize: 8,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            label: false,
          },
          // 开启面积
          area: {},
          // 开启辅助点
          point: {
            size: 2,
          },
        });
        radarPlot.render();
        let jsonData = {}
        radarPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        radarPlot.on('plot:click', ev => {
          ev = ""
          airType = ev + jsonData['type']
          initAirType()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d104() {
  fetch(localhost + y + "/" + selectTxt('d104Type') + "/d104")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t104').innerHTML = y + "年" + selectTxt('d104Type') + "极坐标色块"
        document.getElementById('d104').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d104'), {
          data: data['data'],
          xField: '月',
          yField: '日',
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
            stroke: null,
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
                fontSize: 10,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: false,
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
          initM()
          d1041()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d1041() {
  fetch(localhost + y + "/" + m + "/" + selectTxt('d104Type') + "/d1041")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t104').innerHTML = y + "年" + m + "月" + selectTxt('d104Type') + "极坐标色块"
        document.getElementById('d104').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d104'), {
          data: data['data'],
          xField: '日',
          yField: '时',
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
            stroke: null,
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
                fontSize: 10,
                textBaseline: 'top',
              },
            },
          },
          yAxis: {
            top: true,
            line: null,
            grid: null,
            tickLine: null,
            label: false,
          },
          tooltip: {
            showMarkers: false,
          },
          interactions: [{type: 'element-active'}],
        });
        heatmapPlot.render();
        // eslint-disable-next-line no-unused-vars
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d104()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d105() {
  fetch(localhost + y + "/" + p1 + "/" + airType + "/d105")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t105').innerHTML = y + "年" + airType + "风速关系热力图"
        document.getElementById('d105').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d105'), {
          data,
          xField: '月',
          yField: '日',
          colorField: '风速',
          sizeField: 'size',
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
          m = jsonData['月'].replace("月", "")
          d = jsonData['日'].replace("日", "")
          initM()
          d1051()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d1051() {
  fetch(localhost + y + "/" + m + "/" + p1 + "/" + airType + "/d1051")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t105').innerHTML = y + "年" + m + "月" + airType + "风速关系热力图"
        document.getElementById('d105').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d105'), {
          data,
          xField: '日',
          yField: '时',
          colorField: '风速',
          sizeField: 'size',
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
        // eslint-disable-next-line no-unused-vars
        let jsonData = {}
        heatmapPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        heatmapPlot.on('plot:click', () => {
          d105()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d106() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + carType + "/d106")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t106').innerHTML = y + "年" + m + "月" + d + "日" + carType + "流量流动图"
        document.getElementById('d106').innerHTML = ""
        const sankey = new Sankey('d106', {
          data,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          color,
          nodeWidthRatio: 0.008,
          nodePaddingRatio: 0.03,
        });

        sankey.render();
      });
}

// eslint-disable-next-line no-unused-vars
function d107() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + kakou + "/d107")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t107').innerHTML = kakou + s + "流量分布"
        document.getElementById('d107').innerHTML = ""

        data = data.sort(function (x, y) {
          return y.过车数量 - x.过车数量
        })
        const column = new Bar('d107', {
          data,
          yField: '车辆类型',
          xField: '过车数量',
          color,
          seriesField: '车辆类型',
          yAxis: {
            label: {
              autoRotate: false,
            },
            grid: null
          },
          xAxis: {
            grid: null
          },
          scrollbar: {
            type: 'vertical',
          },
        });

        column.render();
        // const rosePlot = new Rose('d107', {
        //   data,
        //   xField: '车辆类型',
        //   yField: '过车数量',
        //   color,
        //   seriesField: '车辆类型',
        //   radius: 0.9,
        //   legend: {
        //     position: 'bottom',
        //   },
        // });

        // rosePlot.render();

        let jsonData = {}
        column.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        column.on('plot:click', ev => {
          ev = ""
          carType = ev + jsonData['车辆类型']
          initCarType()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d108() {
  fetch(localhost + y + "/" + m + "/" + d + "/d108")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t108').innerHTML = y + "年" + m + "月" + d + "日" + "卡口流量散点图"
        document.getElementById('d108').innerHTML = ""
        const scatterPlot = new Scatter('d108', {
          data,
          xField: '卡口名称',
          yField: '过车数量',
          shape: 'circle',
          colorField: '车辆类型',
          color,
          size: 2,
          brush: {
            enabled: true,
            mask: {
              style: {
                fill: 'rgba(255,0,0,0.15)',
              },
            },
          },
          yAxis: {
            grid: null
          },
          xAxis: {
            grid: null
          },
        });
        scatterPlot.render();
      });

}

// eslint-disable-next-line no-unused-vars
function d109() {
// 我们用 insert-css 演示引入自定义样式
// 推荐将样式添加到自己的样式文件中
// 若拷贝官方代码，别忘了 npm install insert-css
// 我们用 insert-css 演示引入自定义样式
// 推荐将样式添加到自己的样式文件中
// 若拷贝官方代码，别忘了 npm install insert-css
  insertCss(`
    .custom-tooltip-title {
        margin: 0px 12px;
        padding: 72px 0 8px;
        font-size: 12px;
        border-bottom-style: solid;
        border-bottom-width: thin;
        border-bottom-color: #e9e9e9;
    }

    .custom-tooltip-value {
      display: grid;
      grid-template-columns: 1fr 1fr;
      margin: 8px 12px 0 12px;
      padding-bottom: 8px;
      font-size: 40px;
      text-align: center;
      border-bottom-style: solid;
      border-bottom-width: thin;
      border-bottom-color: #e9e9e9;
      height: 70px;
    }

    .custom-tooltip-temp {
      display: flex;
      position: relative;
      align-items: center;
    }

    .custom-tooltip-temp span:first-child {
      font-size: 12px;
      position: absolute;
      top: 0px;
      color: rgba(0, 0, 0, 0.45)
    }

    .custom-tooltip-temp span:last-child {
      text-align: left;
      margin-top: 10px;
      position: relative;
      color: rgba(0, 0, 0, 0.85)
    }

    .custom-tooltip-wind {
        margin: 8px 12px 12px 12px;
        font-size: 10px;
        color: rgba(0, 0, 0, 0.45);
        display: grid;
        grid-template-columns: 1fr 1fr;
    }

    .tooltip-footer {
      margin: 8px 12px 12px 12px;
      font-size: 10px;
      color: rgba(0, 0, 0, 0.45);
    }

    .background-image {
      background-repeat: no-repeat;
    }

    .rain {
        background-image: url(https://gw.alipayobjects.com/mdn/rms_2274c3/afts/img/A*sg5aT7dY36wAAAAAAAAAAABkARQnAQ);
    }

    .sun {
        background-image: url(https://gw.alipayobjects.com/mdn/rms_2274c3/afts/img/A*gE_hS5JVl5YAAAAAAAAAAABkARQnAQ);
    }

    .cloud {
        background-image: url(https://gw.alipayobjects.com/mdn/rms_2274c3/afts/img/A*BTw4R4O341AAAAAAAAAAAABkARQnAQ);
    }
`);

  fetch(localhost + y + "/" + m + "/d109")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t109').innerHTML = y + "年" + m + "月气象走势图"
        document.getElementById('d109').innerHTML = ""
        const plot = new Mix('d109', {
          color,
          meta: {
            date: {sync: true},
            minTemp: {min: 0, max: 40},
            maxTemp: {min: 0, max: 40},
            values: {min: 0, max: 40},
          },
          tooltip: {
            showMarkers: false,
            enterable: true,
            domStyles: {
              'g2-tooltip': {
                width: '150px',
                padding: 0,
              },
            },
            customContent: (title, items) => {
              const data = items[0].data || {};
              const titleDom = `<div class ="custom-tooltip-title">${data.date}</div>`;
              const tempDom = `<div class = "custom-tooltip-value"><div class = "custom-tooltip-temp"><span>低温</span><span style="font-size: 10px">${data.minTemp}℃</span></div><div class = "custom-tooltip-temp"><span>高温</span><span style="font-size: 10px">${data.maxTemp}℃</span></div></div>`;
              const windDom = `<div class = "custom-tooltip-wind"><span>风向:${data.windDir}</span><span>风速:${data.windSpeed}</span></div>`;
              let domClass;
              if (data.rain === 1) {
                domClass = 'rain';
              } else if (data.sunny === 1) {
                domClass = 'sun';
              } else {
                domClass = 'cloud';
              }
              return `<div class="background-image ${domClass}">${titleDom}${tempDom}${windDom}<div class="tooltip-footer">打开 <a href="https://weather.com/zh-CN/weather/today/l/871e71008a65cba13e27214b56f50d23bc1edf900d3401fd1c03b72e188af569" target="_blank">天气预报网 ☁️</a></div></div>`;
            },
          },
          views: [
            {
              data: data.map((d) => {
                return {...d, values: [d.minTemp, d.maxTemp]};
              }),
              meta: {
                date: {sync: true},
                minTemp: {min: 0, max: 40},
                maxTemp: {min: 0, max: 40},
                values: {min: 0, max: 40},
              },
              axes: {
                date: {},
                minTemp: false,
                maxTemp: false,
                values: {
                  position: 'left',
                },
              },
              interactions: [{type: 'active-region'}],
              geometries: [
                {
                  type: 'interval',
                  xField: 'date',
                  yField: 'values',
                  mapping: {
                    size: 4,
                    style: {fill: '#EBEDF0'},
                  },
                },
                {
                  type: 'point',
                  xField: 'date',
                  yField: 'minTemp',
                  colorField: 'maxTemp',
                  mapping: {
                    style: {r: 5},
                    shape: 'circle',
                    color,
                  },
                },
                {
                  type: 'point',
                  xField: 'date',
                  yField: 'maxTemp',
                  colorField: 'maxTemp',
                  mapping: {
                    size: 5,
                    shape: 'circle',
                    color,
                  },
                },
              ],
            },
          ],
        });

        plot.render();
      });

}

// eslint-disable-next-line no-unused-vars
function d110() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + k1 + "/" + k2 + "/" + k3 + "/" + k4 + "/" + carType + "/d110")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t110').innerHTML = carType + '流量配置建议'
        document.getElementById('d110').innerHTML = ""
        const bulletPlot = new Bullet('d110', {
          data,
          measureField: 'measures',
          rangeField: 'ranges',
          targetField: 'target',
          xField: 'title',
          color: {
            range: color,
            measure: color[4],
            target: color[5],
          },
          label: {},
          xAxis: {
            grid: null
          },
          yAxis: false,
          // 自定义 legend
          legend: {
            custom: true,
            position: 'bottom',
            items: [
              {
                value: '优',
                name: '优',
                marker: {symbol: 'square', style: {fill: color[0], r: 5}},
              },
              {
                value: '良',
                name: '良',
                marker: {symbol: 'square', style: {fill: color[1], r: 5}},
              },
              {
                value: '差',
                name: '差',
                marker: {symbol: 'square', style: {fill: color[2], r: 5}},
              },
              {
                value: '实际值',
                name: '实际值',
                marker: {symbol: 'square', style: {fill: color[3], r: 5}},
              },
              {
                value: '目标值',
                name: '目标值',
                marker: {symbol: 'line', style: {stroke: color[4], r: 5}},
              },
            ],
          },
        });
        bulletPlot.render();
        let jsonData = {}
        bulletPlot.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bulletPlot.on('plot:click', () => {
          kakou = jsonData['title']
          d107()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d111() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + p1 + "/d111_112")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t111').innerHTML = p1 + "污染指数"
        document.getElementById('d111').innerHTML = ""
        const liquidPlot = new Liquid('d111', {
          percent: data[0]["污染指数"],
          outline: {
            border: 4,
            distance: 8,
          },
          color: color[0],
          wave: {
            length: 128,
          },
        });
        liquidPlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d112() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + h + "/" + p2 + "/d111_112")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t112').innerHTML = p2 + "污染指数"
        document.getElementById('d112').innerHTML = ""
        const liquidPlot = new Liquid('d112', {
          percent: data[0]["污染指数"],
          outline: {
            border: 4,
            distance: 8,
          },
          wave: {
            length: 128,
          },
          color: color[0]
        });
        liquidPlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d113() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + p1 + "/" + airType + "/d113_114")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t113').innerHTML = airType + "趋势图"
        document.getElementById('d113').innerHTML = ""
        const bar = new Bar('d113', {
          data,
          xField: 'value',
          yField: '时间',
          seriesField: 'value',
          color,
          xAxis: {
            grid: null
          },
          // legend: {
          //   position: 'top-left',
          // },
        });
        bar.render();

        let jsonData = {}
        bar.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bar.on('plot:click', () => {
          h = jsonData['时间'].replace("时", "")
          initH()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d114() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + p2 + "/" + airType + "/d113_114")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t114').innerHTML = airType + "趋势图"
        document.getElementById('d114').innerHTML = ""
        const bar = new Bar('d114', {
          data,
          xField: 'value',
          yField: '时间',
          seriesField: 'value',
          color,
          xAxis: {
            grid: null
          },
          // legend: {
          //   position: 'top-left',
          // },
        });
        bar.render();

        let jsonData = {}
        bar.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        bar.on('plot:click', () => {
          h = jsonData['时间'].replace("时", "")
          initH()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function d115() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + p1 + "/" + p2 + "/" + airType + "/d115")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t115').innerHTML = airType + "对比图"
        document.getElementById('d115').innerHTML = ""
        const area = new Area('d115', {
          data,
          xField: '时间',
          yField: 'value',
          seriesField: '站点',
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
          color: [color[0], color[5]],
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', ev => {
          jsonData = ev.data.items[0].data
        });
        area.on('plot:click', () => {
          h = jsonData['时间'].replace("时", "")
          initH()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d116() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + k1 + "/d116")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1161').innerHTML = k1 + "当日过车情况"
        document.getElementById('d1161').innerHTML = ""
        const rosePlot = new Rose('d1161', {
          data,
          xField: '车辆类型',
          yField: '过车数量',
          seriesField: '车辆类型',
          radius: 0.9,
          label: {
            offset: -15,
          },
          color,
          legend: {
            position: 'bottom',
          },
        });

        rosePlot.render();
      })

  fetch(localhost + y + "/" + m + "/" + d + "/" + k2 + "/d116")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1162').innerHTML = k2 + "当日过车情况"
        document.getElementById('d1162').innerHTML = ""
        const rosePlot = new Rose('d1162', {
          data,
          xField: '车辆类型',
          yField: '过车数量',
          seriesField: '车辆类型',
          radius: 0.9,
          label: {
            offset: -15,
          },
          color,
          legend: {
            position: 'bottom',
          },
        });

        rosePlot.render();
      })

  fetch(localhost + y + "/" + m + "/" + d + "/" + k3 + "/d116")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1163').innerHTML = k3 + "当日过车情况"
        document.getElementById('d1163').innerHTML = ""
        const rosePlot = new Rose('d1163', {
          data,
          xField: '车辆类型',
          yField: '过车数量',
          seriesField: '车辆类型',
          radius: 0.9,
          label: {
            offset: -15,
          },
          color,
          legend: {
            position: 'bottom',
          },
        });

        rosePlot.render();
      })

  fetch(localhost + y + "/" + m + "/" + d + "/" + k4 + "/d116")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1164').innerHTML = k4 + "当日过车情况"
        document.getElementById('d1164').innerHTML = ""
        const rosePlot = new Rose('d1164', {
          data,
          xField: '车辆类型',
          yField: '过车数量',
          seriesField: '车辆类型',
          radius: 0.9,
          label: {
            offset: -15,
          },
          color,
          legend: {
            position: 'bottom',
          },
        });

        rosePlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function fl1() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType + "/l1")
      .then((res) => res.json())
      .then((data) => {
        l1.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function fl2() {
  fetch(localhost + y + '/' + m + "/" + d + '/' + h + "/" + airType + '/l2')
      .then(res => res.json())
      .then(data => {
        l2.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function fl3() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType + "/l3")
      .then(res => res.json())
      .then(data => {
        l3.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function fl4() {
  fetch(localhost + y + "/" + m + "/" + d + "/" + hLength1 + "/" + hLength2 + "/l4")
      .then(res => res.json())
      .then(data => {
        l4.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function initM() {
  d103()
  d106()
  d107()
  d108()
  d109()
  fl1()
  fl2()
  fl3()
  fl4()

  d113()
  d114()
  d115()
  d116()
}

// eslint-disable-next-line no-unused-vars
function initD() {
  d103()
  d106()
  d107()
  d108()
  fl1()
  fl2()
  fl3()
  fl4()


  d113()
  d114()
  d115()
  d116()
}

// eslint-disable-next-line no-unused-vars
function initH() {
  fl2()
  d103()
  d111()
  d112()
}

// eslint-disable-next-line no-unused-vars
function initS() {
  fl1()
  fl3()
  d107()
}

// eslint-disable-next-line no-unused-vars
function initKakou() {
  d107()
  d110()
  d116()
}

// eslint-disable-next-line no-unused-vars
function initAirType() {
  fl2()
  d105()

  d113()
  d114()
  d115()
}

// eslint-disable-next-line no-unused-vars
function initCarType() {
  fl1()
  fl3()
  d106()
  d110()
}

// eslint-disable-next-line no-unused-vars
function init() {
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

  d116()


}

export default {
  name: "csqxpwgkpt",
  components: {},
  mounted() {

    addListOption('d104Type', ['气温', 'AQI', '风速', '降水量', 'SO2', 'NO2', 'CO', 'PM10', 'PM2.5', 'O3'])
    addListOption('year', ['2021', '2020', '2022'])


    scene = new Scene({
      id: 'd101',
      map: new GaodeMap({
        pitch: 45,
        style: 'amap://styles/66156ec93d7481b949829a24124aefc4?isPublic=true',
        center: [115.983208, 36.469046],
        zoom: 8
      })
    });

    fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType + "/l1")
        .then((res) => res.json())
        .then((data) => {
          l1 = new PointLayer({})
              .source(data, {
                parser: {
                  x: 'jd',
                  y: 'wd',
                  type: 'json'
                }
              })
              .shape('circle')
              .size('value', [4, 16])
              .color('value', color)
              .active(true)
              .style({
                opacity: 0.7,
                strokeWidth: 0
              });
          scene.addLayer(l1)
          l1.hide()
          l1.on('click', ev => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">${ev.feature['卡口名称']}</span>`
                );
            scene.addPopup(popup);
            scene.setCenter([
              ev.lngLat.lng,
              ev.lngLat.lat
            ])
            kakou = ev.feature['卡口名称']
            k4 = k3
            k3 = k2
            k2 = k1
            k1 = ev.feature['卡口名称']
            this.p1101 = 0
            initKakou()
          })
          l1.on('contextmenu', ev => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">${ev.feature['卡口名称']}</span>`
                );
            scene.addPopup(popup);
            scene.setCenter([
              ev.lngLat.lng,
              ev.lngLat.lat
            ])
            kakou = ev.feature['卡口名称']
            k4 = k3
            k3 = k2
            k2 = k1
            k1 = ev.feature['卡口名称']
            fetch(localhost + y + "/" + m + "/" + d + "/" + kakou + "/d1101")
                .then((res) => res.json())
                .then((data) => {
                  this.p1101 = 1
                  document.getElementById('t1101').innerHTML = kakou + "车流量影响评价"
                  document.getElementById('d1101').innerHTML = data['s1'] + '<br>' + data['s2']
                })
            initKakou()
          })
        })

    fetch(localhost + y + '/' + m + "/" + d + '/' + h + "/" + airType + '/l2')
        .then(res => res.json())
        .then(data => {
          l2 = new PointLayer({})
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('cylinder')
              .active(true)
              .size('value', h => {
                return [6, 6, h];
              })
              .color('value', color)
              .style({
                opacity: 1.0
              });
          scene.addLayer(l2);
          l2.hide()
          l2.on('click', ev => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">${ev.feature['站点']}</span>`
                );
            scene.addPopup(popup);
            scene.setCenter([
              ev.lngLat.lng,
              ev.lngLat.lat
            ])
            p1 = ev.feature['站点']
            this.p11_15 = 1
            d103()
            d111()
            d113()
            d115()
          })
          l2.on('contextmenu', ev => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">${ev.feature['站点']}</span>`
                );
            scene.addPopup(popup);
            scene.setCenter([
              ev.lngLat.lng,
              ev.lngLat.lat
            ])
            p2 = ev.feature['站点']
            this.p11_15 = 1
            d103()
            d112()
            d114()
            d115()
          })
        });

    fetch(localhost + y + "/" + m + "/" + d + "/" + s + "/" + carType + "/l3")
        .then(res => res.json())
        .then(data => {
          l3 = new LineLayer({
            blend: 'normal'
          })
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd1',
                  y: 'wd1',
                  x1: 'jd2',
                  y1: 'wd2'
                }
              })
              .size('value', [1, 10])
              .shape('arc3d')
              .color('value', color)
              .animate({
                interval: 0.5,
                trailLength: 0.5,
                duration: 5
              })
              .style({
                opacity: 1
              });
          scene.addLayer(l3)
          l3.hide()
        });

    fetch(localhost + y + "/" + m + "/" + d + "/" + hLength1 + "/" + hLength2 + "/l4")
        .then(res => res.json())
        .then(data => {
          l4 = new LineLayer({blend: 'normal'})
              .source(data,
                  {
                    parser: {
                      type: 'json',
                      x: 'jd1',
                      y: 'wd1',
                      x1: 'jd2',
                      y1: 'wd2'
                    }
                  })
              .size(5)
              .shape('arc')
              .color(color[4])
              .animate({
                duration: 5,
                interval: 0.6,
                trailLength: 1
              });
          scene.addLayer(l4)
          l4.hide()
        });


    init()


  },
  data() {
    return {
      p1101: 0,

      p1: 1,
      p2: 0,
      p3: 0,

      l1: 0,
      l2: 0,
      l3: 0,
      l4: 0,

      p11_15: 0,
      p16: 0,


      startHour: '',
      endHour: '',

      value: '',
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '昨天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: '一周前',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          }
        }]
      },
    }
  },
  methods: {
    f1101() {
      if (this.p1101) {
        this.p1101 = 0
      } else {
        this.p1101 = 1
      }
    },

    fD104Type() {
      d104()
    },
    fYear() {
      y = selectTxt('year')
      init()
    },


    getDate: function (val) {
      y = val.getFullYear()
      m = val.getMonth() + 1
      d = val.getDate()
      init()
      fl1()
      fl2()
      fl3()
      fl4()
    },

    getStartHour: function (val) {
      h = Number(val.replace(":00", ""))
      hLength1 = Number(val.replace(":00", ""))
      if (h >= 2 && h <= 4) {
        s = "2:00-4:00"
      } else if (h >= 7 && h <= 9) {
        s = '7:00-9:00'
      } else if (h >= 10 && h <= 12) {
        s = '10:00-12:00'
      } else if (h >= 17 && h <= 19) {
        s = '17:00-19:00'
      }
      initH()
      initS()
    },

    getEndHour: function (val) {
      hLength2 = Number(val.replace(":00", ""))
      fl4()
    },

    fl1() {
      if (this.l1) {
        this.l1 = 0
        this.p16 = 0
        l1.hide()
      } else {
        this.l1 = 1
        this.p16 = 1
        l1.show()
      }
    },
    fl2() {
      if (this.l2) {
        this.l2 = 0
        this.p11_15 = 0
        l2.hide()
      } else {
        this.l2 = 1
        this.p11_15 = 1
        l2.show()
      }
    },
    fl3() {
      if (this.l3) {
        this.l3 = 0
        l3.hide()
      } else {
        this.l3 = 1
        l3.show()
      }
    },
    fl4() {
      if (this.l4) {
        this.l4 = 0
        l4.hide()
      } else {
        this.l4 = 1
        l4.show()
      }
    },
  }
}
</script>

<style scoped>
.divs {
  position: absolute;
  background-color: #f9f9f9;
  border-width: 1px;
  border-style: outset;
  border-color: #ddd;
}

.contents {
  position: absolute;
  height: 80%;
  width: 99%;
  left: 0.5%;
  top: 28px;
}

.titles {
  position: absolute;
  background-color: #ccc;
  color: #333;
  text-align: center;
  font-size: 15px;
  font-weight: bold;
  height: 25px;
  width: 100%;
  left: 0;
  top: 0;
}

.selects {
  position: absolute;
  width: 70px;
  height: 20px;
  border-radius: 5px;
  border-color: #aaa;
  border-style: dot-dash;
  color: #000;
  background-color: #fff;
  text-align: center;
  font-size: 10px;
  font-weight: bold;
}
</style>
