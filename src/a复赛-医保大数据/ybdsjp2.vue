<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div style="position: absolute;width: 98%;height: 85%;left: 1%;top: 12%;">
      <div id="map2" style="position: absolute; width: 49%; height: 98%;left: 0;top: 0"></div>
      <div class="divs" style="width: 24%; height: 59%; left: 50%; top: 0">
        <div id="d201" class="content"></div>
        <div id="t201" class="title"></div>
      </div>
      <div class="divs" style="width: 49%; height: 39%; left: 50%; top: 60%">
        <div id="d202" class="content"></div>
        <div id="t202" class="title"></div>
      </div>
      <div class="divs" style="width: 11.5%; height: 29%; left: 75%; top: 0">
        <div id="d204" class="content"></div>
        <div id="t204" class="title"></div>
      </div>
      <div class="divs" style="width: 12%; height: 29%; left: 87%; top: 0">
        <div id="d203" class="content"></div>
        <div id="t203" class="title"></div>
      </div>
      <div class="divs" style="width: 24%; height: 29%; left: 75%; top: 30%">
        <div id="d205" class="content"></div>
        <div id="t205" class="title"></div>
      </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar, Column, DualAxes, Rose} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene, layer201, layer202

// eslint-disable-next-line no-unused-vars
let type = "住院部分", xzqh = "莒县"

// eslint-disable-next-line no-unused-vars
function fType() {
  c4()
  l201()
}

// eslint-disable-next-line no-unused-vars
function fXzqh() {
  c3()
}

// eslint-disable-next-line no-unused-vars
function c1() {
  fetch(localhost + '/d201')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }

        data = data.sort(cmp)
        document.getElementById('t201').innerHTML = "各县区人均报销排行"
        document.getElementById('d201').innerHTML = ""
        const bar = new Bar('d201', {
          data,
          xField: 'value',
          yField: 'name',
          legend: false,
          xAxis: false
        });
        bar.render()
        let hoverData = {}
        bar.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        bar.on('plot:click', ev => {
          ev = ""
          xzqh = ev + hoverData['name']
          fXzqh()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c2() {
  fetch(localhost + "d202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = "各县区医疗费用情况"
        document.getElementById('d202').innerHTML = ""
        const area = new Area('d202', {
          data,
          xField: '行政区划',
          yField: 'value',
          seriesField: 'type',
          smooth: true,
          xAxis: {
            grid: null
          },
          yAxis: false
        });
        area.render();
        let hoverData = {}
        area.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        area.on('plot:click', ev => {
          ev = ""
          xzqh = ev + hoverData['行政区划']
          fXzqh()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function c3() {
  fetch(localhost + xzqh + '/d203')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }

        data = data.sort(cmp)
        document.getElementById('t203').innerHTML =  xzqh + "费用支出情况"
        document.getElementById('d203').innerHTML = ""
        const bar = new Bar('d203', {
          data,
          xField: 'value',
          yField: 'name',
          // seriesField: '',
          legend: false,
          xAxis: false
        });
        bar.render()
        let hoverData = {}
        bar.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        bar.on('plot:click', ev => {
          ev = ""
          type = ev + hoverData['name']
          fType()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c4() {
  fetch(localhost + type + '/d204')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }

        data = data.sort(cmp)
        document.getElementById('t204').innerHTML =  type + "费用排行"
        document.getElementById('d204').innerHTML = ""
        const bar = new Bar('d204', {
          data,
          xField: 'value',
          yField: 'name',
          // seriesField: '',
          legend: false,
          xAxis: false
        });
        bar.render()
        let hoverData = {}
        bar.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        bar.on('plot:click', ev => {
          ev = ""
          xzqh = ev + hoverData['name']
          fXzqh()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c5() {
  fetch(localhost + "d205")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t205').innerHTML =  "治疗人次和总费用关系"
        document.getElementById('d205').innerHTML = ""
        const dualAxes = new DualAxes('d205', {
          data: [data, data],
          xField: 'name',
          yField: ['治疗人次', '总费用'],
          yAxis: {
            治疗人次: false,
            总费用: false
          },
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
          xzqh = ev + hoverData['name']
          fXzqh()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function l201() {
  fetch(localhost + type + "/l201")
      .then(res => res.json())
      .then(data => {
        layer201.setData(data)
        layer202.setData(data)
      });
}

export default {
  name: 'p2',
  data() {
    return {}
  },
  mounted() {

    // eslint-disable-next-line no-undef
    scene = new Scene({
      id: 'map2',
      map: new GaodeMap({
        pitch: 0,
        type: 'amap',
        style: 'amap://styles/83b73ccd633185b096afe1b7035f9a1c?isPublic=true',
        center: [119.295469, 35.357701],
        zoom: 8,
      })
    });

    scene.on('loaded', () => {
      fetch(localhost + type + "/l201")
          .then(res => res.json())
          .then(data => {
            layer201 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
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
            scene.addLayer(layer201);
            layer202 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('circle')
                .size('value', [4, 16])
                .color('value', [
                  '#34B6B7',
                  '#4AC5AF',
                  '#5FD3A6',
                  '#7BE39E',
                  '#A1EDB8',
                  '#CEF8D6'
                ])
                .active(true)
                .style({
                  opacity: 0.5,
                  strokeWidth: 0
                });
            layer202.on('click', e => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(e.lngLat)
                  .setHTML(`<span>${e.feature.name}</span>`);
              xzqh = e.feature.name
              fXzqh()
              scene.addPopup(popup);
            });
            scene.addLayer(layer202)
          });
    });


    c1()
    c2()
    c3()
    c4()
    c5()


  },
  methods: {}
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
  background-color: #fff;
  border-color: #eee;
  border-width: 1px;
  color: #000;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>