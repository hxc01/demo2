<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div
        id="map"
        style="position: absolute;width: 98%;height: 87%;left: 1%;top: 8.5%;">
      <div style="position: absolute;width: 99%;height: 99%;left: 0.5%;top: 0.5%">
        <div class="divs" style="width: 19.5%; height: 19%;left: 0;top: 0">
          <div id="d1" class="content"></div>
          <div id="t1" class="title"></div>
        </div>
        <div class="divs" style="width: 19.5%; height: 29%;left: 0;top: 20%">
          <div id="d2" class="content"></div>
          <div id="t2" class="title"></div>
        </div>
        <div class="divs" style="width: 9.5%; height: 19%;left: 0;top: 50%">
          <div id="d3" class="content"></div>
          <div id="t3" class="title"></div>
        </div>
        <div class="divs" style="width: 9.5%; height: 19%;left: 10%;top: 50%">
          <div id="d4" class="content"></div>
          <div id="t4" class="title" style="width: 100%; left: 0; font-size: 5px"></div>
        </div>
        <div class="divs" style="width: 19.5%; height: 29%;left: 0;top: 70%">
          <div id="d5" class="content"></div>
          <div id="t5" class="title"></div>
        </div>
        <div class="divs" style="width: 49.5%; height: 19%;left: 20%;top: 80%">
          <div id="d6" class="content"></div>
          <div id="t6" class="title"></div>
        </div>

        <div class="divs" style="width: 14.5%; height: 19%;left: 70%;top: 80%">
          <div id="d7" class="content">
            <div id="div6_1" style="position: absolute; width: 50%; height: 160%; left: -10%; top: -30%"></div>
            <div id="div6_2" style="position: absolute; width: 50%; height: 160%; left: 24%; top: -30%"></div>
            <div id="div6_3" style="position: absolute; width: 50%; height: 160%; left: 57%; top: -30%"></div>
          </div>
          <div id="t7" class="title" style="font-size: 5px"></div>
        </div>
        <div class="divs" style="width: 14.5%; height: 19%;left: 85%;top: 80%">
          <div id="d8" class="content">
            <div id="div5_1" style="position: absolute; width: 50%; height: 160%; left: -10%; top: -30%"></div>
            <div id="div5_2" style="position: absolute; width: 50%; height: 160%; left: 24%; top: -30%"></div>
            <div id="div5_3" style="position: absolute; width: 50%; height: 160%; left: 57%; top: -30%"></div>
          </div>
          <div id="t8" class="title" style="font-size: 5px"></div>
        </div>

        <div id="d13" class="divs" style="width: 9.5%; height: 19%;right: 0;top: 0"></div>
        <div id="d10" class="divs" style="width: 9.5%; height: 19%;right: 10%;top: 0"></div>
        <div id="d11" class="divs" style="width: 9.5%; height: 19%;right: 0;top: 20%"></div>
        <div id="d12" class="divs" style="width: 9.5%; height: 19%;right: 10%;top: 20%"></div>
        <div class="divs" style="width: 19.5%; height: 39%;right: 0;top: 40%">
          <div id="d9" class="content"></div>
          <div id="t9" class="title"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {GaodeMap, HeatmapLayer, LineLayer, PointLayer, Popup, Scene} from "@antv/l7";
import {Area, Bar, Liquid, Pie, RingProgress, Rose, Scatter, WordCloud} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene, HeatLayer, flyLayer

// eslint-disable-next-line no-unused-vars
let zdmc = '糖尿病胰岛素治疗', age = '60', xb = "男", jgdj = "一级", yllb = "门诊慢特病", rycs, layer1


// eslint-disable-next-line no-unused-vars
function fZdmc() {
  c1()
  c4()
  c6()
  c7()
  c8()
  c9()
  c10()
  c12()
  c13()
  heatLayer()
  flyLines()
}


// eslint-disable-next-line no-unused-vars
function fAge() {
  c1()
  c2()
  c3()
  c5()
  flyLines()
}

// eslint-disable-next-line no-unused-vars
function fJgdj() {
  c9()
  c12()
}

// eslint-disable-next-line no-unused-vars
function fYllb() {
  c11()
}

// eslint-disable-next-line no-unused-vars
function fXB() {
  flyLines()
}

// eslint-disable-next-line no-unused-vars
function c1() {
  fetch(localhost + age + "/" + zdmc + "/d1")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1').innerHTML = zdmc + age + "岁住院时长情况"
        document.getElementById('d1').innerHTML = ""
        const piePlot = new Pie('d1', {
          data,
          angleField: '平均住院时长',
          colorField: 'name',
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
function c2() {
  fetch(localhost + age + "/d2")
      .then((res) => res.json())
      .then((data) => {
        // eslint-disable-next-line no-unused-vars
        function cmp(x, y) {
          return y.诊断人数 - x.诊断人数
        }

        data = data.sort(cmp)
        document.getElementById('t2').innerHTML = age + "岁病症排行"
        document.getElementById('d2').innerHTML = ""
        const bar = new Bar('d2', {
          data,
          xField: '诊断人数',
          yField: '诊断名称',
          scrollbar: {
            type: 'vertical',
          },
          color: ['#0ef', '#07b', '#039'],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
        });
        bar.render();
        let hoverData = {}
        bar.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        bar.on('plot:click', ev => {
          ev = ""
          zdmc = hoverData['诊断名称'] + ev
          fZdmc()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c3() {
  fetch(localhost + age + "/d3")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d3').innerHTML = ""
        const ringProgress = new RingProgress('d3', {
          percent: data['value'],
          color: ['#00ffbb', '#E8EDF3'],
          innerRadius: 0.85,
          radius: 0.98,
          statistic: {
            title: {
              style: {color: '#363636', fontSize: '3px', lineHeight: '30px'},
              formatter: () => age + "岁报销比",
            },
          },
        });

        ringProgress.render();
      })
}

// eslint-disable-next-line no-unused-vars
function c4() {
  fetch(localhost + zdmc + "/d4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t4').innerHTML = zdmc
        document.getElementById('d4').innerHTML = ""
        const ringProgress = new RingProgress('d4', {
          percent: data['value'],
          color: ['#00bbff', '#E8EDF3'],
          innerRadius: 0.85,
          radius: 0.98,
          statistic: {
            title: {
              style: {color: '#363636', fontSize: '12px', lineHeight: '14px'},
              formatter: () => "报销比",
            },
          },
        });

        ringProgress.render();
      })
}

// eslint-disable-next-line no-unused-vars
function c5() {
  fetch(localhost + age + "/d5")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t5').innerHTML = age + "岁病症词云"
        document.getElementById('d5').innerHTML = ""
        const wordCloud = new WordCloud('d5', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'name',
          wordStyle: {
            fontFamily: 'Avenir',
            fontSize: [4, 20],
            rotation: 45,
          },
        });
        wordCloud.render();
      });
}

// eslint-disable-next-line no-unused-vars
function c6() {
  fetch(localhost + zdmc + '/d6')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t6').innerHTML = zdmc + "年龄分布图"
        document.getElementById('d6').innerHTML = ""
        const area = new Area('d6', {
          data,
          xField: '年龄',
          yField: '人数',
          isStack: true,
          seriesField: '性别',
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true
        });
        area.render();
        let hoverData = {}
        area.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        area.on('plot:click', ev => {
          ev = ""
          age = hoverData['年龄'] + ev
          fAge()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function div6(div, percent, title) {
  const liquidPlot = new Liquid(div, {
    percent: percent,
    shape: 'rect',
    colorField: percent,
    statistic: {
      title: {
        content: title,
        style: {
          fontSize: '6px',
          color: '#000'
        }
      },
      content: {
        style: {
          fontSize: '6px',
          color: '#000'
        }
      }
    },
    outline: {
      border: 2,
      distance: 4,
    },
    wave: {
      length: 120,
    },
    label: false,
  });
  liquidPlot.render();
}

// eslint-disable-next-line no-unused-vars
function c7() {
  fetch(localhost + zdmc + '/d7')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div6_1').innerHTML = ""
        document.getElementById('div6_2').innerHTML = ""
        document.getElementById('div6_3').innerHTML = ""
        document.getElementById('t7').innerHTML = "各级医院" + zdmc + "减免比例"
        div6('div6_1', data[0]['percent'], data[0]['JGDJ'], "一级")
        div6('div6_2', data[1]['percent'], data[1]['JGDJ'], "二级")
        div6('div6_3', data[2]['percent'], data[2]['JGDJ'], "三级")
      });
}

// eslint-disable-next-line no-unused-vars
function c8() {
  fetch(localhost + zdmc + '/d8')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div5_1').innerHTML = ""
        document.getElementById('div5_2').innerHTML = ""
        document.getElementById('div5_3').innerHTML = ""
        document.getElementById('t8').innerHTML = "各级医院" + zdmc + "复诊率"
        div6('div5_1', data[0]['percent'], data[0]['JGDJ'], "一级")
        div6('div5_2', data[1]['percent'], data[1]['JGDJ'], "二级")
        div6('div5_3', data[2]['percent'], data[2]['JGDJ'], "三级")
      });
}

// eslint-disable-next-line no-unused-vars
function c9() {
  fetch(localhost + zdmc + "/" + jgdj + "/d9")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t9').innerHTML = zdmc + jgdj + "医院统筹费用情况"
        document.getElementById('d9').innerHTML = ""
        const plot = new Scatter('d9', {
          data,
          xField: '年龄',
          yField: '平均统筹费用',
          colorField: '性别',
          size: 5,
          shape: 'circle',
          pointStyle: {
            fillOpacity: 1,
          },
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          brush: {
            enabled: true,
            mask: {
              style: {
                fill: 'rgba(255,0,0,0.15)',
              },
            },
          },
        });
        plot.render();
      });
}

// eslint-disable-next-line no-unused-vars
function c10() {
  fetch(localhost + zdmc + "/d10")
      .then((res) => res.json())
      .then((data) => {
        // document.getElementById('t10').innerHTML = zdmc+"不同机构等级就诊人数"
        document.getElementById('d10').innerHTML = ""
        const rosePlot = new Rose('d10', {
          data,
          xField: '机构等级',
          yField: '就诊人数',
          seriesField: '机构等级',
          radius: 0.7,
          legend: false,
        });

        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', ev => {
          ev = ""
          jgdj = hoverData['机构等级'] + ev
          fJgdj()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c12() {
  fetch(localhost + zdmc + "/" + jgdj + "/d12")
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return y.就诊人数 - x.就诊人数
        }

        data = data.sort(cmp)
        document.getElementById('d12').innerHTML = ""
        const rosePlot = new Rose('d12', {
          data,
          xField: '人员城市',
          yField: '就诊人数',
          seriesField: '人员城市',
          radius: 0.7,
          legend: false,
          label: false
        });

        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', ev => {
          ev = ""
          rycs = hoverData['人员城市'] + ev

        });
      })
}

// eslint-disable-next-line no-unused-vars
function c13() {
  fetch(localhost + zdmc + "/d13")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d13').innerHTML = ""
        const rosePlot = new Rose('d13', {
          data,
          xField: '医疗类别',
          yField: '就诊人数',
          seriesField: '医疗类别',
          radius: 0.7,
          legend: false,
        });

        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', ev => {
          ev = ""
          yllb = hoverData['医疗类别'] + ev
          fYllb()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function c11() {
  fetch(localhost + zdmc + "/" + yllb + "/d11")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d11').innerHTML = ""
        const rosePlot = new Rose('d11', {
          data,
          xField: '性别',
          yField: '就诊人数',
          seriesField: '性别',
          radius: 0.7,
          legend: false,
        });

        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', ev => {
          ev = ""
          xb = hoverData['性别'] + ev
          fXB()
        });
      })
}

// eslint-disable-next-line no-unused-vars
function heatLayer() {
  fetch(localhost + zdmc + '/heat')
      .then(res => res.json())
      .then(data => {
        HeatLayer.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function flyLines() {
  fetch(localhost + zdmc + "/" + age + '/' + xb + '/flyLines')
      .then(res => res.json())
      .then(data => {
        flyLayer.setData(data)
      });
}

export default {
  name: "ybdsjp1",
  components: {},
  data() {
    return {}
  },
  methods: {},
  mounted() {

    // eslint-disable-next-line no-undef
    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        pitch: 60,
        type: 'amap',
        style: 'amap://styles/83b73ccd633185b096afe1b7035f9a1c?isPublic=true',
        center: [119.295469, 35.357701],
        zoom: 8.5,
      })
    });


    scene.on('loaded', () => {
      fetch(localhost + zdmc + '/heat')
          .then(res => res.json())
          .then(data => {
            layer1 = new PointLayer({})
                .source(data, {
                  parser: {
                    x: 'jd',
                    y: 'wd',
                    type: 'json'
                  }
                })
                .shape('circle')
                .size('value', [4, 32])
                .color('value', [
                  '#34B6B7',
                  '#4AC5AF',
                  '#5FD3A6',
                  '#7BE39E',
                  '#A1EDB8',
                ])
                .active(true)
                .style({
                  opacity: 0.9,
                  strokeWidth: 0
                });
            scene.addLayer(layer1);
          });
    });

    scene.on('loaded', () => {
      fetch(localhost + zdmc + "/" + age + '/' + xb + '/flyLines')
          .then(res => res.json())
          .then(data => {
            flyLayer = new LineLayer({
              blend: 'normal'
            })
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'lng1',
                    y: 'lat1',
                    x1: 'lng2',
                    y1: 'lat2'
                  }
                })
                .size(4)
                .shape('arc3d')
                .color('#FF7C6A')
                .animate({
                  enable: true,
                  interval: 0.1,
                  trailLength: 0.5,
                  duration: 2
                })
                .style({
                  opacity: 0.8
                });
            scene.addLayer(flyLayer);
            flyLayer.on('click', e => {
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(e.lngLat)
                  .setHTML(
                      `<span>人员区划: ${e.feature.人员城市}</span>` + `<br>` +
                      `<span>就诊区划: ${e.feature.就诊城市}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });


    c1()
    c2()
    c3()
    c4()
    c5()
    c6()
    c7()
    c8()
    c9()
    c10()
    c12()
    c13()
    c11()


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