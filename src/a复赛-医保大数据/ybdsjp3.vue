<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div style="position: absolute;width: 98%;height: 85%;left: 1%;top: 12%;">
      <div id="map3" style="position: absolute; width: 49%; height: 99%;left: 0;top: 0"></div>

      <div class="divs" style="left: 50%; top: 0; width: 49%; height: 49%">
        <div id="d301" class="content"></div>
        <div id="t301" class="title"></div>
      </div>
      <div class="divs" style="left: 50%; top: 50%; width: 29%; height: 49%">
        <div id="d302" class="content"></div>
        <div id="t302" class="title"></div>
      </div>
      <div class="divs" style="left: 80%; top: 50%; width: 9%; height: 24%">
        <div id="d303" class="content"></div>
        <div id="t303" class="title"></div>
      </div>
      <div class="divs" style="left: 90%; top: 50%; width: 9%; height: 24%">
        <div id="d304" class="content"></div>
        <div id="t304" class="title"></div>
      </div>
      <div class="divs" style="left: 80%; top: 75%; width: 19%; height: 24%">
        <div id="d305" class="content">
          <div id="d3051" class="content" style="left: 0; top: 0; width: 33%; height: 100%"></div>
          <div id="d3052" class="content" style="left: 33%; top: 0; width: 33%; height: 100%"></div>
          <div id="d3053" class="content" style="left: 66%; top: 0; width: 33%; height: 100%"></div>
        </div>
        <div id="t305" class="title"></div>
      </div>

      <select id="s301" class="selects" style="left: 51%; top: 50.5%" @change="fS301_302"></select>
      <select id="s302" class="selects" style="left: 73%; top: 50.5%" @change="fS301_302"></select>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar, Column, DualAxes, Gauge, Radar, Rose} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene, layer301, layer302, layer303, layer304

// eslint-disable-next-line no-unused-vars
let type = "GDP", xq1 = "五莲县", xq2 = '东港区'

// eslint-disable-next-line no-unused-vars
function fXq1() {
  c303_4()
  c305()
}

// eslint-disable-next-line no-unused-vars
function fXq2() {
  c303_4()
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
function c301() {
  fetch(localhost + 'd301')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }

        data = data.sort(cmp)
        document.getElementById('t301').innerHTML = "公立机构病种价格"
        document.getElementById('d301').innerHTML = ""
        const stackedBarPlot = new Bar('d301', {
          data,
          isGroup: true,
          xField: 'value',
          yField: '手术名称',
          seriesField: 'type',
          label: false,
          scrollbar: {
            type: 'vertical',
          },
          xAxis: false
        });

        stackedBarPlot.render();

      })
}

// eslint-disable-next-line no-unused-vars
function c302() {
  fetch(localhost + selectTxt('s301') + "/" + selectTxt('s302') + "/d302")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t302').innerHTML = selectTxt('s301') + selectTxt('s302') + "关系图"
        document.getElementById('d302').innerHTML = ""
        const dualAxes = new DualAxes('d302', {
          data: [data, data],
          xField: '县区',
          yField: [selectTxt('s301'), selectTxt('s302')],
          geometryOptions: [
            {
              geometry: 'column',
            },
            {
              geometry: 'line',
            },
          ],
        });
        dualAxes.render();
        let hoverData = {}
        dualAxes.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        dualAxes.on('plot:click', ev => {
          ev = ""
          xq1 = ev + hoverData['县区']
          fXq1()
        });
        dualAxes.on('plot:contextmenu', ev => {
          ev = ""
          xq2 = ev + hoverData['县区']
          fXq2()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c303_4() {
  fetch(localhost + xq1 + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t303').innerHTML = xq1 + "民生雷达模型"
        document.getElementById('d303').innerHTML = ""
        const radarPlot = new Radar('d303', {
          data,
          xField: 'name',
          yField: 'value',
          xAxis: {
            label: {
              offset: -10,
              style: {
                fontSize: 10
              }
            },
            grid: null,
          },
          yAxis: {
            label: false,
            grid: null,
          },
        });
        radarPlot.render();
      })
  fetch(localhost + xq2 + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t304').innerHTML = xq2 + "民生雷达模型"
        document.getElementById('d304').innerHTML = ""
        const radarPlot = new Radar('d304', {
          data,
          xField: 'name',
          yField: 'value',
          xAxis: {
            label: {
              offset: -10,
              style: {
                fontSize: 10
              }
            },
            grid: null,
          },
          yAxis: {
            label: false,
            grid: null,
          },
        });
        radarPlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function c305() {
  fetch(localhost + xq1 + "/d305")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t305').innerHTML = xq1 + "民生数据比例"
        document.getElementById('d3051').innerHTML = ""
        document.getElementById('d3052').innerHTML = ""
        document.getElementById('d3053').innerHTML = ""
        const gauge1 = new Gauge('d3051', {
          percent: data[0]['人均面积'],
          range: {
            color: 'l(0) 0:#B8E1FF 1:#3D76DD',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            content: {
              style: {
                fontSize: '4px',
                lineHeight: '44px',
                color: '#4B535E',
              },
              formatter: () => '人均面积',
            },
          },
        });
        const gauge2 = new Gauge('d3052', {
          percent: data[0]["人均GDP"],
          range: {
            color: 'l(0) 0:#B8E1FF 1:#3D76DD',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            content: {
              style: {
                fontSize: '4px',
                lineHeight: '44px',
                color: '#4B535E',
              },
              formatter: () => '人均GDP',
            },
          },
        });
        const gauge3 = new Gauge('d3053', {
          percent: data[0]['常住占比'],
          range: {
            color: 'l(0) 0:#B8E1FF 1:#3D76DD',
          },
          startAngle: Math.PI,
          endAngle: 2 * Math.PI,
          indicator: null,
          statistic: {
            content: {
              style: {
                fontSize: '4px',
                lineHeight: '44px',
                color: '#4B535E',
              },
              formatter: () => '常住占比',
            },
          },
        });
        gauge1.render();
        gauge2.render();
        gauge3.render();
      });
}

// eslint-disable-next-line no-unused-vars
function l304() {
  fetch(localhost + selectTxt('s301') + '/l304')
      .then(res => res.json())
      .then(data => {
        layer304.setData(data)
      });
}

export default {
  name: 'p3',
  data() {
    return {}
  },
  mounted() {


    addListOption('s301', ['GDP', '常住人口', '户籍人口', '面积'])
    addListOption('s302', ['常住人口', 'GDP', '户籍人口', '面积'])

    // eslint-disable-next-line no-undef
    scene = new Scene({
      id: 'map3',
      map: new GaodeMap({
        pitch: 0,
        type: 'amap',
        style: 'amap://styles/83b73ccd633185b096afe1b7035f9a1c?isPublic=true',
        center: [119.295469, 35.357701],
        zoom: 8,
      })
    });


    scene.on('loaded', () => {
      fetch(localhost + 'l301')
          .then(res => res.json())
          .then(data => {
            layer301 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: '经度',
                    y: '纬度'
                  }
                })
                .shape('circle')
                .size(20)
                .color('#34B6B7')
                .active(true)
                .animate({})
                .style({
                  opacity: 0.5,
                  strokeWidth: 0
                });
            scene.addLayer(layer301);
            layer301.on('click', e => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(e.lngLat)
                  .setHTML(
                      `<span>机构类型: 民营医疗机构</span>` + `<br>` +
                      `<span>机构名称: ${e.feature.机构名称}</span>` + `<br>` +
                      `<span>联系电话: ${e.feature.联系电话}</span>` + `<br>` +
                      `<span>机构级别: ${e.feature.机构级别}</span>` + `<br>` +
                      `<span>经营性质: ${e.feature.经营性质}</span>` + `<br>` +
                      `<span>机构等次: ${e.feature.机构等次}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + 'l302')
          .then(res => res.json())
          .then(data => {
            layer302 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: '经度',
                    y: '纬度'
                  }
                })
                .shape('circle')
                .size(20)
                .color('#B634B7')
                .active(true)
                .animate({})
                .style({
                  opacity: 0.5,
                  strokeWidth: 0
                });
            scene.addLayer(layer302);
            layer302.on('click', e => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(e.lngLat)
                  .setHTML(
                      `<span>机构类型: 乡镇卫生院</span>` + `<br>` +
                      `<span>机构名称: ${e.feature.机构名称}</span>` + `<br>` +
                      `<span>联系电话: ${e.feature.联系电话}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + 'l303')
          .then(res => res.json())
          .then(data => {
            layer303 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: '经度',
                    y: '纬度'
                  }
                })
                .shape('circle')
                .size(20)
                .color('#B6B734')
                .active(true)
                .animate({})
                .style({
                  opacity: 0.5,
                  strokeWidth: 0
                });
            scene.addLayer(layer303);
            layer303.on('click', e => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(e.lngLat)
                  .setHTML(
                      `<span>机构类型: 社区卫生服务中心</span>` + `<br>` +
                      `<span>机构名称: ${e.feature.机构名称}</span>` + `<br>` +
                      `<span>联系电话: ${e.feature.联系电话}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + selectTxt('s301') + '/l304')
          .then(res => res.json())
          .then(data => {
            layer304 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: '经度',
                    y: '纬度'
                  }
                })
                .shape('heatmap')
                .size('value', [0, 1.0]) // weight映射通道
                .style({
                  intensity: 2,
                  radius: 30,
                  opacity: 1.0,
                  rampColors: {
                    colors: [
                      '#FF4818',
                      '#F7B74A',
                      '#FFF598',
                      '#91EABC',
                      '#2EA9A1',
                      '#206C7C'
                    ].reverse(),
                    positions: [0, 0.2, 0.4, 0.6, 0.8, 1.0]
                  }
                });
            scene.addLayer(layer304);
          });
    });


    c301()
    c302()
    c303_4()
    c305()


  },
  methods: {
    fS301_302() {
      c302()
      l304()
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
  width: 80%;
  height: 80%;
  left: 5%;
  top: 20%;
  text-align: center;
  font-size: 20%;
  color: #fff;
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