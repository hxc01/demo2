<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0">


    <dv-border-box4
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 50%;left: 0;top: 0"
    >
      <div id="div301" class="content"></div>
      <div id="t301" class="title"></div>
    </dv-border-box4>

    <dv-border-box13
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 50%;left: 0;top: 50%"
    >
      <div id="t302" class="title"></div>
      <div id="div302" style="position: absolute;height: 60%;top: 10%" class="content"></div>
      <div id="div3021" style="position: absolute;height: 25%;top: 70%" class="content"></div>
    </dv-border-box13>

    <dv-border-box6
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 28%;height: 30%;left: 22%;top: 70%"
    >
      <div id="t303" class="title"></div>
      <div id="div303" class="content"></div>
    </dv-border-box6>


    <dv-border-box1
        style="position: absolute; width: 56%; height: 60%; left: 22%; top: 10%; color: #007700"
        :color="['#aaaaaa', '#eeeeee']"
    >
      <div id="map3" class="content"></div>
    </dv-border-box1>


    <dv-border-box6
        :reverse="true"
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 28%;height: 30%;right: 22%;top: 70%"
    >
      <div id="t306" class="title"></div>
      <div id="div306" class="content"></div>
    </dv-border-box6>


    <dv-border-box13
        :reverse="true"
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 60%;right: 0;top: 0"
    >
      <div id="t305" class="title"></div>
      <div id="div305" style="position: absolute;height: 60%;top: 10%" class="content"></div>
      <div id="div3051" style="position: absolute;height: 40%;top: 60%" class="content"></div>
    </dv-border-box13>

    <dv-border-box4
        :reverse="true"
        :color="['#aaaaaa', '#eeeeee']"
        style="position: absolute;width: 22%;height: 40%;right: 0;bottom: 0"
    >
      <div id="t304" class="title"></div>
      <div id="div304" class="content"></div>
    </dv-border-box4>


  </div>
</template>

<script>


// eslint-disable-next-line no-unused-vars
import {GaodeMap, PointLayer, Popup, Scene} from "@antv/l7";
import insertCss from "insert-css";
import {each, groupBy} from "@antv/util";
import {Bar, Column, Gauge, Pie} from "@antv/g2plot";
import {PivotSheet} from "@antv/s2";


// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:5000/'


// eslint-disable-next-line no-unused-vars
let scene, layer1, layer2


// eslint-disable-next-line no-unused-vars
let colors1 = [
  '#33aa33',
  '#776677',
  '#449944',
  '#885588',
  '#558855',
  '#667766',
  '#994499',
]
// eslint-disable-next-line no-unused-vars
let colors2 = [
  '#33aa33',
  '#994499',
  '#33aaaa',
  '#3a3aaa',
  '#aaaa33',
]
// eslint-disable-next-line no-unused-vars
let colors3 = [
  '#33aa33',
  '#449944',
  '#558855',
  '#667766',
  '#776677',
  '#885588',
  '#994499',
]
// eslint-disable-next-line no-unused-vars
let age1 = 60, age2 = 81

// eslint-disable-next-line no-unused-vars
let jg1 = '招远市夏甸镇东庄卫生院', jg2 = '烟台圣莱恩康复医院'

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
function div301() {
  fetch(localhost + age1 + "/div301")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('t301').innerHTML = age1 + "岁签约服务包情况"
        document.getElementById('div301').innerHTML = ""
        const column = new Bar('div301', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          color: colors3,
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
        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        //   zbmc = hoverData['name'] + ev
        // });
      });
}

// eslint-disable-next-line no-unused-vars
function div302() {
  fetch(localhost + age1 + "/" + jg1 + '/div302')
      .then((res) => res.json())
      .then((data) => {
        let dataConfig = data;
        document.getElementById('t302').innerHTML = age1+"岁"+jg1+"签约情况"
        document.getElementById('div302').innerHTML = ""
        const container = document.getElementById('div302');
        const s2Options = {
          width: 270,
          height: 200,
        };
        const s2Palette = {
          basicColors: [
            '#000',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#FFFFFF',
            '#eee',
            '#999',
            '#88',
            '#77',
            '#666',
            '#000',
          ],
          semanticColors: {
            red: '#FF4D4F',
            green: '#29A294',
          },
        };
        const s2 = new PivotSheet(container, dataConfig, s2Options);
        s2.setThemeCfg({palette: s2Palette});
        s2.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div3021(div = 'div3021') {
  document.getElementById(div).innerHTML = ""
  let div1 = document.createElement('div')
  let div2 = document.createElement('div')
  let div3 = document.createElement('div')
  document.getElementById(div).appendChild(div1)
  document.getElementById(div).appendChild(div2)
  document.getElementById(div).appendChild(div3)
  div1.id = div + "div1"
  div1.style.position = 'absolute'
  div1.style.width = '33%'
  div1.style.height = '98%'
  div1.style.left = '1%'
  div1.style.top = '1%'
  div2.id = div + "div2"
  div2.style.position = 'absolute'
  div2.style.width = '33%'
  div2.style.height = '98%'
  div2.style.left = '34%'
  div2.style.top = '1%'
  div3.id = div + "div3"
  div3.style.position = 'absolute'
  div3.style.width = '33%'
  div3.style.height = '98%'
  div3.style.left = '67%'
  div3.style.top = '1%'
  document.getElementById(div+'div1').innerHTML = ""
  document.getElementById(div+'div2').innerHTML = ""
  document.getElementById(div+'div3').innerHTML = ""
  fetch(localhost + age1 + "/" + jg1 + "/div3021")
      .then((res) => res.json())
      .then((data) => {
        let div1data = data['data']
        let div2data = data['jg']
        let div3data = data['age']
        const pie = new Pie(div + "div1", {
          data: div1data,
          colorField: 'name',
          color: colors2,
          angleField: 'value',
          label: false,
          tooltip: false,
          state: {
            // 设置【active】激活状态样式 - 无描边
            active: {
              style: {
                lineWidth: 0,
              },
            },
          },
        });
        pie.render();
        let gauge2 = new Gauge(div+'div2', {
          percent: div2data['value'],
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
              formatter: () => String((div2data['value']).toFixed(4) * 100).slice(0, 5) + "%",
            },
            content: {
              offsetY: 12,
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => div2data['name'],
            },
          },
        });
        gauge2.render();
        let gauge3 = new Gauge(div+'div3', {
          percent: div3data['value'],
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
              formatter: () => String((div3data['value']).toFixed(4) * 100).slice(0, 5) + "%",
            },
            content: {
              style: {
                fontSize: '12px',
                lineHeight: '22px',
                color: '#4B535E',
              },
              formatter: () => div3data['name'] + "岁",
            },
          },
        });
        gauge3.render();
      });
}


// eslint-disable-next-line no-unused-vars
function div303(div = 'div303', url = localhost + 'div303', color = [colors1[0], colors1[6]]) {
  insertCss(`
        #container {
          display: flex;
          flex-direction: column !important;
          padding: 8px;
        }
        #container1, #container2 {
          flex: 1;
        }
      `);

  fetch(url)
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t303').innerHTML = "签约人数年龄分布情况"
        document.getElementById(div).innerHTML = ""

        const pieData = ((originData) => {
          const groupData = groupBy(originData, 'type');
          const result = [];
          each(groupData, (values, k) => {
            result.push({type: k, value: values.reduce((a, b) => a + b.value, 0)});
          });
          return result;
        })(data);


        let div1 = document.createElement('div')
        let div2 = document.createElement('div')
        document.getElementById(div).appendChild(div1)
        document.getElementById(div).appendChild(div2)
        div1.id = url + "div1"
        div1.style.position = 'absolute'
        div1.style.width = '34%'
        div1.style.height = '34%'
        div1.style.left = '1%'
        div1.style.top = '1%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '73%'
        div2.style.height = '73%'
        div2.style.left = '25%'
        div2.style.top = '25%'
        const pie = new Pie(url + "div1", {
          data: pieData,
          colorField: 'type',
          color: color,
          angleField: 'value',
          label: false,
          tooltip: false,
          state: {
            // 设置【active】激活状态样式 - 无描边
            active: {
              style: {
                lineWidth: 0,
              },
            },
          },
          interactions: [
            {
              type: 'element-highlight',
              cfg: {
                showEnable: [{trigger: 'element:mouseenter', action: 'cursor:pointer'}],
                end: [
                  {trigger: 'element:mouseleave', action: 'cursor:default'},
                  {trigger: 'element:mouseleave', action: 'element-highlight:reset'},
                ],
              },
            },
          ],
        });

        const column = new Column(url + "div2", {
          data,
          isStack: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color: color,
          // isGroup: 'true',
          legend: false,
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          slider: {
            start: 0,
            end: 0.6
          },
          yAxis: false,
          xAxis: false,
        });

        pie.render();
        column.render();

        let hoverData = {}
        column.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        column.on('plot:click', ev => {
          ev = ""
          age1 = hoverData['name'].replace("岁", '') + ev
          l1()
          div301()
          div302()
          div3021()
        });

        pie.on('element:mouseover', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            column.setState('selected', (datum) => datum.type === type);
            column.setState('selected', (datum) => datum.type !== type, false);
          }
        });
        pie.on('element:mouseleave', () => {
          // 取消 selected 选中状态
          column.setState('selected', () => true, false);
        });

        pie.on('element:click', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            pie.chart.changeData(pieData.filter((datum) => datum.type === type));
            column.chart.changeData(data.filter((datum) => datum.type === type));
          }
        });
        // 双击，还原数据
        pie.on('element:dblclick', () => {
          pie.chart.changeData(pieData);
          column.chart.changeData(data);
        });
      });
}

// eslint-disable-next-line no-unused-vars
function div304() {
  fetch(localhost + age2 + "/div304")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('t304').innerHTML = age2+"岁长期参保分布情况"
        document.getElementById('div304').innerHTML = ""
        const column = new Bar('div304', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          color: colors3,
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
          jg2 = hoverData['name'] + ev
          div305()
        });
      });
}


// eslint-disable-next-line no-unused-vars
function div3051() {
  fetch(localhost + age2 + "/div3051")
      .then((res) => res.json())
      .then((data) => {
        data = data.sort(cmp)
        document.getElementById('div3051').innerHTML = ""
        const column = new Bar('div3051', {
          data,
          yField: 'name',
          xField: 'value',
          seriesField: 'value',
          color: colors3,
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
      });
}

// eslint-disable-next-line no-unused-vars
function div305() {
  fetch(localhost + age2 + "/" + jg2 + '/div305')
      .then((res) => res.json())
      .then((data) => {
        let dataConfig = data;
        document.getElementById('t305').innerHTML = age2+"岁"+jg2+"参保情况"
        document.getElementById('div305').innerHTML = ""
        const container = document.getElementById('div305');
        const s2Options = {
          width: 270,
          height: 200,
        };
        const s2Palette = {
          basicColors: [
            '#000',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#fff',
            '#FFFFFF',
            '#eee',
            '#999',
            '#88',
            '#77',
            '#666',
            '#000',
          ],
          semanticColors: {
            red: '#FF4D4F',
            green: '#29A294',
          },
        };
        const s2 = new PivotSheet(container, dataConfig, s2Options);
        s2.setThemeCfg({palette: s2Palette});
        s2.render();
      });
}


// eslint-disable-next-line no-unused-vars
function div306(div = 'div306', url = localhost + 'div306', color = colors2) {
  insertCss(`
        #container {
          display: flex;
          flex-direction: column !important;
          padding: 8px;
        }
        #container1, #container2 {
          flex: 1;
        }
      `);

  fetch(url)
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t306').innerHTML = "长期参保分布情况"
        document.getElementById(div).innerHTML = ""

        const pieData = ((originData) => {
          const groupData = groupBy(originData, 'type');
          const result = [];
          each(groupData, (values, k) => {
            result.push({type: k, value: values.reduce((a, b) => a + b.value, 0)});
          });
          return result;
        })(data);


        let div1 = document.createElement('div')
        let div2 = document.createElement('div')
        document.getElementById(div).appendChild(div1)
        document.getElementById(div).appendChild(div2)
        div1.id = url + "div1"
        div1.style.position = 'absolute'
        div1.style.width = '80%'
        div1.style.height = '34%'
        div1.style.left = '1%'
        div1.style.top = '1%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '73%'
        div2.style.height = '73%'
        div2.style.left = '25%'
        div2.style.top = '25%'
        const pie = new Pie(url + "div1", {
          data: pieData,
          colorField: 'type',
          color: color,
          angleField: 'value',
          label: false,
          tooltip: false,
          state: {
            // 设置【active】激活状态样式 - 无描边
            active: {
              style: {
                lineWidth: 0,
              },
            },
          },
          interactions: [
            {
              type: 'element-highlight',
              cfg: {
                showEnable: [{trigger: 'element:mouseenter', action: 'cursor:pointer'}],
                end: [
                  {trigger: 'element:mouseleave', action: 'cursor:default'},
                  {trigger: 'element:mouseleave', action: 'element-highlight:reset'},
                ],
              },
            },
          ],
        });

        const column = new Column(url + "div2", {
          data,
          isStack: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color: color,
          // isGroup: 'true',
          legend: false,
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          slider: {},
          yAxis: false,
          xAxis: false,
        });

        pie.render();
        column.render();

        let hoverData = {}
        column.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data
        })
        column.on('plot:click', ev => {
          ev = ""
          age2 = hoverData['name'].replace("岁", '') + ev
          l2()
          div304()
          div3051()
          div305()
        });

        pie.on('element:mouseover', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            column.setState('selected', (datum) => datum.type === type);
            column.setState('selected', (datum) => datum.type !== type, false);
          }
        });
        pie.on('element:mouseleave', () => {
          // 取消 selected 选中状态
          column.setState('selected', () => true, false);
        });

        pie.on('element:click', (evt) => {
          const eventData = evt.data;
          if (eventData.data) {
            const type = eventData.data.type;
            pie.chart.changeData(pieData.filter((datum) => datum.type === type));
            column.chart.changeData(data.filter((datum) => datum.type === type));
          }
        });
        // 双击，还原数据
        pie.on('element:dblclick', () => {
          pie.chart.changeData(pieData);
          column.chart.changeData(data);
        });
      });
}


// eslint-disable-next-line no-unused-vars
function l1() {
  fetch(localhost + age1 + "/l21")
      .then(res => res.json())
      .then(data => {
        layer1.setData(data)
      });
}


// eslint-disable-next-line no-unused-vars
function l2() {
  fetch(localhost + age2 + "/l22")
      .then(res => res.json())
      .then(data => {
        layer2.setData(data)
      });
}


export default {
  name: "yantaiyanglaofusaip3",
  mounted() {

    scene = new Scene({
      id: 'map3',
      map: new GaodeMap({
        center: [121.495243, 37.213508],
        pitch: 45,
        zoom: 7,
        // style: 'amap://styles/30e7c78b2547888bba6ce4c27edf7431?isPublic=true',
        style: 'light'
      })
    });


    scene.on('loaded', () => {
      fetch(localhost + age1 + "/l21")
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
                .shape('cylinder')
                .size('value', function (level) {
                  return [2, 2, level / 2];
                })
                .active(true)
                .color('value', [
                  '#094D4A',
                  '#146968',
                  '#1D7F7E',
                  '#289899',
                  '#34B6B7',
                  '#4AC5AF',
                  '#5FD3A6',
                  '#7BE39E',
                  '#A1EDB8',
                  '#CEF8D6'
                ].reverse())
                .style({
                  opacity: 1.0
                });
            scene.addLayer(layer1);
            layer1.on('click', ev => {
              jg1 = ev.feature['name']
              div302()
              div3021()
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #070">${ev.feature['name']}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });
    scene.on('loaded', () => {
      fetch(localhost + age2 + '/l22')
          .then(res => res.json())
          .then(data => {
            layer2 = new PointLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('circle')
                .size(40)
                .color('value', [
                  '#34B6B7',
                  '#4AC5AF',
                  '#5FD3A6',
                  '#7BE39E',
                  '#A1EDB8',
                  '#CEF8D6'
                ].reverse())
                .active(true)
                .animate({})
                .style({
                  opacity: 1,
                  strokeWidth: 0
                });
            scene.addLayer(layer2);
            layer2.on('click', ev => {
              jg2 = ev.feature['name']
              div305()
              scene.setCenter([ev.lngLat.lng, ev.lngLat.lat])
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #070">${ev.feature['name']}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });


    div301()
    div302()
    div3021()
    div303()
    div304()
    div305()
    div3051()
    div306()


  },
  methods: {},
  data() {
    return {}
  }
}
</script>

<style scoped>
.content {
  position: absolute;
  width: 96%;
  height: 80%;
  left: 2%;
  top: 15%;
  text-align: center;
  font-size: 20%;
  color: #fff;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 100%;
  height: 6%;
  left: 0;
  top: 5%;
  text-align: center;
  font-size: 20%;
  color: #555;
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
  border-color: #ddd;
  border-width: 1px;
  color: #000;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>
