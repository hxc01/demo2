<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #eee">
    <div class="title">基 于 B P 神 经 网 络 的 碳 排 放 分 析 预 测</div>
    <div style="position: absolute;width: 99%;height: 95%;left: 0.5%;top: 25px;">
      <div class="divs" style="width: 54.5%; height: 64%; left: 0; top: 0">
        <div class="title">G I S 功 能 面 板</div>
        <div class="content" id="map" style="height: 93%"></div>
      </div>
      <div class="divs" style="width: 54.5%; height: 34%; left: 0; top: 65%">
        <div class="title">电 力 能 源 消 耗 分 析</div>
        <div class="content">
          <div class="divs2" style="width: 39.5%; height: 100%; left: 0; top: 0">
            <div class="title" id="t101">电 力 分 析</div>
            <div class="content" id="d101"></div>
          </div>
          <div class="divs2" style="width: 34.5%; height: 100%; left: 40%; top: 0">
            <div class="title" id="t102">能 源 分 析</div>
            <div class="content" id="d102"></div>
          </div>
          <div class="divs2" style="width: 24.5%; height: 100%; left: 75%; top: 0">
            <div class="title" id="t103">产 业 占 比</div>
            <div class="content" id="d103"></div>
          </div>
        </div>
      </div>
      <div class="divs" style="width: 19.5%; height: 10%; left: 55%; top: 0">
        <div class="title">图 层 控 制</div>
        <div class="content">
          <button class="selects" style="background-color: #5b5; color: #fff; left: 0; top: 1%">污染分布</button>
          <button class="selects" style="background-color: #5bb; color: #fff; left: 25%; top: 1%">植被情况</button>
          <button class="selects" style="background-color: #b55; color: #fff; left: 50%; top: 1%">碳中评估</button>
          <button class="selects" style="background-color: #b5b; color: #fff; left: 75%; top: 1%">碳排评估</button>
          <button class="selects" style="background-color: #55b; color: #fff; left: 0; top: 35%">用电分布</button>
          <button class="selects" style="background-color: #b5b; color: #fff; left: 25%; top: 35%">能耗分布</button>
          <button class="selects" style="background-color: #bbb; color: #fff; left: 50%; top: 35%">人口分布</button>
          <button class="selects" style="background-color: #bb5; color: #fff; left: 75%; top: 35%">GDP分布</button>
        </div>
      </div>
      <div class="divs" style="width: 19.5%; height: 23%; left: 55%; top: 11%">
        <div class="title" id="t109">G D P 发 展 分 析</div>
        <div class="content" id="d109" style="position: absolute; height: 82%"></div>
      </div>
      <div class="divs" style="width: 24.5%; height: 34%; left: 75%; top: 0">
        <div class="title">人 口 经 济 趋 势 分 析</div>
        <div class="content">
          <div class="divs2" style="width: 49.5%; height: 100%; left: 0; top: 0">
            <div class="title" id="t104">人 口 变 化 预 测</div>
            <div class="content" id="d104"></div>
          </div>
          <div class="divs2" style="width: 49.5%; height: 100%; left: 50%; top: 0">
            <div class="title" id="t105">经 济 发 展 预 测</div>
            <div class="content" id="d105"></div>
          </div>
        </div>
      </div>
      <div class="divs" style="width: 24.5%; height: 64%; left: 55%; top: 35%">
        <div class="title">气 象 变 化 预 测 分 析</div>
        <div class="content">
          <div class="divs2" style="width: 59.5%; height: 49%; left: 0; top: 0">
            <div class="title" id="t106">A Q I 色 块 图</div>
            <div class="content" id="d106"></div>
          </div>
          <div class="divs2" style="width: 39.5%; height: 49%; left: 60%; top: 0">
            <div class="title" id="t107">污 染 因 子 排 行</div>
            <div class="content" id="d107"></div>
          </div>
          <div class="divs2" style="width: 99%; height: 56%; left: 1%; top: 50%">
            <div class="title" id="t108">气 象 数 据 预 测</div>
            <div class="content" id="d108"></div>
          </div>
        </div>
      </div>
      <div class="divs" style="width: 19.5%; height: 64%; left: 80%; top: 35%">
        <div class="title">城 市 环 境 模 型 评 估
          <button @click="fp2" v-show="p2"
                  style="position: absolute; width: 10%; height: 95%; left: 1%; top: 2.5%; background-color: #fff; color: #000; font-size: 12px; text-align: center">
            《
          </button>
          <button @click="fp1" v-show="p1"
                  style="position: absolute; width: 10%; height: 95%; right: 1%; top: 2.5%; background-color: #fff; color: #000; font-size: 12px; text-align: center">
            》
          </button>
        </div>
        <div class="content" style="height: 95%">
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 0; top: 0">
            <div class="title">济南</div>
            <div class="content" id="d1901"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 0">
            <div class="title">青岛</div>
            <div class="content" id="d1902"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 0; top: 25%">
            <div class="title">淄博</div>
            <div class="content" id="d1903"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 25%">
            <div class="title">枣庄</div>
            <div class="content" id="d1904"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 0; top: 50%">
            <div class="title">东营</div>
            <div class="content" id="d1905"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 50%">
            <div class="title">烟台</div>
            <div class="content" id="d1906"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 0; top: 75%">
            <div class="title">潍坊</div>
            <div class="content" id="d1907"></div>
          </div>
          <div v-show="p1" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 75%">
            <div class="title">济宁</div>
            <div class="content" id="d1908"></div>
          </div>

          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 0; top: 0">
            <div class="title">泰安</div>
            <div class="content" id="d1909"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 0">
            <div class="title">威海</div>
            <div class="content" id="d1910"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 0; top: 25%">
            <div class="title">日照</div>
            <div class="content" id="d1911"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 25%">
            <div class="title">临沂</div>
            <div class="content" id="d1912"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 0; top: 50%">
            <div class="title">德州</div>
            <div class="content" id="d1913"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 50%">
            <div class="title">聊城</div>
            <div class="content" id="d1914"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 0; top: 75%">
            <div class="title">滨州</div>
            <div class="content" id="d1915"></div>
          </div>
          <div v-show="p2" class="divs2" style="width: 49%; height: 24%; left: 50%; top: 75%">
            <div class="title">菏泽</div>
            <div class="content" id="d1916"></div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar,} from '@antv/g2plot';
// eslint-disable-next-line no-unused-vars
import {Rose, Sunburst, WordCloud, Line, Pie, Facet, Column, DualAxes, Gauge, Radar, Heatmap} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:5000/'

// eslint-disable-next-line no-unused-vars
let scene, l1, l2, l3, l4, l5, l6, l7, l8, l9

// eslint-disable-next-line no-unused-vars
let y = 2018, m = 1, hy = '工业', city = '济南', airType = 'CO',
    airType2 = 'O3', ydlb = '大工业'

// eslint-disable-next-line no-unused-vars
let color = [
  '#333311',
  '#444422',
  '#4C4C33',
  '#575744',
  '#887755',
  '#BB9966',
  '#CCAA77',
].reverse()

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
  fetch(localhost + y + "/d101")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(function (y, x) {
          return x.value - y.value
        })
        document.getElementById('t101').innerHTML = y + "年电力能源消耗"
        document.getElementById('d101').innerHTML = ""
        const line = new Bar('d101', {
          data,
          xField: 'value',
          yField: 'name',
          seriesField: 'name',
          xAxis: {
            grid: null,
          },
          smooth: true,
          yAxis: {
            label: null,
            grid: null,
          },
          color
        });
        line.render();
        let hoverData = {}
        line.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        line.on('plot:click', () => {
          ydlb = hoverData['name']
          d103()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d102() {
  fetch(localhost + 'd102')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d102').innerHTML = ""
        const area = new Area('d102', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          isPercent: true,
          yAxis: {
            label: false,
            grid: null
          },
          xAxis: {
            grid: null
          }
        });
        area.render();
      });
}

// eslint-disable-next-line no-unused-vars
function d103() {
  fetch(localhost + ydlb + "/d103")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t103').innerHTML = ydlb + "耗电发展"
        document.getElementById('d103').innerHTML = ""
        const piePlot = new Pie('d103', {
          data,
          angleField: '用电量',
          colorField: '年份',
          radius: 1,
          startAngle: Math.PI,
          endAngle: Math.PI * 1.5,
          label: {
            type: 'inner',
            offset: '-30%',
            content: ({percent}) => `${(percent * 100).toFixed(0)}%`,
            style: {
              fontSize: 14,
              textAlign: 'center',
            },
          },
          color,
          legend: true,
          interactions: [{type: 'element-active'}],
          pieStyle: {
            lineWidth: 0,
          },
        });
        piePlot.render();
        let hoverData = {}
        piePlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        piePlot.on('plot:click', () => {
          y = hoverData['年份']
          d101()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d104() {
  fetch(localhost + 'd104')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d104').innerHTML = ""
        const stackedBarPlot = new Bar('d104', {
          data: data.reverse(),
          isGroup: true,
          xField: 'value',
          yField: 'name',
          seriesField: 'type',
          label: false,
          color: [color[0], color[2]],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
        });
        stackedBarPlot.render();
        let hoverData = {}
        stackedBarPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        stackedBarPlot.on('plot:click', () => {
          y = hoverData['name']
          d105()
        })
      })
}

// eslint-disable-next-line no-unused-vars
function d105() {
  fetch(localhost + y + "/d105")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t105').innerHTML = y + "年行业经济占比"
        document.getElementById('d105').innerHTML = ""
        const plot = new Sunburst('d105', {
          data,
          innerRadius: 0.3,
          interactions: [{type: 'element-active'}],
          color,
          legend: {},
          label: {
            style: {
              fontSize: 10
            }
          }
        });
        plot.render();
      });
}

// eslint-disable-next-line no-unused-vars
function d106() {
  fetch(localhost + city + '/d106')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t106').innerHTML = city + "AQI色块图"
        const heatmapPlot = new Heatmap(document.getElementById('d106'), {
          data,
          xField: '年',
          yField: '月',
          colorField: 'AQI',
          legend: false,
          color,
          coordinate: {
            type: 'polar',
            cfg: {
              innerRadius: 0.2,
            },
          },
          heatmapStyle: {
            stroke: '#f5f5f5',
            opacity: 0,
          },
          meta: {
            time: {
              type: 'cat',
            },
            value: {
              min: 0,
              max: 1,
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
        let hoverData = {}
        heatmapPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        heatmapPlot.on('plot:click', () => {
          y = hoverData['年'].replace("年", "")
          m = hoverData['月'].replace("月", "")
          d107()
          d108()
          c190()
          fl1()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d107() {
  fetch(localhost + y + '/' + m + "/" + airType + "/d107")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(function (x, y) {
          return y.value - x.value
        })
        document.getElementById('t107').innerHTML = y + "-" + m + "-" + airType + "排行"
        document.getElementById('d107').innerHTML = ""
        const column = new Bar('d107', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          legend: false,
          color,
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
      });

}

// eslint-disable-next-line no-unused-vars
function d108() {
  fetch(localhost + y + "/" + airType2 + "/d108")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t108').innerHTML = y + "年" + airType2 + "热力图"
        document.getElementById('d108').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d108'), {
          data,
          xField: '城市',
          yField: '月',
          colorField: 'value',
          sizeField: 'value',
          shape: 'square',
          color,
          xAxis: {
            grid: null,
          },
          yAxis: {
            grid: null,
          },
          label: false,
        });
        heatmapPlot.render();
      });

}

// eslint-disable-next-line no-unused-vars
function d109() {
  fetch(localhost + 'd109')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d109').innerHTML = ""
        const line = new Bar('d109', {
          data,
          // padding: 5,
          xField: 'GDP',
          yField: 'name',
          seriesField: 'GDP',
          legend: false,
          color,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
        });

        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function d190(div, city) {
  fetch(localhost + y + "/" + m + "/" + city + "/d190")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById(div).innerHTML = ""
        const rosePlot = new Rose(div, {
          data,
          xField: 'name',
          yField: 'value',
          color,
          legend: false,
          seriesField: 'name',
          radius: 0.7,
        });
        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', () => {
          airType2 = hoverData['name']
          d108()
        })
        rosePlot.on('plot:dblclick', () => {
          airType = hoverData['name']
          d107()
          fl1()
        })
      })
}

// eslint-disable-next-line no-unused-vars
function c190() {
  let citys = ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '临沂', '德州', '聊城', '滨州', '菏泽']
  for(let i=1901; i<=1916; i+=1) {
    d190('d' + i.toString(), citys[i-1901])
  }
}

// eslint-disable-next-line no-unused-vars
function fl1() {
   fetch(localhost + y + "/" + m + "/" + airType + '/l1')
        .then(res => res.json())
        .then(data => {
          l1.setData(data)
        });
}

// eslint-disable-next-line no-unused-vars
function init() {
  d101()
  d102()
  d103()
  d104()
  d105()
  d106()
  d107()
  d108()
  d109()
  c190()
}

export default {
  name: "app",
  components: {},
  data() {
    return {
      p1: 1,
      p2: 0


    }
  },
  methods: {
    fp1() {
      this.p2 = 1;
      this.p1 = 0
    },
    fp2() {
      this.p2 = 0;
      this.p1 = 1
    }

  },
  mounted() {
    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        pitch: 45,
        style: 'amap://styles/66156ec93d7481b949829a24124aefc4?isPublic=true',
        center: [118.154058, 35.925513],
        zoom: 4.9
      })
    });


    fetch(localhost + y + "/" + m + "/" + airType + '/l1')
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
              .shape('cylinder')
              .size('value', function (ev) {
                return [5, 5, 20 + ev / 4];
              })
              .color('value', color)
              .style({
                opacity: 1,
                lightEnable: false
              });
          scene.addLayer(l1);
        });


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
  width: 99.6%;
  height: 88%;
  left: 0.2%;
  top: 25px;
  text-align: center;
  font-size: 18px;
  color: #000;
  font-weight: bold;
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
  background-color: #999;
  font-weight: bold;
}

.divs {
  position: absolute;
  background-color: #f7f7f7;
  text-align: center;
  border-width: 3px;
  border-color: #ddd;
  border-style: inset;
}

.divs2 {
  position: absolute;
  background-color: #f7f7f7;
  text-align: center;
  border-width: 1px;
  border-color: #ddd;
  border-style: inset;
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