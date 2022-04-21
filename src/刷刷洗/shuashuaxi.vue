<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #f7f7f7">
    <div
        style="position: absolute; left: -0.3%; width: 14.2%; top: 0; height: 100%; background-color: #fff; border-style: dot-dot-dash"></div>
    <el-col :span="12" style="position: absolute; width: 20%; left: -6%; top: 0; height: 100%">
      <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose">
        <el-menu-item index="1" @click="fp1">
          <i class="el-icon-location"> 疫 情 地 图 </i>
          <span slot="title"></span>
        </el-menu-item>
        <el-menu-item index="2" @click="fp2">
          <i class="el-icon-menu"> 密 接 追 踪 </i>
          <span slot="title"></span>
        </el-menu-item>
        <el-menu-item index="3" @click="fp3">
          <i class="el-icon-document"> 疫 情 数 据 </i>
          <span slot="title"></span>
        </el-menu-item>
        <el-menu-item index="4" @click="fp4">
          <i class="el-icon-setting"> 密 接 数 据 </i>
          <span slot="title"></span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <div style="position: absolute; left: 14%; width: 86%; height: 100%; top: 0;">
      <div class="title" style="height: 40px">疫情多维动态监控管理系统</div>
      <div class="content" style="height: 93%; top: 41px" v-show="p1">
        <div class="divs" style="width: 39%; height: 39%; left: 60%; top: 0">
          <div class="title" id="t102">疫情发展趋势</div>
          <div class="content" id="d102"></div>
        </div>
        <div class="divs" style="width: 39%; height: 59%; left: 60%; top: 40%">
          <div class="title" id="t103">疫情发展热力</div>
          <div class="content" id="d103"></div>
        </div>
      </div>
      <div class="content" style="height: 93%; top: 41px" v-show="p2">
        <div class="divs" style="width: 39%; height: 49%; left: 60%; top: 0">
          <div class="title" id="t201">密接流动图</div>
          <div class="content" id="d201"></div>
        </div>
        <div class="divs" style="width: 39%; height: 49%; left: 60%; top: 50%">
          <div class="title" id="t202">次密接桑基图</div>
          <div class="content" id="d202"></div>
        </div>
      </div>
      <div class="content" style="height: 93%; top: 41px" v-show="p3">
        <shuashuaxip3></shuashuaxip3>
      </div>
      <div class="content" style="height: 93%; top: 41px" v-show="p4">
        <shuashuaxip4></shuashuaxip4>
      </div>
      <div class="divs" style="width: 59%; height: 92%; left: 0; top: 41px" v-show="p1||p2">
        <div class="title" id="t101">疫情地图</div>
        <div class="content" id="d101" style="height: 95%">
          <div class="divs" style="width: 100%; height: 29%; left: 0; bottom: 0; z-index: 9999">
            <div class="title" id="t104"></div>
            <div class="content" id="d104"></div>
          </div>
        </div>
      </div>
    </div>
    <div v-show="p1||p2">
      <button @click="fl1" class="selects" style="left: 14%; top: 9.5%">现存确诊</button>
      <button @click="fl2" class="selects" style="left: 19%; top: 9.5%">阳性分布</button>
      <button @click="fl3" class="selects" style="left: 24%; top: 9.5%">密接分布</button>
      <button @click="fl4" class="selects" style="left: 29%; top: 9.5%">次接分布</button>
      <button @click="fl5" class="selects" style="left: 34%; top: 9.5%">密接轨迹</button>
      <button @click="fl6" class="selects" style="left: 39%; top: 9.5%">次接轨迹</button>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, LineLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Chord, Line, Sankey} from '@antv/g2plot';
// eslint-disable-next-line no-unused-vars
import {Pie, G2, Radar, Liquid, Gauge, Area, Bar, Heatmap, Rose, Violin, RadialBar, Progress} from '@antv/g2plot';
// eslint-disable-next-line no-unused-vars
import {PivotSheet} from '@antv/s2';


// eslint-disable-next-line no-unused-vars
import {DrawControl} from "@antv/l7-draw";

// eslint-disable-next-line no-unused-vars
import * as echarts from "echarts";
import Shuashuaxip3 from "./shuashuaxip3";
import Shuashuaxip4 from "./shuashuaxip4";

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:4500/"

// eslint-disable-next-line no-unused-vars
let scene, drawControl, lng1, lat1, lng2, lat2, l1, l2, l3, l4, l5, l6, l7

// eslint-disable-next-line no-unused-vars
let city = "济南", y = 2022, m = 4, d = 5, types = "累计确诊", date = '2022-04-05'

// eslint-disable-next-line no-unused-vars
let color = [
  '#336699',
  '#6699cc',
  '#aabbcc',
  '#cc9977',
  '#cc5533',
  '#aa2200',
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
  fetch(localhost + y + "/" + m + "/" + d + "/d101")
      .then((res) => res.json())
      .then((data) => {
        l1.setData(data)
      });
}


// eslint-disable-next-line no-unused-vars
function d102() {
  fetch(localhost + 'd102')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d102').innerHTML = ""
        const line = new Line('d102', {
          data,
          xField: 'date',
          yField: 'value',
          seriesField: 'type',
          yAxis: {
            grid: null,
          },
          color,
          slider: {
            start: 0.9,
            end: 1
          }
        });
        line.render();
        let jsonData = {}
        line.on('tooltip:change', (ev) => {
          jsonData = ev
        })
        line.on('plot:click', (ev) => {
          // console.log(jsonData.data.items[0])
          // console.log(ev.data.data[0])
          y = (jsonData.data.items[0]['title'] / 10000).toFixed(0)
          m = (jsonData.data.items[0]['title'] / 100).toFixed(0) % 100
          d = (jsonData.data.items[0]['title'] / 1).toFixed(0) % 100
          types = ev.data.data[0]['type']
          d101()
          d103()
          d104()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d103() {
  fetch(localhost + y + "/" + city + "/" + types + "/d103")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t103').innerHTML = city + types + y + "年变化热力图"
        document.getElementById('d103').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d103'), {
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
        heatmapPlot.on('plot:click', (ev) => {
          m = ev['data']['data']['月'].replace("月", "")
          d = ev['data']['data']['日'].replace("日", "")
          d101()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d104() {
  fetch(localhost + y + "/" + city + "/d104")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t104').innerHTML = city + y + "年疫情趋势"
        document.getElementById('d104').innerHTML = ""
        const area = new Area('d104', {
          data,
          xField: 'date',
          yField: 'value',
          seriesField: 'type',
          slider: {
            start: 0,
            end: 1,
          },
          color,
          smooth: true,
          yAxis: {
            grid: null
          }
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', (ev) => {
          jsonData = ev.data.items[0]
        })
        area.on('plot:click', () => {
          date = jsonData['title']
          d201()
          d202()
          initDate()
        })
      })
}

// eslint-disable-next-line no-unused-vars
function d201() {
  fetch(localhost + date + '/d201')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t201').innerHTML = date + "密接流动图"
        document.getElementById('d201').innerHTML = ""
        const chord = new Chord('d201', {
          data,
          theme: {
            colors10: [
              '#336699',
              '#6699cc',
              '#aabbcc',
              '#cc9977',
              '#cc5533',
              '#aa2200',
              '#cc9977',
              '#aabbcc',
              '#6699cc',
              '#336699',
            ],
          },
          color,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          seriesField: 'source',
        });
        chord.render();
      })
}

// eslint-disable-next-line no-unused-vars
function d202() {
  fetch(localhost + date + '/d201')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t202').innerHTML = date + "次密接流动图"
        document.getElementById('d202').innerHTML = ""
        const sankey = new Sankey('d202', {
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
function initDate() {
  fetch(localhost + date + '/d203')
      .then((res) => res.json())
      .then((data) => {
        l2.setData(data)
      });
  fetch(localhost + date + '/d204')
      .then((res) => res.json())
      .then((data) => {
        l3.setData(data)
      });
  fetch(localhost + date + '/d205')
      .then((res) => res.json())
      .then((data) => {
        l4.setData(data)
      });
  fetch(localhost + date + '/d206')
      .then((res) => res.json())
      .then((data) => {
        l5.setData(data)
      });
  fetch(localhost + date + '/d207')
      .then((res) => res.json())
      .then((data) => {
        l6.setData(data)
      });
}

export default {
  name: "app",
  components: {
    Shuashuaxip3,
    Shuashuaxip4
  },
  data() {
    return {
      p1: 1,
      p2: 0,
      p3: 0,
      p4: 0,


      l1: 1,
      l2: 0,
      l3: 0,
      l4: 0,
      l5: 0,
      l6: 0

    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    fp1() {
      this.p1 = 1
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
    },
    fp2() {
      this.p1 = 0
      this.p2 = 1
      this.p3 = 0
      this.p4 = 0
    },
    fp3() {
      this.p1 = 0
      this.p2 = 0
      this.p3 = 1
      this.p4 = 0
    },
    fp4() {
      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 1
    },
    fl1() {
      if (this.l1) {
        this.l1 = 0;
        l1.hide()
      } else {
        this.l1 = 1;
        l1.show()
      }
    },
    fl2() {
      if (this.l2) {
        this.l2 = 0;
        l2.hide()
      } else {
        this.l2 = 1;
        l2.show()
      }
    },
    fl3() {
      if (this.l3) {
        this.l3 = 0;
        l3.hide()
      } else {
        this.l3 = 1;
        l3.show()
      }
    },
    fl4() {
      if (this.l4) {
        this.l4 = 0;
        l1.hide()
      } else {
        this.l4 = 1;
        l4.show()
      }
    },
    fl5() {
      if (this.l5) {
        this.l5 = 0;
        l5.hide()
      } else {
        this.l5 = 1;
        l5.show()
      }
    },
    fl6() {
      if (this.l6) {
        this.l6 = 0;
        l6.hide()
      } else {
        this.l6 = 1;
        l6.show()
      }
    },

  },
  mounted() {

    scene = new Scene({
      id: 'd101',
      map: new GaodeMap({
        pitch: 45,
        style: 'amap://styles/ac239e8628904a93dfa30ccbb6dd9521?isPublic=true',
        center: [119.960904, 36.428165],
        zoom: 5.5
      })
    });


    fetch(localhost + y + "/" + m + "/" + d + "/d101")
        .then((res) => res.json())
        .then((data) => {
          l1 = new PointLayer({})
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('cylinder')
              .size('value', function (level) {
                return [6, 6, level / 5];
              })
              // .animate(true)
              .active(true)
              .color('value', color)
              .style({
                opacity: 1.0
              });
          scene.addLayer(l1)
          l1.on('click', (ev) => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">${ev.feature['name']}</span>` + '<br>' +
                    `<span style="color: #777">${ev.feature['date']}</span>` + '<br>' +
                    `<span style="color: #777">新增确诊：${ev.feature['确诊']}</span>` + '<br>' +
                    `<span style="color: #777">新增疑似：${ev.feature['疑似']}</span>` + '<br>' +
                    `<span style="color: #777">新增治愈：${ev.feature['治愈']}</span>` + '<br>' +
                    `<span style="color: #777">累计确诊：${ev.feature['累计确诊']}</span>` + '<br>' +
                    `<span style="color: #777">累计疑似：${ev.feature['累计疑似']}</span>` + '<br>' +
                    `<span style="color: #777">累计死亡：${ev.feature['累计死亡']}</span>` + '<br>' +
                    `<span style="color: #777">累计治愈：${ev.feature['累计治愈']}</span>` + '<br>' +
                    `<span style="color: #777">现有确诊：${ev.feature['value']}</span>`
                );
            scene.addPopup(popup);
            city = ev.feature['name']
            d103()
            d104()
          })
        })


    fetch(localhost + date + '/d203')
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
              .size('value', [0, 90])
              .color('#bb3300')
              .active(true)
              .animate(true)
              .style({
                opacity: 1,
                strokeWidth: 0
              });
          scene.addLayer(l2);
          l2.hide()
        })

    fetch(localhost + date + '/d204')
        .then((res) => res.json())
        .then((data) => {
          l3 = new PointLayer({})
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('circle')
              .size('value', [0, 75])
              .color('#bb7700')
              .active(true)
              .animate(true)
              .style({
                opacity: 1,
                strokeWidth: 0
              });
          scene.addLayer(l3);
          l3.hide()
        })

    fetch(localhost + date + '/d205')
        .then((res) => res.json())
        .then((data) => {
          l4 = new PointLayer({})
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('circle')
              .size('value', [0, 60])
              .color('#bbaa00')
              .active(true)
              .animate(true)
              .style({
                opacity: 1,
                strokeWidth: 0
              });
          scene.addLayer(l4);
          l4.hide()
        })

    fetch(localhost + date + '/d206')
        .then((res) => res.json())
        .then((data) => {
          l5 = new LineLayer({
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
              .size('value', [0.2, 5])
              .shape('arc3d')
              .color(color[0])
              .animate({
                interval: 0.5,
                trailLength: 0.5,
                duration: 5
              })
              .style({
                opacity: 0.5
              });
          scene.addLayer(l5);
          l5.hide()
        })

    fetch(localhost + date + '/d207')
        .then((res) => res.json())
        .then((data) => {
          l6 = new LineLayer({
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
              .size('value', [0.2, 5])
              .shape('arc3d')
              .color(color[4])
              .animate({
                interval: 0.5,
                trailLength: 0.5,
                duration: 5
              })
              .style({
                opacity: 0.5
              });
          scene.addLayer(l6);
          l6.hide()
        })

    d102()
    d103()
    d104()
    d201()
    d202()


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
  height: 91%;
  left: 0;
  top: 25px;
  text-align: center;
  font-size: 20%;
  color: #f7f7f7;
  font-weight: bold;
  /*border-style: groove;*/
  /*border-width: 1px;*/
}

.title {
  position: absolute;
  width: 100%;
  height: 24px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 16px;
  color: #000;
  background-color: #f7f7f7;
  font-weight: bold;
  /*border-style: groove;*/
  /*border-width: 1px;*/
}

.divs {
  position: absolute;
  background-color: #f7f7f7;
  text-align: center;
  border-width: 1px;
  border-color: #eeeeee;
  border-style: ridge;
}

.selects {
  position: absolute;
  width: 70px;
  height: 20px;
  background-color: #fff;
  border-color: #bbb;
  border-width: 2px;
  /*border-style: inset;*/
  color: #000;
  border-radius: 5px;
  z-index: 9999;
  font-size: 5px;
  font-weight: bold;
  text-align: center;
}
</style>
