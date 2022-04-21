<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0">

    <dv-border-box5
        :reverse="true"
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 43.5%;left: 0;top: 6.5%"
    >
      <div class="title" id="t201"></div>
      <div class="content" id="div201"></div>
    </dv-border-box5>
    <dv-border-box2
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 20%;left: 0;top: 50%"
    >
      <div class="title" id="t203"></div>
      <div id="div203" class="content"></div>
    </dv-border-box2>
    <dv-border-box6
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 45%;height: 30%;left: 0;top: 70%"
    >
      <div class="title" id="t204"></div>
      <div id="div204" class="content"></div>
    </dv-border-box6>


    <dv-border-box1
        style="position: absolute; width: 56%; height: 60%; left: 22%; top: 10%; color: #007700"
        :color="['#aaaaaa', '#eeeeee']"
    >
      <div id="map2" class="content"></div>
    </dv-border-box1>


    <dv-border-box9
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 35%;right: 0;top: 6.5%"
    >
      <div class="title" id="t205"></div>
      <div id="div205" class="content"></div>
    </dv-border-box9>
    <dv-border-box2
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 33%;height: 30%;left: 45%;bottom: 0"
    >
      <div class="title" id="t202"></div>
      <div id="div202" class="content"></div>
    </dv-border-box2>
    <dv-border-box5
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 58.5%;right: 0;bottom: 0"
    >
      <div class="title" id="t206"></div>
      <div id="div206" class="content"></div>
    </dv-border-box5>

  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Scene} from "@antv/l7";
import {Bar, Column, WordCloud} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let scene, layer1


// eslint-disable-next-line no-unused-vars
let colors1 = [
  '#33aa33',
  '#449944',
  '#558855',
  '#667766',
  '#776677',
  '#885588',
  '#994499',
]


// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:5000/'

// eslint-disable-next-line no-unused-vars
let year = 2021, month = 7, day = 31

// eslint-disable-next-line no-unused-vars
let xsq = "莱州市", age = "72", zbmc = '糖尿病'

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
function div201() {
  fetch(localhost + age + "/div201")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t201').innerHTML = age + "岁疾病词云图"
        document.getElementById('div201').innerHTML = ""
        const wordCloud = new WordCloud('div201', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'value',
          color: colors1,
          wordStyle: {
            fontFamily: 'Verdana',
            fontSize: [8, 32],
            rotation: 0,
          },
          random: () => 0.5,
        });

        wordCloud.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div202y() {
  fetch(localhost + "/div202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = "就诊人数"
        document.getElementById('div202').innerHTML = ""
        const columnPlot = new Column('div202', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'value',
          color: colors1,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
        });

        columnPlot.render();
        let hoverData = {}
        columnPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        columnPlot.on('plot:click', ev => {
          ev = ""
          year = hoverData['name'] + ev
          div202m()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function div202m() {
  fetch(localhost + year + "/div202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = year+"年就诊人数"
        document.getElementById('div202').innerHTML = ""
        const columnPlot = new Column('div202', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'value',
          color: colors1,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
        });

        columnPlot.render();
        let hoverData = {}
        columnPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        columnPlot.on('plot:click', ev => {
          ev = ""
          month = hoverData['name'] + ev
          div202d()
        });
        columnPlot.on('contextmenu', ev => {
          ev = ""
          month = month + ev
          div202y()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function div202d() {
  fetch(localhost + year + "/" + month + "/div202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = year+"年"+month+"月就诊人数"
        document.getElementById('div202').innerHTML = ""
        const columnPlot = new Column('div202', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'value',
          color: colors1,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
        });

        columnPlot.render();
        let hoverData = {}
        columnPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        columnPlot.on('plot:click', ev => {
          ev = ""
          day = hoverData['name'] + ev
          div206()
        });
        columnPlot.on('contextmenu', ev => {
          ev = ""
          month = month + ev
          div202m()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function div203() {
  fetch(localhost + "div203")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t203').innerHTML = "年龄分布"
        document.getElementById('div203').innerHTML = ""
        const columnPlot = new Column('div203', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'value',
          color: colors1,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
        });
        columnPlot.render();
        let hoverData = {}
        columnPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        columnPlot.on('plot:click', ev => {
          ev = ""
          age = hoverData['name'] + ev
          div201()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function div204() {
  fetch(localhost + xsq + "/div204")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('t204').innerHTML = xsq+"疾病分布"
        document.getElementById('div204').innerHTML = ""
        const column = new Bar('div204', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          color: colors1,
          yAxis: {
            grid: null
          },
          xAxis: {
            grid: null
          },
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
          zbmc = hoverData['name'] + ev
          l1()
          div205()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function l1() {
  fetch(localhost + zbmc + "/l1")
      .then(res => res.json())
      .then(data => {
        layer1.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function div205() {
  fetch(localhost + xsq + "/" + zbmc + "/div205")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('t205').innerHTML = xsq+zbmc+"就诊次数"
        document.getElementById('div205').innerHTML = ""
        const column = new Bar('div205', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          color: colors1,
          yAxis: {
            grid: null
          },
          xAxis: {
            grid: null
          },
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
        column.render()
      });
}

// eslint-disable-next-line no-unused-vars
function div206() {
  fetch(localhost + year + "/" + month + "/" + day + "/div206")
      .then((res) => res.json())
      .then((data) => {
        // eslint-disable-next-line no-undef
        document.getElementById('t206').innerHTML = year+"年"+month+"月"+day+"日疾病词云"
        document.getElementById('div206').innerHTML = ""
        const wordCloud = new WordCloud('div206', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'value',
          color: colors1,
          columnStyle: {
            radius: [20, 20, 20, 20],
          },
          wordStyle: {
            fontFamily: 'Verdana',
            fontSize: [8, 32],
            rotation: 0,
          },
          random: () => 0.5,
        });

        wordCloud.render();
      });
}

export default {
  name: "yantaiyanglaofusaip2",
  mounted() {
    scene = new Scene({
      id: 'map2',
      map: new GaodeMap({
        center: [121.495243, 37.213508],
        pitch: 0,
        zoom: 7,
        // style: 'amap://styles/30e7c78b2547888bba6ce4c27edf7431?isPublic=true',
        style: 'light'
      })
    });

    scene.on('loaded', () => {
      fetch(localhost + zbmc + "/l1")
          .then(res => res.json())
          .then(data => {
            layer1 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('circle')
                .size('value', [4, 64])
                .color('value', [
                  '#B634B7',
                  '#C54AAF',
                  '#D35FA6',
                  '#E37B9E',
                  '#EDA1B8',
                  '#F8CED6'
                ].reverse())
                .active(true)
                .animate({
                  rings: 6,
                  speed: 3
                })
                .style({
                  opacity: 1,
                  strokeWidth: 0
                });
            scene.addLayer(layer1);
            layer1.on('click', ev => {
              xsq = ev.feature['name']
              div204()
              div205()
            })
          });
    });


    div201()
    div202y()
    div203()
    div204()
    div205()
    div206()


  },
  data() {
    return {}
  },
  methods: {}
}
</script>

<style scoped>
.content {
  position: absolute;
  width: 96%;
  height: 80%;
  left: 2%;
  top: 18%;
  text-align: center;
  font-size: 20%;
  color: #fff;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 50%;
  height: 6%;
  left: 25%;
  top: 8%;
  text-align: center;
  font-size: 20%;
  color: #000;
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
  color: #000;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>