<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0">
    <dv-border-box4

        style="position: absolute; width: 30%; height: 50%; left: 0; top: 0"
        :color="['#aaa', '#eee']"
    >

    </dv-border-box4>

    <dv-border-box-12

        style="position: absolute; width: 20%; height: 20%; left: 2%; top: 50%"
        :color="['#aaa', '#eee']"
    >

    </dv-border-box-12>

    <dv-border-box-13

        style="position: absolute; width: 48%; height: 27%; left: 2%; top: 70%"
        :color="['#aaa', '#eee']"
    >
      <div id="column1" class="content"></div>
    </dv-border-box-13>


    <dv-border-box1
        style="position: absolute; width: 56%; height: 60%; left: 22%; top: 10%; color: #777"
        :color="['#eee', '#aaa']"
    >
      <div id="map" class="content"></div>
    </dv-border-box1>


    <dv-border-box-12

        style="position: absolute; width: 20%; height: 45%; right: 2%; top: 5%"
        :color="['#aaa', '#eee']"
    >
      <div class="title" id="tbar1"></div>
      <div class="content" id="bar1"></div>
    </dv-border-box-12>


    <dv-border-box12

        style="position: absolute; width: 25%; height: 27%; right: 25%; bottom: 3%"
        :color="['#aaa', '#eee']"
    >
      <div class="content" id="pie1"></div>
    </dv-border-box12>

    <dv-border-box4

        style="position: absolute; width: 30%; height: 50%; right: 0; bottom: 0"
        :color="['#aaa', '#eee']"
        :reverse="true"
    >

    </dv-border-box4>

    <!--    图表内容-->
    <div id="div1_1">
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
    </div>
    <div id="div1_2"
         style="position: absolute; width: 18%; height: 8%;left: 2%;top: 40%">
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
    <div id="div2_1">
      <img
          src="./logo/机构名称.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 3%;top: 50%"
      >
      <div
          id="jigoumingcheng2"
          style="position: absolute;width: 6%;height: 9%;left: 7%;top: 52.5%"
          class="title"
      />
      <img
          src="./logo/建筑面积.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 3%;top: 59%"
      >
      <div
          id="jianzhumianji2"
          style="position: absolute;width: 6%;height: 9%;left: 7%;top: 61.5%"
          class="title"
      />
      <img
          src="./logo/入住人数.jpg"
          style="position: absolute;width: 4%;height: 9%;left: 14%;top: 50%"
      >
      <div
          id="ruzhurenshu2"
          style="position: absolute;width: 6%;height: 9%;left: 16%;top: 52.5%"
          class="title"
      />
    </div>
    <div
        style="position: absolute; width: 9%; height: 9%;left: 12%;top: 59%">
      <div id="div2_2" class="content"></div>
    </div>
    <div id="div3_1">
      <img
          src="./logo/机构名称.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 17%;bottom: 40%"
      >
      <div
          id="jigoumingcheng3"
          style="position: absolute;width: 6%;height: 9%;left: 83%;top: 51%"
          class="title"
      />
      <img
          src="./logo/运营方式.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 17%;bottom: 31%"
      >
      <div
          id="yunyingfangshi3"
          style="position: absolute;width: 8%;height: 9%;left: 82%;top: 63%"
          class="title"
      />
      <img
          src="./logo/建筑面积.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 17%;bottom: 22%"
      >
      <div
          id="jianzhumianji3"
          style="position: absolute;width: 8%;height: 9%;left: 82%;top: 72%"
          class="title"
      />
      <img
          src="./logo/床位总数.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 7%;bottom: 40%"
      >
      <div
          id="chuangweizongshu3"
          style="position: absolute;width: 8%;height: 9%;left: 91%;top: 55%"
          class="title"
      />
    </div>
    <div
        style="position: absolute; width: 8%; height: 18%; right: 3%; bottom: 21%">
      <div id="div3_2" class="content"></div>
    </div>
    <div id="div4_1">
      <img
          src="./logo/机构名称.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 17%;bottom: 12%"
      >
      <div
          id="jigoumingcheng4"
          style="position: absolute;width: 6%;height: 9%;left: 83%;top: 82%"
          class="title"
      />
      <img
          src="./logo/建筑面积.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 17%;bottom: 3%"
      >
      <div
          id="jianzhumianji4"
          style="position: absolute;width: 6%;height: 9%;left: 83%;top: 92%"
          class="title"
      />
      <img
          src="./logo/运营方式.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 7%;bottom: 12%"
      >
      <div
          id="yunyingfangshi4"
          style="position: absolute;width: 6%;height: 9%;left: 93%;top: 82%"
          class="title"
      />
      <img
          src="./logo/床位总数.jpg"
          style="position: absolute;width: 4%;height: 9%;right: 7%;bottom: 3%"
      >
      <div
          id="chuangweizongshu4"
          style="position: absolute;width: 6%;height: 9%;left: 93%;top: 92%"
          class="title"
      />
    </div>


    <select
        class="selects"
        id="csvName"
        style="left: 40%;top: 10.5%"
        @change=fcsvName
    ></select>
    <select
        class="selects"
        id="value1"
        style="left: 45%;top: 10.5%"
        @change="fvalue1"
    ></select>
    <select
        class="selects"
        id="value2"
        style="left: 50%;top: 10.5%"
        @change="fvalue2"
    ></select>
    <select
        class="selects"
        id="value3"
        style="left: 55%;top: 10.5%"
        @change="fvalue3"
    ></select>

  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, PointLayer, Popup, Scene} from "@antv/l7";
import {Bar, Column, Gauge, Pie} from "@antv/g2plot";
import {DrawControl} from "@antv/l7-draw";


// eslint-disable-next-line no-unused-vars
let scene, lng1 = 0, lat1 = 0, lng2 = 180, lat2 = 90

// eslint-disable-next-line no-unused-vars
let layer1_1, layer1_2, layer1_3

// eslint-disable-next-line no-unused-vars
let color1 = [
  '#009933',
  '#ff66aa',
  '#33bb77',
  '#ee77dd',
  '#77dd99',
  '#ff99ff',
  '#008800',
  '#880088'
]

// eslint-disable-next-line no-unused-vars
let colors1 = ['#009933', '#55aa99', '#99ddaa']


// eslint-disable-next-line no-unused-vars
let layer2_1, layer2_2

// eslint-disable-next-line no-unused-vars
let colors2 = ['#997766', '#bb7788', '#dd99aa']

// eslint-disable-next-line no-unused-vars
let layer3_1, layer3_2

// eslint-disable-next-line no-unused-vars
let colors3 = ['#334488', '#6677aa', '#99aadd']


// eslint-disable-next-line no-unused-vars
let layer4_1, layer4_2

// eslint-disable-next-line no-unused-vars
let colors4 = ['#999900', '#ddbb00', '#ffff33']

// eslint-disable-next-line no-unused-vars
let layer5

// eslint-disable-next-line no-unused-vars
let colors5 = ['#aa0000', '#dd4400', '#ff7700']

// eslint-disable-next-line no-unused-vars
let layer6, layer7

// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:5000/'

// eslint-disable-next-line no-unused-vars
let csvName = "养老机构", value1 = "床位总数", value2 = "兴办主体", value3 = "护理型床位数"

// eslint-disable-next-line no-unused-vars
let values1 = {
  "养老机构": ['床位总数', '护理型床位数', '入住老年人数', '从业人员数'],
  "助餐点": ['建筑面积'],
  "小区养老设施": ['住户人数', '建筑面积'],
  "幸福院": ['建筑面积', '床位数量'],
  "日间照料中心": ['建筑面积', '床位数量']
}

// eslint-disable-next-line no-unused-vars
let values2 = {
  "养老机构": ['机构类别', '所属区划', '运营方式', '兴办主体'],
  "助餐点": ['县市区'],
  "小区养老设施": ['街道名称'],
  "幸福院": ['县市区', '运营性质'],
  "日间照料中心": ['县市区', '运营性质']
}

// eslint-disable-next-line no-unused-vars
let values3 = {
  "养老机构": ['护理型床位数', '床位总数', '入住老年人数', '从业人员数'],
  "助餐点": ['建筑面积'],
  "小区养老设施": ['建筑面积', '住户人数'],
  "幸福院": ['床位数量', '建筑面积'],
  "日间照料中心": ['床位数量', '建筑面积']
}

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
function div2(name) {
  fetch(localhost + name + "/div2")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div2_2').innerHTML = ""
        document.getElementById('jigoumingcheng2').innerHTML = data[0]['机构名称']
        document.getElementById('jianzhumianji2').innerHTML = data[0]['建筑面积'] + "m2"
        document.getElementById('ruzhurenshu2').innerHTML = data[0]['住户人数'] + "人"
        let gauge1 = new Gauge('div2_2', {
          percent: data[0]['建筑面积'] / data[0]['住户人数'],
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
              formatter: () => String((data[0]['建筑面积'] / data[0]['住户人数']).toFixed(2)).slice(0, 4) + "m2",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => '人均面积',
            },
          },
        });
        gauge1.render();
      })
}

// eslint-disable-next-line no-unused-vars
function div3(name) {
  fetch(localhost + name + "/div3")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div3_2').innerHTML = ""
        document.getElementById('jigoumingcheng3').innerHTML = data[0]['机构名称']
        document.getElementById('jianzhumianji3').innerHTML = data[0]['建筑面积'] + "m2"
        document.getElementById('yunyingfangshi3').innerHTML = data[0]['运营性质']
        document.getElementById('chuangweizongshu3').innerHTML = data[0]['床位数量'] + "张"
        let gauge1 = new Gauge('div3_2', {
          percent: data[0]['建筑面积'] / data[0]['床位数量'],
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
              formatter: () => String((data[0]['建筑面积'] / data[0]['床位数量']).toFixed(2)).slice(0, 4) + "m2",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => '人均面积',
            },
          },
        });
        gauge1.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div4(name) {
  fetch(localhost + name + "/div4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('jigoumingcheng4').innerHTML = data[0]['机构名称']
        document.getElementById('jianzhumianji4').innerHTML = data[0]['建筑面积'] + "m2"
        document.getElementById('yunyingfangshi4').innerHTML = data[0]['运营性质']
        document.getElementById('chuangweizongshu4').innerHTML = data[0]['床位数量'] + "张"
      });
}

let color = colors1.reverse()

// eslint-disable-next-line no-unused-vars
function bar1() {
  fetch(localhost + csvName + "/" + lng1 + "/" + lng2 + "/" + lat1 + "/" + lat2 + "/bar1")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('tbar1').innerHTML = csvName + '机构topsis评分'
        document.getElementById('bar1').innerHTML = ""
        const column = new Bar('bar1', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          yAxis: {
            grid: null
          },
          xAxis: {
            grid: null
          },
          color,
          scrollbar: {
            type: 'vertical',
          },
          barStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
        });

        column.render();
        let hoverData = {}
        column.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        column.on('plot:click', ev => {
          ev = ""
          if (csvName === '养老机构') div1(hoverData['name'] + ev)
          if (csvName === '小区养老设施') div2(hoverData['name'] + ev)
          if (csvName === '日间照料中心') div3(hoverData['name'] + ev)
          if (csvName === '幸福院') div4(hoverData['name'] + ev)
          scene.setCenter([hoverData['jd'], hoverData['wd']])
          const popup = new Popup({
            offsets: [0, 0],
            closeButton: false
          })
              .setLnglat({'lng': hoverData['jd'], 'lat': hoverData['wd']})
              .setHTML(
                  `<span style="color: #777">${hoverData['name']}</span>`
              );
          scene.addPopup(popup);
        });
      });
}

// eslint-disable-next-line no-unused-vars
function pie1() {
  fetch(localhost + csvName + "/" + value2 + "/" + lng1 + "/" + lng2 + "/" + lat1 + "/" + lat2 + "/pie1")
      .then((res) => res.json())
      .then((data) => {

        document.getElementById('pie1').innerHTML = ""
        const piePlot = new Pie('pie1', {
          appendPadding: 10,
          data,
          angleField: 'value',
          colorField: 'name',
          radius: 0.8,
          color: color1,
          label: {
            type: 'outer',
            content: '{name} {percentage}',
          },
          pirStyle: {
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          interactions: [{type: 'pie-legend-active'}, {type: 'element-active'}],
        });

        piePlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function column1() {
  fetch(localhost + csvName + "/" + value1 + "/" + value3 + "/" + lng1 + "/" + lng2 + "/" + lat1 + "/" + lat2 + "/column1")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('column1').innerHTML = ""
        const stackedColumnPlot = new Column('column1', {
          data,
          isStack: true,
          xField: "name",
          yField: 'value',
          seriesField: 'type',
          color: color1,
          legend: false,
          label: false,
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          slider: {
            start: 0,
            end: 0.2
          }
        });
        stackedColumnPlot.render();
        let hoverData = {}
        stackedColumnPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        stackedColumnPlot.on('plot:click', ev => {
          ev = ""
          if (csvName === '养老机构') div1(hoverData['name'] + ev)
          if (csvName === '小区养老设施') div2(hoverData['name'] + ev)
          if (csvName === '日间照料中心') div3(hoverData['name'] + ev)
          if (csvName === '幸福院') div4(hoverData['name'] + ev)
          scene.setCenter([hoverData['jd'], hoverData['wd']])
          const popup = new Popup({
            offsets: [0, 0],
            closeButton: false
          })
              .setLnglat({'lng': hoverData['jd'], 'lat': hoverData['wd']})
              .setHTML(
                  `<span style="color: #777">${hoverData['name']}</span>`
              );
          scene.addPopup(popup);
        });
      });
}

export default {
  name: "yantaiyanglaofusaip1",
  mounted() {


    addListOption('csvName', ['养老机构', '助餐点', '小区养老设施', '幸福院', '日间照料中心'])
    addListOption('value1', values1[csvName])
    addListOption('value2', values2[csvName])
    addListOption('value3', values3[csvName])


    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        center: [121.495243, 37.213508],
        pitch: 45,
        zoom: 7.5,
        // style: 'amap://styles/30e7c78b2547888bba6ce4c27edf7431?isPublic=true',
        style: 'light'
      })
    });
    const drawControl = new DrawControl(scene, {
      position: 'topright',
      layout: 'horizontal', // horizontal vertical
      controls: {
        point: false,
        polygon: false,
        line: false,
        circle: true,
        rect: true,
        delete: true
      }
    });
    scene.addControl(drawControl);
    drawControl.on('draw.create', (e) => {
      lng1 = e.feature.properties.startPoint.lng
      lat1 = e.feature.properties.startPoint.lat
      lng2 = e.feature.properties.endPoint.lng
      lat2 = e.feature.properties.endPoint.lat
      bar1()
      pie1()
      column1()
    });
    drawControl.on('draw.update', (e) => {
      lng1 = e.feature.properties.startPoint.lng
      lat1 = e.feature.properties.startPoint.lat
      lng2 = e.feature.properties.endPoint.lng
      lat2 = e.feature.properties.endPoint.lat
      bar1()
      pie1()
      column1()
    });


    scene.on('loaded', () => {
      fetch(localhost + "layer1")
          .then(res => res.json())
          .then(data => {
            layer1_1 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('床位总数', function (level) {
                  return [3, 3, level / 20];
                })
                .active(true)
                .color(colors1[0])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer1_1);
            layer1_1.on('click', ev => {
              div1(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + "layer1")
          .then(res => res.json())
          .then(data => {
            layer1_2 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('入住老年人数', function (level) {
                  return [6, 6, level / 20];
                })
                .active(true)
                .color(colors1[1])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer1_2);
            layer1_2.on('click', ev => {
              div1(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + "layer1")
          .then(res => res.json())
          .then(data => {
            layer1_3 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('从业人员数', function (level) {
                  return [9, 9, level / 20];
                })
                .active(true)
                .color(colors1[2])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer1_3);
            layer1_3.on('click', ev => {
              div1(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });


    scene.on('loaded', () => {
      fetch(localhost + "layer2")
          .then(res => res.json())
          .then(data => {
            layer2_1 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('建筑面积', function (level) {
                  return [level / 200, level / 200, 5];
                })
                .active(true)
                .color(colors2[2])
                .style({
                  opacity: 0.7
                });
            scene.addLayer(layer2_1);
            layer2_1.hide()
            layer2_1.on('click', ev => {
              div2(ev.feature['小区名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['小区名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + "layer2")
          .then(res => res.json())
          .then(data => {
            layer2_2 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('住户人数', function (level) {
                  return [3, 3, level / 100];
                })
                .active(true)
                .color(colors2[1])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer2_2);
            layer2_2.hide()
            layer2_2.on('click', ev => {
              div2(ev.feature['小区名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['小区名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });


    scene.on('loaded', () => {
      fetch(localhost + "layer3")
          .then(res => res.json())
          .then(data => {
            layer3_1 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('建筑面积', function (level) {
                  return [level / 200, level / 200, 5];
                })
                .active(true)
                .color(colors3[2])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer3_1);
            layer3_1.hide()
            layer3_1.on('click', ev => {
              div3(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + "layer3")
          .then(res => res.json())
          .then(data => {
            layer3_2 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('床位数量', function (level) {
                  return [3, 3, level / 5];
                })
                .active(true)
                .color(colors3[1])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer3_2);
            layer3_2.hide()
            layer3_2.on('click', ev => {
              div3(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });


    scene.on('loaded', () => {
      fetch(localhost + "layer4")
          .then(res => res.json())
          .then(data => {
            layer4_1 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('建筑面积', function (level) {
                  return [level / 500, level / 500, 5];
                })
                .active(true)
                .color(colors4[2])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer4_1);
            layer4_1.hide()
            layer4_1.on('click', ev => {
              div4(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + "layer4")
          .then(res => res.json())
          .then(data => {
            layer4_2 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('床位数量', function (level) {
                  return [3, 3, level / 5];
                })
                .active(true)
                .color(colors4[1])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer4_2);
            layer4_2.hide()
            layer4_2.on('click', ev => {
              div4(ev.feature['机构名称'])
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });


    scene.on('loaded', () => {
      fetch(localhost + "layer5")
          .then(res => res.json())
          .then(data => {
            layer5 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd',
                  }
                })
                .shape('cylinder')
                .size('建筑面积', function (level) {
                  return [level / 200, level / 200, 5];
                })
                .active(true)
                .color(colors5[2])
                .style({
                  opacity: 1
                });
            scene.addLayer(layer5);
            layer5.hide()
            layer5.on('click', ev => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['机构名称']}</span>`
                  );
              scene.addPopup(popup);
            });
          });
    });


    div1('烟台市老年福利服务中心')
    div2('楚泰')
    div3('烟台市芝罘区黄务街道蓁山社区老年人日间照料中心')
    div4('高疃幸福院')
    bar1()
    column1()
    pie1()
  },
  methods: {
    fcsvName: function () {
      csvName = selectTxt('csvName')
      addListOption('value1', values1[csvName])
      addListOption('value2', values2[csvName])
      addListOption('value3', values3[csvName])
      value1 = selectTxt('value1')
      value2 = selectTxt('value2')
      value3 = selectTxt('value3')
      bar1()
      pie1()
      column1()
      if (csvName === "养老机构") {
        layer1_1.hide()
        layer1_2.hide()
        layer1_3.hide()
        layer2_1.hide()
        layer2_2.hide()
        layer3_1.hide()
        layer3_2.hide()
        layer4_1.hide()
        layer4_2.hide()
        layer5.hide()
        layer1_1.show()
        layer1_2.show()
        layer1_3.show()
      }
      if (csvName === "小区养老设施") {
        layer1_1.hide()
        layer1_2.hide()
        layer1_3.hide()
        layer2_1.hide()
        layer2_2.hide()
        layer3_1.hide()
        layer3_2.hide()
        layer4_1.hide()
        layer4_2.hide()
        layer5.hide()
        layer2_1.show()
        layer2_2.show()
      }
      if (csvName === "日间照料中心") {
        layer1_1.hide()
        layer1_2.hide()
        layer1_3.hide()
        layer2_1.hide()
        layer2_2.hide()
        layer3_1.hide()
        layer3_2.hide()
        layer4_1.hide()
        layer4_2.hide()
        layer5.hide()
        layer3_1.show()
        layer3_2.show()
      }
      if (csvName === "幸福院") {
        layer1_1.hide()
        layer1_2.hide()
        layer1_3.hide()
        layer2_1.hide()
        layer2_2.hide()
        layer3_1.hide()
        layer3_2.hide()
        layer4_1.hide()
        layer4_2.hide()
        layer5.hide()
        layer4_1.show()
        layer4_2.show()
      }
      if (csvName === "助餐点") {
        layer1_1.hide()
        layer1_2.hide()
        layer1_3.hide()
        layer2_1.hide()
        layer2_2.hide()
        layer3_1.hide()
        layer3_2.hide()
        layer4_1.hide()
        layer4_2.hide()
        layer5.hide()
        layer5.show()
      }
    },
    fvalue1: function () {
      value1 = selectTxt('value1')
      column1()
    },
    fvalue2: function () {
      value2 = selectTxt('value2')
      pie1()
    },
    fvalue3: function () {
      value3 = selectTxt('value3')
      column1()
    },
  },
  data() {
    return {}
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
  color: #333
}

.content {
  position: absolute;
  width: 96%;
  height: 85%;
  left: 2%;
  top: 12%;
  text-align: center;
  font-size: 20%;
  color: #fff;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 50%;
  height: 10%;
  left: 25%;
  top: 2%;
  text-align: center;
  font-size: 20%;
  color: #777;
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
  border-color: #eee;
  border-width: 1px;
  color: #777;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>