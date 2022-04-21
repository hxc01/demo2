<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div style="position: absolute;width: 98%;height: 85%;left: 1%;top: 12%;">
      <div id="map4" style="position: absolute; width: 39%; height: 98%;left: 0;top: 0"></div>
      <div class="divs" style="width: 29%; height: 69%; left: 70%; top: 30%">
        <div id="d401" class="content"></div>
        <div id="t401" class="title"></div>
      </div>
      <div class="divs" style="width: 14%; height: 29%; left: 70%; top: 0">
        <div id="d402" class="content"></div>
        <div id="t402" class="title"></div>
      </div>
      <div class="divs" style="width: 14%; height: 29%; left: 85%; top: 0">
        <div id="d403" class="content"></div>
        <div id="t403" class="title"></div>
      </div>
      <div class="divs" style="width: 29%; height: 99%; left: 40%; top: 0">
        <div id="d404" class="content"></div>
        <div id="t404" class="title"></div>
      </div>
      <select @change="fS401" id="s401" class="selects" style="left: 71%; top: 31%"></select>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar, Column, DualAxes, Gauge, Radar, Rose, Sunburst, WordCloud} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene, layer401, layer402

// eslint-disable-next-line no-unused-vars
let year = '2021', month = '8', day = '31', zdmc = '糖尿病胰岛素治疗'

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
function fZdmc() {
  d403()
  l401_2()
}

// eslint-disable-next-line no-unused-vars
function d401() {
  fetch(localhost + selectTxt('s401') + "/d401")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('d401').innerHTML = ""
        const plot = new Sunburst('d401', {
          data,
          innerRadius: 0.4,
          interactions: [{type: 'element-active'}],
          label: {
            // label layout: limit label in shape, which means the labels out of shape will be hide
            layout: [{type: 'limit-in-shape'}],
          },
        });
        plot.render();
        let hoverData = {}
        plot.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        plot.on('plot:click', ev => {
          ev = ""
          month = ev + hoverData['ancestor-node']
          day = ev + hoverData['name']
          d402()
          d404()
          l401_2()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d402() {
  fetch(localhost + year + "/" + month + "/" + day + "/d402")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t402').innerHTML = year + "年" + month + "月" + day + "日病症词云"
        document.getElementById('d402').innerHTML = ""
        const wordCloud = new WordCloud('d402', {
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
        let hoverData = {}
        wordCloud.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        wordCloud.on('plot:click', ev => {
          ev = ""
          console.log(hoverData)
          zdmc = ev + hoverData['text']
          fZdmc()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d403() {
  fetch(localhost + zdmc + '/d403')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }

        data = data.sort(cmp)
        document.getElementById('t403').innerHTML = zdmc + "街道分布"
        document.getElementById('d403').innerHTML = ""
        const column = new Bar('d403', {
          data,
          yField: 'name',
          xField: 'value',
          yAxis: {
            label: {
              autoRotate: false,
            },
          },
          scrollbar: {
            type: 'vertical',
          },
          xAxis: false
        });
        column.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d404() {
  fetch(localhost + year + "/" + month + "/" + day + "/d404")
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.value - x.value
        }
        data = data.sort(cmp)
        document.getElementById('t404').innerHTML = year + "年" + month + "月" + day + "日病症住院时长"
        document.getElementById('d404').innerHTML = ""
        const column = new Bar('d404', {
          data,
          yField: 'name',
          xField: 'value',
          // yAxis: false,
          xAxis: {
            grid: null
          },
          scrollbar: {
            type: 'vertical',
          },
        });
        column.render();
        let hoverData = {}
        column.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        column.on('plot:click', ev => {
          ev = ""
          console.log(hoverData)
          zdmc = ev + hoverData['name']
          fZdmc()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function l401_2() {
  fetch(localhost + zdmc + "/" + year + "/" + month + "/" + day + "/l401_2")
      .then(res => res.json())
      .then(data => {
        layer401.setData(data)
        layer402.setData(data)
      });
}

export default {
  name: 'p4',
  data() {
    return {}
  },
  mounted() {


    addListOption('s401', ['门诊慢特病', '普通门诊', '住院'])


    // eslint-disable-next-line no-undef
    scene = new Scene({
      id: 'map4',
      map: new GaodeMap({
        pitch: 0,
        type: 'amap',
        style: 'amap://styles/83b73ccd633185b096afe1b7035f9a1c?isPublic=true',
        center: [119.295469, 35.357701],
        zoom: 8,
      })
    });

    scene.on('loaded', () => {
      fetch(localhost + zdmc + "/" + year + "/" + month + "/" + day + "/l401_2")
          .then(res => res.json())
          .then(data => {
            layer401 = new HeatmapLayer({})
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
            scene.addLayer(layer401);
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + zdmc + "/" + year + "/" + month + "/" + day + "/l401_2")
          .then(res => res.json())
          .then(data => {
            layer402 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('circle')
                .size('value', [0, 16])
                .color('#CEF8D6')
                .active(true)
                .style({
                  opacity: 0.5,
                  strokeWidth: 0
                });
            scene.addLayer(layer402);
          });
    });


    d401()
    d402()
    d403()
    d404()


  },
  methods: {
    fS401() {
      d401()
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
  height: 90%;
  left: 5%;
  top: 20px;
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