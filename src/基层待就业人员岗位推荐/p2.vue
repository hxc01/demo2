<template>
  <div id="page" style="position: absolute; width: 100%; height: 100%; left: 0; top: 0;">
    <div style="position: absolute; width: 99%; left: 0.5%; top: 22px; height: 96.5%;">
      <div class="divs" style="width: 19.5%; height: 58%; left: 0; top: 1%;">
        <div class="titles" id="t201"></div>
        <div class="charts" id="d201">
          <div style="position: absolute; width: 20%; left: 5%; height: 8%; top: 5%; font-size: 20px; color: #236">
            年龄:
          </div>
          <input id="i1" class="input" style="position: absolute; width: 60%; height: 8%; left: 30%; top: 5%" value="22">

          <div style="position: absolute; width: 20%; left: 5%; height: 8%; top: 20%; font-size: 20px; color: #236">
            性别:
          </div>
          <input id="i2" class="input" style="position: absolute; width: 60%; height: 8%; left: 30%; top: 20%" value="男">

          <div style="position: absolute; width: 20%; left: 5%; height: 8%; top: 35%; font-size: 20px; color: #236">
            专业:
          </div>
          <input id="i3" class="input" style="position: absolute; width: 60%; height: 8%; left: 30%; top: 35%" value="法律类">

          <div style="position: absolute; width: 20%; left: 5%; height: 8%; top: 50%; font-size: 20px; color: #236">
            学历:
          </div>
          <input id="i4" class="input" style="position: absolute; width: 60%; height: 8%; left: 30%; top: 50%" value="本科">

          <div style="position: absolute; width: 20%; left: 5%; height: 8%; top: 65%; font-size: 20px; color: #236">
            经验:
          </div>
          <input id="i5" class="input" style="position: absolute; width: 60%; height: 8%; left: 30%; top: 65%" value="1-3年">

          <button @click="this.d201" class="input"
                  style="position: absolute; width: 30%; height: 10%; left: 35%; top: 90%">提交
          </button>

        </div>
      </div>
      <div class="divs" style="width: 19.5%; height: 38%; left: 45%; top: 60%;">
        <div class="titles" id="t202"></div>
        <div class="charts" id="d202"></div>
      </div>
      <div class="divs" style="width: 44.5%; height: 58%; left: 20%; top: 1%;">
        <div class="titles" id="t203"></div>
        <div class="charts" id="d203"></div>
      </div>
      <div class="divs" style="width: 44.5%; height: 38%; left: 0; top: 60%;">
        <div class="titles" id="t204"></div>
        <div class="charts" id="d204"></div>
      </div>
      <div class="divs" style="width: 35%; height: 97%; left: 65%; top: 1%;">
        <div class="titles" id="t205"></div>
        <div class="charts" id="d205">
          <el-table
              ref="mytable"
              :data="table_data"
              style="width: 100%"
              @selection-change="handleSelectionChange"
              height="610"
          >
            <el-table-column
                align="center"
                v-for="(item,index,key) in table_columns"
                :item="item"
                :key="key"
                :index="index"
                :label="item.label"
            >
              <template slot-scope="scope">
                <span @click="consTable(scope.row)" v-if="  !scope.row.edit">{{ scope.row[item.prop] }}</span>
              </template>
            </el-table-column>
            <el-table-column fixed label="操作" align="center" width="50">
              <template slot-scope="scope">
                <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
                <el-button @click="div6(scope.row)" type="text" size="small">分析</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
      <div v-show="isTxt" class="divs" style="width: 44.5%; height: 97%; left: 20%; top: 1%;">
        <div @click="d206Back" class="divs"
             style="width: 10%; height: 23px; right: 1%; top: 1px; font-size: 18px; color: #236; text-align: center">返回
        </div>
        <div class="titles" id="t206"></div>
        <div class="charts" id="d206" style="font-size: 2px"></div>
      </div>
    </div>
  </div>
</template>


<script>
// eslint-disable-next-line no-unused-vars
import {Scene, PointLayer, Popup} from '@antv/l7';

// eslint-disable-next-line no-unused-vars
import {GaodeMap} from "@antv/l7-maps";

// eslint-disable-next-line no-unused-vars
import {Radar, Sankey} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
import * as echarts from 'echarts';
import {DrawControl} from "@antv/l7-draw";

// eslint-disable-next-line no-unused-vars
let div6JsonData = []


// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:3050/', lng1, lat1, lng2, lat2

// eslint-disable-next-line no-unused-vars
let scene, pointLayer, drawControl, layer1, colors = [
  '#3377cc',
  '#4488cc',
  '#5599dd',
  '#66aadd',
  '#77bbee',
  '#88ccee',
].reverse();

// eslint-disable-next-line no-unused-vars
let gwlx = '店长', xl = '大专', cs = '上海', gsmc = '西西弗书店', gzjy = '1-3年'

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
function selectTxt(div) {
  return document.getElementById(div).options[document.getElementById(div).options.selectedIndex].text
}


// eslint-disable-next-line no-unused-vars
function d202() {

}

// eslint-disable-next-line no-unused-vars
function d203() {
  fetch(localhost + gwlx + "/" + xl + "/d203")
      .then(res => res.json())
      .then(data => {
        pointLayer.setData(data)
        let jsonData = []
        drawControl.on('draw.create', (e) => {
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          jsonData = []
          for (let i in data) {
            if (Math.min(lng1, lng2) <= data[i]['jd'] && data[i]['jd'] <= Math.max(lng1, lng2)) {
              if (Math.min(lat1, lat2) <= data[i]['wd'] && data[i]['wd'] <= Math.max(lat1, lat2)) {
                jsonData.push(data[i])
              }
            }
          }
          layer1 = new PointLayer({})
              .source(jsonData, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('技能高频词', 'text')
              .size('value', [8, 15])
              .color('value', ['#013', '#124', '#236'])
              .style({
                textAnchor: 'center', // 文本相对锚点的位置 center|left|right|top|bottom|top-left
                textOffset: [0, 0], // 文本相对锚点的偏移量 [水平, 垂直]
                spacing: 2, // 字符间距
                padding: [0.2, 0.2], // 文本包围盒 padding [水平，垂直]，影响碰撞检测结果，避免相邻文本靠的太近
                stroke: '#000', // 描边颜色
                strokeWidth: 0, // 描边宽度
                strokeOpacity: 0.7
              });
          scene.addLayer(layer1);
        });
        drawControl.on('draw.update', (e) => {
          scene.removeLayer(layer1)
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          lng1 = e.feature.properties.startPoint.lng
          lat1 = e.feature.properties.startPoint.lat
          lng2 = e.feature.properties.endPoint.lng
          lat2 = e.feature.properties.endPoint.lat
          jsonData = []
          for (let i in data) {
            if (Math.min(lng1, lng2) <= data[i]['jd'] && data[i]['jd'] <= Math.max(lng1, lng2)) {
              if (Math.min(lat1, lat2) <= data[i]['wd'] && data[i]['wd'] <= Math.max(lat1, lat2)) {
                jsonData.push(data[i])
              }
            }
          }
          layer1 = new PointLayer({})
              .source(jsonData, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('技能高频词', 'text')
              .size('value', [8, 15])
              .color('value', ['#013', '#124', '#236'])
              .style({
                textAnchor: 'center', // 文本相对锚点的位置 center|left|right|top|bottom|top-left
                textOffset: [0, 0], // 文本相对锚点的偏移量 [水平, 垂直]
                spacing: 2, // 字符间距
                padding: [0.2, 0.2], // 文本包围盒 padding [水平，垂直]，影响碰撞检测结果，避免相邻文本靠的太近
                stroke: '#000', // 描边颜色
                strokeWidth: 0, // 描边宽度
                strokeOpacity: 0.7
              });
          scene.addLayer(layer1);
        });
        drawControl.on('draw.delete', function () {
          scene.removeLayer(layer1)
        });
      });
}

// eslint-disable-next-line no-unused-vars
function d204() {
  fetch(localhost + gwlx + "/" + xl + "/d204")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t204').innerHTML = gwlx + xl + "招聘热度分布图"
        document.getElementById('d204').innerHTML = ""
        const sankey = new Sankey('d204', {
          data,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          color: colors,
          nodeWidthRatio: 0.008,
          nodePaddingRatio: 0.03,
        });

        sankey.render();
      });


}

export default {
  name: "jicengdaijiuye",
  data() {
    return {
      isTxt: 0,
      table_columns: [],
      table_data: [],
      search: '',
      showEdit: [], //显示编辑框
      showBtn: [],
      showBtnOrdinary: true,
      new_date_json: {}, //数据结构
      multipleSelection: [], //复选框，数据
      is_edit: true, //是否可编辑
      is_delete: true, //是否可删除
      selection: true, //是否需要复选框
      radio: false, //单选变色
      space_color: true, //隔行变色
    }
  },
  mounted() {
    scene = new Scene({
      id: 'd203',
      map: new GaodeMap({
        pitch: 0,
        style: 'amap://styles/45acf9c63991132cf759a67613e1f2d5?isPublic=true',
        center: [121.499035, 31.215548],
        zoom: 9,
      })
    });

    drawControl = new DrawControl(scene, {
      position: 'topright',
      layout: 'horizontal', // horizontal vertical
      controls: {
        point: false,
        polygon: false,
        line: false,
        circle: false,
        rect: true,
        delete: true
      }
    });
    scene.addControl(drawControl);

    scene.on('loaded', () => {
      fetch(localhost + gwlx + "/" + xl + "/d203")
          .then(res => res.json())
          .then(data => {
            pointLayer = new PointLayer({})
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
            scene.addLayer(pointLayer);
            pointLayer.on('click', ev => {
              gsmc = ev.feature['公司名称']
              div6JsonData = []
              this.initEditAttribute()
              const popup = new Popup({
                offsets: [0, 0],
                closeButton: false
              })
                  .setLnglat(ev.lngLat)
                  .setHTML(
                      `<span style="color: #777">${ev.feature['公司名称']}</span>`
                  );
              scene.addPopup(popup);
            })
          });
    });


    d202()

    d204()
    this.initEditAttribute();


  },

  methods: {
    d201() {
      let nl = document.getElementById('i1').value
      let xb = document.getElementById('i2').value
      let zy = document.getElementById('i3').value
      xl = document.getElementById('i4').value
      gzjy = document.getElementById('i5').value
      fetch(localhost + zy + "/" + xb + "/" + nl + "/d201")
          .then((res) => res.json())
          .then((data) => {
            gwlx = data['name']
            d203()
            d204()
          })

    },
    handleClick(row) {
      this.isTxt = 1
      document.getElementById('t206').innerHTML = row['岗位名称']
      document.getElementById('d206').innerHTML = row['岗位描述'] + '。 具备的技能：' + row['技能需求']
    },
    consTable(data) {
      console.log(data['公司名称'])
    },
    d206Back() {
      this.isTxt = 0
    },
    //隔行变色
    tableRowClassName() {
      //选取DOM节点
      var trs = this.$refs.mytable.$el
          .getElementsByTagName("tbody")[0]
          .getElementsByTagName("tr");
      for (var i in trs) {
        if (i % 2 == 0) {
          //当隔行变色未true时改变颜色
          if (this.space_color) {
            trs[i].style.backgroundColor = "#f0f9eb";
          } else {
            trs[i].style.backgroundColor = "";
          }
        }
      }
    },

    //多选框
    handleSelectionChange(val) {
      this.multipleSelection = val;
      // console.log("selection:", this.multipleSelection);
    },
    //编辑
    handleEdit(index, row) {
      // console.log(index, row);
      row.edit = true;
    },
    //删除
    handleDelete(index) {
      // console.log(index, row);

      this.table_data.splice(index, 1);

      this.$message({
        message: "删除成功！",
        type: "success"
      });
    },
    //保存
    handleSave(index, row) {
      // console.log(index, row);
      row.edit = false;

      delete this.table_data[index].add;

      this.$message({
        message: "保存成功！",
        type: "success"
      });
    },
    handleAdd() {
      var addDataJson = {};
      for (var key in this.new_date_json) {
        if (key === "edit") {
          delete addDataJson[key];
        } else if (key === "add") {
          delete addDataJson[key];
        } else {
          addDataJson[key] = "";
        }
      }
      addDataJson.edit = true;
      addDataJson.add = true;
      this.table_data.push(addDataJson);
    },
    //初始化编辑属性
    initEditAttribute() {
      fetch(localhost + gsmc + "/d205")
          .then((res) => res.json())
          .then((data) => {
            this.table_columns = []
            this.table_data = []
            this.table_columns = data['columns']
            let dataArray = data['data']
            if (dataArray.length > 0) {
              //添加编辑事件
              for (var index in dataArray) {
                dataArray[index]["edit"] = false;
                this.table_data.push(dataArray[index]);
              }
              if (Object.keys(this.new_date_json).length === 0) {
                //新增时，初始化数据结构
                this.initAddDataJson(dataArray[0]);
              }
            }
          })
    },
    initAddDataJson(dataArray) {
      //新增时，初始化数据结构
      var dataJson = dataArray;
      var newDateJson = {};
      for (var key in dataJson) {
        if (key === "edit") {
          newDateJson[key] = "true";
        } else {
          newDateJson[key] = "";
        }
      }
      newDateJson["add"] = true;
      this.new_date_json = newDateJson;
    },
    div6: function (ev) {
      let Id = ev['Id']
      fetch(localhost + Id + "/d206")
          .then((res) => res.json())
          .then((data) => {
            for (let i = 0; i <= 1; i += 1) {
              div6JsonData.push(
                  {"item": "薪资", "user": data[i]['岗位名称'] + Id, "score": data[i]['平均薪资'] / 1000},
                  {"item": "工作经验", "user": data[i]['岗位名称'] + Id, "score": data[i]['工作经验等级']},
                  {"item": "学历", "user": data[i]['岗位名称'] + Id, "score": data[i]['学历等级']},
                  {"item": "招聘人数", "user": data[i]['岗位名称'] + Id, "score": data[i]['招聘人数'] / 10},
                  {"item": "工作类型", "user": data[i]['岗位名称'] + Id, "score": data[i]['工作类型等级']},
              )
              document.getElementById('t202').innerHTML = data[i]['公司名称'] + "岗位对比图"
              document.getElementById('d202').innerHTML = ""
              const radarPlot = new Radar('d202', {
                data: div6JsonData,
                xField: 'item',
                yField: 'score',
                seriesField: 'user',
                color: colors,
                meta: {
                  score: {},
                },
                xAxis: {
                  line: null,
                  tickLine: null,
                  grid: {
                    line: {
                      style: {
                        lineDash: null,
                      },
                    },
                  },
                },
                yAxis: {
                  line: null,
                  tickLine: null,
                  grid: {
                    line: {
                      type: 'line',
                      style: {
                        lineDash: null,
                      },
                    },
                    alternateColor: 'rgba(0, 0, 0, 0.04)',
                  },
                },
                // 开启辅助点
                point: {
                  size: 2,
                },
              });
              radarPlot.render();
            }
          })
    },
  }

}
</script>

<style scoped>
#page {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  background-color: #bcc;
  color: #000000;
}

.charts {
  position: absolute;
  width: 96%;
  height: 87%;
  left: 2%;
  top: 30px;
  text-align: center;
  font-size: 2px;
  color: #000;
  font-weight: bold;
}

.titles {
  position: absolute;
  width: 100%;
  height: 28px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 12px;
  font-family: 宋体;
  color: #fff;
  background-color: #446699;
  font-weight: bold;


  border-top-right-radius: 15px;
  border-top-left-radius: 15px;

}

.divs {
  position: absolute;
  text-align: center;
  background-color: #eff;
  /*border-radius: 0;*/
  /*border-style: outset;*/
  /*border-width: 2px;*/
  /*border-color: #f9f9f9;*/
  /*box-shadow: #999 0 0 1px 1px;*/
  color: #000;
  opacity: unset;
  z-index: 100;

  border-radius: 15px;
}

.select {
  position: absolute;
  width: 4.5%;
  height: 2.7%;
  background-color: #fff;
  border-color: #eeeeee;
  z-index: 9999;
  font-size: 5px;
  border-radius: 10px;
}

.input {
  position: absolute;
  width: 4.5%;
  height: 2.7%;
  font-size: 20px;
  text-align: center;
  background-color: #fff;
  border-color: #eeeeee;
  z-index: 9999;
  border-radius: 10px;
}
</style>