<template>
  <div style="position: absolute;width: 99%;height: 100%;left: 0;top: 0">

    <div style="position: absolute;width: 40%;height: 100%;left: 0;top: 0"></div>


    <div
        style="position: absolute; width: 33%; height: 19%; left: 0; top: 60%"
        class="divs"
    >
      <div id="div406" class="content"></div>
      <div id="t406" class="title">七次人口普查数据</div>
    </div>
    <div
        style="position: absolute; width: 33%; height: 19%; left: 33.5%; top: 60%"
        class="divs"
    >
      <div id="div407" class="content"></div>
      <div id="t407" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 33%; height: 19%; left: 67%; top: 60%"
        class="divs"
    >
      <div id="div408" class="content"></div>
      <div id="t408" class="title"></div>
    </div>


    <div
        style="position: absolute; width: 24.5%; height: 19%; left: 0; top: 80%"
        class="divs"
    >
      <div id="div409" class="content"></div>
      <div id="t409" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 24.5%; height: 19%; left: 25%; top: 80%"
        class="divs"
    >
      <div id="div410" class="content"></div>
      <div id="t410" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 24.5%; height: 19%; left: 50%; top: 80%"
        class="divs"
    >
      <div id="div411" class="content"></div>
      <div id="t411" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 24.5%; height: 19%; left: 75%; top: 80%"
        class="divs"
    >
      <div id="div412" class="content"></div>
      <div id="t412" class="title"></div>
    </div>


    <div
        style="position: absolute; width: 49.5%; height: 29%; left: 24.5%; top: 30%"
        class="divs"
    >
      <div id="div413" class="content"></div>
      <div id="t413" class="title"></div>
    </div>


    <div
        class="divs"
        style="position: absolute; width: 24%; height: 29%; left: 0; top: 30%"
    >
      <div id="div401" class="content"></div>
      <div id="t401" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 24.7%; height: 29%; right: 0.3%; top: 30%"
        class="divs"
    >
      <div id="div402" class="content"></div>
      <div id="t402" class="title"></div>
    </div>
    <select @change="f402" id="s402" class="selects" style="right: 2%; top: 36%"></select>


    <div
        style="position: absolute; width: 33%; height: 29%; left: 0; top: 0"
        class="divs"
    >
      <div id="div403" class="content"></div>
      <div id="t403" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 33%; height: 29%; left: 33.5%; top: 0"
        class="divs"
    >
      <div id="div404" class="content"></div>
      <div id="t404" class="title"></div>
    </div>
    <div
        style="position: absolute; width: 33%; height: 29%; left: 67%; top: 0"
        class="divs"
    >
      <div id="div405" class="content"></div>
      <div id="t405" class="title"></div>
    </div>


    <select id="s406" @change="f406" class="selects" style="left: 27%; top: 65%"></select>
    <select id="s407" @change="f407" class="selects" style="left: 61%; top: 65%"></select>
    <select id="s408" @change="f408" class="selects" style="left: 95%; top: 65%"></select>

    <select id="s409" @change="f409" class="selects" style="left: 20.5%; top: 84%"></select>
    <select id="s4101" @change="f410" class="selects" style="left: 45%; top: 84%"></select>
    <select id="s4102" @change="f410" class="selects" style="left: 45%; top: 88%"></select>
    <select id="s411" @change="f411" class="selects" style="left: 70.5%; top: 84%"></select>
    <select id="s412" @change="f412" class="selects" style="left: 95.5%; top: 84%"></select>


  </div>
</template>

<script>


import insertCss from "insert-css";
import {each, groupBy} from "@antv/util";
import {Column, Pie, Line} from "@antv/g2plot";

let localhost = 'http://127.0.0.1:5000/'


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
let div402Types = [
  '按年龄分类',
  '按学历分类',
  '按性别分类',
  '按户数分类',
  '按抚养比分类',
  '按民族分类',
], div402Type = div402Types[0]

// eslint-disable-next-line no-unused-vars
let div406Types = [
  '总人口', '男', '女', '0-14岁', '15-64岁', '65岁及以上', '家庭户', '平均家庭户规模', '少儿抚养比', '老年抚养比'
], div406Type = div406Types[0]


// eslint-disable-next-line no-unused-vars
let div407Types = [
  '常住人口', '城镇人口', '市区人口', '城镇化率', '户籍人口', '市区人口'
], div407Type = div407Types[0]

// eslint-disable-next-line no-unused-vars
let div408Types = ['一、粮食消费量', '（一）谷物消费量', '1.小麦', '2.稻谷', '3.玉米', '4.其他谷物', '（二）薯类消费量', '1.红薯', '2.马铃薯', '3.其他薯类', '（三）豆类消费量', '1.大豆', '2.其他豆类', '二、油脂类消费量', '（一）植物油', '（二）动物油', '三、蔬菜及菜制品消费量', '（一）鲜菜', '（二）干菜及菜制品', '（三）鲜菌', '（四）干菌及菌制品', '四、肉类', '（一）猪肉', '（二）牛肉', '（三）羊肉', '（四）其他肉类及制品', '五、禽类', '（一）鸡', '（二）鸭', '（三）鹅', '（四）其他禽类及制品', '六、水产品', '（一）鱼类', '（二）虾贝蟹类', '（三）藻类', '（四）其他', '七、蛋类及蛋制品', '（一）鲜蛋', '（二）蛋制品', '八、奶和奶制品', '（一）鲜奶', '（二）酸奶', '（三）奶粉', '（四）其他奶制品', '九、干鲜瓜果类', '（一）鲜瓜果', '（二）瓜果制品', '（三）坚果类', '十、糖果糕点类', '（一）食糖', '（二）糖果', '（三）糕点', '（四）其他糖果糕点', '十一、饮料', '（一）茶叶', '十二、烟叶消费量', '十三、酒', '（一）白酒', '（二）啤酒', '（三）果酒', '一.粮食消费量', '(一)谷物消费量', '4.高粱', '5.谷子', '6.青稞', '7.其他谷物', '(二)薯类消费量', '(三)豆类消费量', '二.油脂类消费量', '1.植物油', '2.动物油', '三.烟叶消费量', '四.豆制品', '五.蔬菜及菜制品消费量', '1.鲜菜', '2.干菜', '3.菜制品', '4.鲜菌', '5.干菌', '6.菌制品', '六.瓜类', '1.西瓜', '2.其他瓜果', '七.水果类', '八.消费茶叶', '九.坚果消费量', '十.肉禽及其制品', '1.猪肉', '2.牛肉', '3.羊肉', '4.家禽', '5.其他肉禽及制品', '十一.蛋类及蛋制品', '十二.奶和奶制品', '十三.水产品', '1.鱼类', '2.虾、贝、蟹类', '3.藻类', '4.其他', '十四.食糖', '十五、酒', '#白酒', '啤酒', '果酒', '粮食消费量', '＃小麦', '玉米', '大豆', '植物油', '豆制品', '蔬菜', '猪肉', '牛羊肉', '家禽', '其他肉禽及制品', '蛋类及蛋制品', '奶和奶制品', '水产品', '食糖', '白酒', '瓜类', '水果类']
// eslint-disable-next-line no-unused-vars
let div408Type = div408Types[0]
// eslint-disable-next-line no-unused-vars
let div409Types = ['卫生机构数(个)', '医院、卫生院', '卫生机构床位数(张)', '医院、卫生院', '卫生技术人员数(人)', '医生']
// eslint-disable-next-line no-unused-vars
let div409Type = div409Types[0]
// eslint-disable-next-line no-unused-vars
let div410Types1 = ['全市', '市区', '芝罘区', '福山区', '牟平区', '莱山区', '蓬莱区', '龙口市', '莱阳市', '莱州市', '招远市', '栖霞市', '海阳市', '开发区', '高新区', '昆嵛区', '蓬莱市', '长岛县']
// eslint-disable-next-line no-unused-vars
let div410Type1 = div410Types1[0]
// eslint-disable-next-line no-unused-vars
let div410Types2 = ['出生人数', '出生率', '死亡人数', '死亡率', '增长人数', '增长率', '年平均人口']
// eslint-disable-next-line no-unused-vars
let div410Type2 = div410Types2[0]
// eslint-disable-next-line no-unused-vars
let div411Types = ['芝罘区', '福山区', '牟平区', '莱山区', '蓬莱区', '开发区', '高新区', '长岛综合试验区', '昆嵛山保护区', '龙口市', '莱阳市', '莱州市', '招远市', '栖霞市', '海阳市', '昆嵛区', '蓬莱市', '长岛县', '市区', '市直']
// eslint-disable-next-line no-unused-vars
let div411Type = div411Types[0]
// eslint-disable-next-line no-unused-vars
let div412Types = ['合计', '市区', '芝罘区', '福山区', '牟平区', '莱山区', '蓬莱区', '开发区', '高新区', '长岛综合试验区', '龙口市', '莱阳市', '莱州市', '招远市', '栖霞市', '海阳市']
// eslint-disable-next-line no-unused-vars
let div412Type = div412Types[0]


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
function div401(div = 'div401', url = localhost + 'div401', color = colors2) {
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
        document.getElementById('t401').innerHTML = "主要年份人口情况"
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
        div1.style.height = '35%'
        div1.style.left = '10%'
        div1.style.top = '2.5%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '80%'
        div2.style.height = '55%'
        div2.style.left = '10%'
        div2.style.top = '42.5%'
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
          // slider: {},
          yAxis: false,
          xAxis: {
            grid: null
          },
        });

        pie.render();
        column.render();

        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        // });

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
function div402(div = 'div402', url = localhost + div402Type + '/div402', color = colors2) {
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
        document.getElementById('t402').innerHTML = "六次普查" + div402Type + "数据"
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
        div1.style.height = '35%'
        div1.style.left = '10%'
        div1.style.top = '2.5%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '80%'
        div2.style.height = '55%'
        div2.style.left = '10%'
        div2.style.top = '42.5%'
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
          // slider: {},
          yAxis: false,
          xAxis: {
            grid: null
          },
        });

        pie.render();
        column.render();

        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        // });

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
function div403(div = 'div403', url = localhost + '/div403', color = colors2) {
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
        document.getElementById('t403').innerHTML = "出生、死亡、增长率"
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
        div1.style.height = '35%'
        div1.style.left = '10%'
        div1.style.top = '2.5%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '80%'
        div2.style.height = '55%'
        div2.style.left = '10%'
        div2.style.top = '42.5%'
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
          // slider: {},
          yAxis: false,
          xAxis: {
            grid: null
          },
        });

        pie.render();
        column.render();

        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        // });

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
function div404(div = 'div404', url = localhost + '/div404', color = colors2) {
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
        document.getElementById('t404').innerHTML = "2019年末户数、人口数"
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
        div1.style.height = '35%'
        div1.style.left = '10%'
        div1.style.top = '2.5%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '80%'
        div2.style.height = '55%'
        div2.style.left = '10%'
        div2.style.top = '42.5%'
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
          // isStack: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color: color,
          isGroup: true,
          legend: false,
          slider: {},
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          // slider: {},
          yAxis: false,
          xAxis: {
            grid: null
          },
        });

        pie.render();
        column.render();

        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        // });

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
function div405(div = 'div405', url = localhost + '/div405', color = colors2) {
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
        document.getElementById('t405').innerHTML = "2018、2019年人口基本情况"
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
        div1.style.height = '35%'
        div1.style.left = '10%'
        div1.style.top = '2.5%'
        div2.id = url + "div2"
        div2.style.position = 'absolute'
        div2.style.width = '80%'
        div2.style.height = '55%'
        div2.style.left = '10%'
        div2.style.top = '42.5%'
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
          // isStack: true,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color: color,
          isGroup: true,
          legend: false,
          slider: {},
          columnStyle: {
            radius: [20, 20, 20, 20],
            strokeOpacity: 0.7,
            shadowColor: 'black',
            shadowOffsetX: 1,
            shadowOffsetY: 1,
            cursor: 'pointer'
          },
          // slider: {},
          yAxis: false,
          xAxis: {
            grid: null
          },
        });

        pie.render();
        column.render();

        // let hoverData = {}
        // column.on('tooltip:change', ev => {
        //   hoverData = ev.data.items[0].data
        // })
        // column.on('plot:click', ev => {
        //   ev = ""
        // });

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
function div406() {
  fetch(localhost + div406Type + "/div406")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div406').innerHTML = ''
        document.getElementById('t406').innerHTML = '七次人口普查' + div406Type + "数据"
        const line = new Line('div406', {
          data,
          xField: 'name',
          yField: div406Type,
          color: colors3[0],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });

        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div407() {
  fetch(localhost + div407Type + "/div407")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div407').innerHTML = ''
        document.getElementById('t407').innerHTML = '主要年份人口情况' + div407Type + "数据"
        const line = new Line('div407', {
          data,
          xField: 'name',
          yField: div407Type,
          color: colors3[4],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });

        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div408() {
  fetch(localhost + div408Type + "/div408")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div408').innerHTML = ''
        console.log(div408Type)
        document.getElementById('t408').innerHTML = div408Type + "人均消费量"
        const line = new Line('div408', {
          data,
          xField: 'name',
          yField: '食品消耗量',
          color: colors3[0],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });

        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div409() {
  fetch(localhost + div409Type + "/div409")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div409').innerHTML = ''
        document.getElementById('t409').innerHTML = div409Type + "卫生机构情况"
        const line = new Line('div409', {
          data,
          xField: 'name',
          yField: div409Type,
          color: colors3[4],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });
        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div410() {
  fetch(localhost + div410Type1 + "/" + div410Type2 + "/div410")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div410').innerHTML = ''
        document.getElementById('t410').innerHTML = div410Type1 + div410Type2
        const line = new Line('div410', {
          data,
          xField: 'name',
          yField: div410Type2,
          color: colors3[0],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });
        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div411() {
  fetch(localhost + div411Type + "/div411")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div411').innerHTML = ''
        document.getElementById('t411').innerHTML = div411Type + "生产总值"
        const line = new Line('div411', {
          data,
          xField: 'name',
          yField: "生产总值",
          color: colors3[4],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });
        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div412() {
  fetch(localhost + div412Type + "/div412")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div412').innerHTML = ''
        document.getElementById('t412').innerHTML = div412Type + "建筑业生产总值"
        const line = new Line('div412', {
          data,
          xField: 'name',
          yField: "生产总值",
          color: colors3[0],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });
        line.render();
      });
}

// eslint-disable-next-line no-unused-vars
function div413() {
  fetch(localhost + "/div413")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('div413').innerHTML = ''
        document.getElementById('t413').innerHTML = '65岁以上老年人群预测数据'
        const line = new Line('div413', {
          data,
          xField: 'name',
          yField: 'value',
          color: colors3[4],
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
        });

        line.render();
      });
}

export default {
  name: "yantaiyanglaofusaip3",
  mounted() {


    addListOption('s402', div402Types)
    addListOption('s406', div406Types)
    addListOption('s407', div407Types)
    addListOption('s408', div408Types)
    addListOption('s409', div409Types)
    addListOption('s4101', div410Types1)
    addListOption('s4102', div410Types2)
    addListOption('s411', div411Types)
    addListOption('s412', div412Types)


    div401()
    div402()
    div403()
    div404()
    div405()
    div406()
    div407()
    div408()
    div409()
    div410()
    div411()
    div412()
    div413()


  },
  methods: {
    f402: function () {
      div402Type = selectTxt('s402')
      div402()
    },
    f406: function () {
      div406Type = selectTxt('s406')
      div406()
    },
    f407: function () {
      div407Type = selectTxt('s407')
      div407()
    },
    f408: function () {
      div408Type = selectTxt('s408')
      div408()
    },
    f409: function () {
      div409Type = selectTxt('s409')
      div409()
    },
    f410: function () {
      div410Type1 = selectTxt('s4101')
      div410Type2 = selectTxt('s4102')
      div410()
    },
    f411: function () {
      div411Type = selectTxt('s411')
      div411()
    },
    f412: function () {
      div412Type = selectTxt('s412')
      div412()
    },
  },
  data() {
    return {}
  }
}
</script>

<style scoped>
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
  color: #fff;
  font-weight: bold;
  background-color: #777;
}

.divs {
  position: absolute;
  text-align: center;
  background-color: #fff;
  border-width: 3px;
  border-style: outset;
  border-color: #ddd;
  opacity: 0.99;
  /*border-radius: 5px;*/
  z-index: 3000;
}

.selects {
  position: absolute;
  width: 4%;
  height: 3%;
  background-color: #fff;
  border-color: #eee;
  border-width: 1px;
  color: #000;
  border-radius: 5px;
  z-index: 9990;
  font-size: 9px;
  text-align: center;
}
</style>
