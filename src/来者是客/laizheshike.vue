<template>
  <dv-border-box-11
      style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #e5f3f8"
      title="密接轨迹可视化分析系统"
      :color="['#51688a', '#40555A']">
    <div style="position: absolute; width: 97%; height: 88%; left: 1.5%; top: 10%">
      <div id="map" class="divs" style="width: 49.5%; height: 59%; left: 25%; top: 0"></div>
      <div class="divs" style="width: 24%; height: 59%; left: 0; top: 0">
        <div class="title" id="t101">密接人员信息</div>
        <div class="content" id="d101">
          <el-table
              ref="mytable"
              :data="table_data"
              style="width: 100%; top: 10%"
              @selection-change="handleSelectionChange"
              height="300"
          >
            <el-table-column v-if="radio" type="index" width="50"></el-table-column>
            <el-table-column v-if="selection" type="selection" width="55"></el-table-column>
            <el-table-column
                align="center"
                v-for="(item,index,key) in table_columns"
                :item="item"
                :key="key"
                :index="index"
                :label="item.label"
            >
              <template slot-scope="scope">
                <el-input
                    v-if=" scope.row.edit"
                    size="small"
                    v-model="scope.row[item.prop]"
                    :placeholder="'请输入'+item.label"
                ></el-input>
                <span v-if="  !scope.row.edit">{{ scope.row[item.prop] }}</span>
              </template>
            </el-table-column>
            <el-table-column fixed label="操作" align="center" width="70">
              <template slot-scope="scope">
                <!-- 编辑 -->
                <el-button
                    size="mini"
                    v-if="!scope.row.edit"
                    @click="handleSelect(scope.row)"
                    type="info"
                >查
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <el-button
            style="position: absolute; top: 25px; left: 0"
            size="mini"
            @click="initEditAttribute"
            type=""
        >更新
        </el-button>
      </div>
      <div class="divs" style="width: 33%; height: 39%; left: 0; top: 60%">
        <div class="title" id="t102">某区域疫情变化情况</div>
        <div class="content" id="d102"></div>
      </div>
      <div class="divs" style="width: 33%; height: 39%; left: 33.5%; top: 60%">
        <div class="title" id="t103">全省各区域疫情热力图</div>
        <div class="content" id="d103"></div>
      </div>
      <div class="divs" style="width: 32.5%; height: 39%; left: 67%; top: 60%">
        <div class="title" id="t104">几市对比分析</div>
        <div class="content" id="d104"></div>
      </div>
      <div class="divs" style="width: 24%; height: 59%; right: 0; top: 0">
        <div class="title" id="t105">疫情舆论词云</div>
        <div class="content" id="d105"></div>
      </div>
    </div>
  </dv-border-box-11>

</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, LineLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar, Liquid, Pie, RingProgress, Rose, Scatter, WordCloud, Heatmap, Mix} from '@antv/g2plot';
// eslint-disable-next-line no-unused-vars
import laizheshikeTable from "./laizheshikeTable";
// eslint-disable-next-line no-unused-vars
import {DrawControl} from "@antv/l7-draw";

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:5000/"

// eslint-disable-next-line no-unused-vars
let scene, l1, l2, l3, l4, ids = 1, lng1, lat1, lng2, lat2

// eslint-disable-next-line no-unused-vars
let city = "青岛市", y = 2022, m = 3, day = 31, date = '2022-03-31'

// eslint-disable-next-line no-unused-vars
let color = [
  '#263b40',
  '#50656a',
  '#818e94',
  '#afaeb6',
  '#c1b3bd',
  '#d3d5d8'
]

// eslint-disable-next-line no-unused-vars
let _color = [
  '#263b40',
  '#50656a',
  '#818e94',
  '#afaeb6',
  '#c1b3bd',
  '#d3d5d8'
].reverse()

// eslint-disable-next-line no-unused-vars
function d101() {

}

// eslint-disable-next-line no-unused-vars
function d102() {
  fetch(localhost + city + "/d102")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t102').innerHTML = city + "疫情变化"
        document.getElementById('d102').innerHTML = ""
        const area = new Area('d102', {
          data,
          xField: 'date',
          yField: 'value',
          seriesField: 'type',
          color,
          areaStyle: {
            fillOpacity: 0.7,
          },
          isPercent: true,
          yAxis: {
            grid: null
          },
        });
        area.render();
        let jsonData = {}
        area.on('tooltip:change', (ev) => {
          jsonData = ev.data.items[0]
        })
        area.on('plot:click', () => {
          y = jsonData['title'].split("-")[0]
          m = jsonData['title'].split("-")[1]
          d103()
          d104()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d103() {
  fetch(localhost + y + "/" + m + "/d103")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t103').innerHTML = y + "年" + m + "月现存确诊对比"
        document.getElementById('d103').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d103'), {
          data,
          xField: 'city',
          yField: 'day',
          colorField: 'value',
          sizeField: 'size',
          shape: 'square',
          color: _color,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          label: false,
        });
        heatmapPlot.render();
        let jsonData = {}
        heatmapPlot.on('tooltip:change', (ev) => {
          jsonData = ev.data.items[0].data
        })
        heatmapPlot.on('plot:click', () => {
          city = jsonData['city']
          date = y + "-" + m + "-" + jsonData['day'].replace("日", "")
          dl1()
          dl2()
          dl3()
          d102()
          d105()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function d104() {
  fetch(localhost + y + "/d104")
      .then((data) => data.json())
      .then((data) => {
        document.getElementById('t104').innerHTML = y + "年" + "疫情趋势对比"
        document.getElementById('d104').innerHTML = ""
        const plot = new Mix('d104', {
          // 关闭 chart 上的 tooltip，子 view 开启 tooltip
          tooltip: false,
          plots: [
            {
              type: 'bar',
              region: {start: {x: 0, y: 0}, end: {x: 0.45, y: 0.45}},
              options: {
                data: data.bar,
                xField: 'value',
                yField: 'city',
                seriesField: 'type',
                isStack: true,
                tooltip: {
                  shared: true,
                  showCrosshairs: false,
                  showMarkers: false,
                },
                yAxis: {
                  grid: null
                },
                xAxis: {
                  grid: null
                },
                color,
                label: {},
                interactions: [{type: 'active-region'}],
              },
            },
            {
              type: 'pie',
              region: {start: {x: 0.5, y: 0}, end: {x: 1, y: 0.45}},
              options: {
                data: data.pie,
                angleField: 'value',
                colorField: 'city',
                tooltip: {
                  showMarkers: false,
                },
                color,
                radius: 0.85,
                label: {type: 'inner', formatter: '{name}', offset: '-15%'},
                interactions: [
                  {type: 'element-active'},
                  {
                    type: 'association-tooltip',
                    cfg: {
                      start: [
                        {
                          trigger: 'element:mousemove',
                          action: 'association:showTooltip',
                          arg: {dim: 'x', linkField: 'area'},
                        },
                      ],
                    },
                  },
                  {
                    type: 'association-highlight',
                    cfg: {
                      start: [
                        {
                          trigger: 'element:mousemove',
                          action: 'association:highlight',
                          arg: {linkField: 'area'},
                        },
                      ],
                    },
                  },
                ],
              },
            },
            {
              type: 'area',
              region: {start: {x: 0, y: 0.5}, end: {x: 1, y: 0.95}},
              options: {
                data: data.line,
                xField: 'date',
                yField: 'value',
                seriesField: 'city',
                line: {},
                point: {style: {r: 2.5}},
                meta: {
                  time: {range: [0, 1]},
                },
                yAxis: {
                  grid: null
                },
                xAxis: {
                  grid: null
                },
                color,
                smooth: true,
                tooltip: {
                  showCrosshairs: true,
                  shared: true,
                },
              },
            },
          ],
        });

        plot.render();
      });

}

// eslint-disable-next-line no-unused-vars
function d105() {
  fetch(localhost + 'd105')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t105').innerHTML = date + "疫情相关舆论词云"
        document.getElementById('d105').innerHTML = ""
        const wordCloud = new WordCloud('d105', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'date',
          legend: {},
          color,
          imageMask: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.puchedu.cn%2Fuploads%2F0%2F26%2F681270724%2F3795654864.jpg&refer=http%3A%2F%2Fimg.puchedu.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1651793329&t=f22f29fd7ac13457df1fa4a17e1d2028',
          wordStyle: {
            fontFamily: 'Avenir',
            fontSize: [4, 32],
          },
          state: {
            active: {
              style: {
                lineWidth: 0,
                shadowBlur: 4,
                shadowColor: 'rgba(0,0,0,0.3)',
              },
            },
          },
        });

        wordCloud.render();
      });
}

// eslint-disable-next-line no-unused-vars
function dl1() {
  fetch(localhost + date + "/" + ids + "/l1")
      .then(res => res.json())
      .then(data => {
        l1.setData(data)
      })
}

// eslint-disable-next-line no-unused-vars
function dl2() {
  fetch(localhost + date + "/l2")
      .then((res) => res.json())
      .then((data) => {
        l2.setData(data)
      })
}

// eslint-disable-next-line no-unused-vars
function dl3() {
  fetch(localhost + "/d105")
      .then((res) => res.json())
      .then((data) => {
        l3.setData(data)
      });
}

export default {
  name: "ybdsjp1",
  components: {
    // eslint-disable-next-line vue/no-unused-components
    laizheshikeTable
  },
  data() {
    return {
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
      table_columns: [],
      table_data: [],
      id: 1
    }
  },
  methods: {
    //隔行变色
    tableRowClassName() {
      //选取DOM节点
      var trs = this.$refs.mytable.$el
          .getElementsByTagName("tbody")[0]
          .getElementsByTagName("tr");
      for (var i in trs) {
        if (i % 2 === 0) {
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
    handleSelect(row) {
      ids = row.id
      scene.setCenter([row.jd, row.wd])
      scene.setZoom(9)
      const popup = new Popup({
        offsets: [0, 0],
        closeButton: false
      })
          .setLnglat([row.jd, row.wd])
          .setHTML(
              `<span style="color: #777">时间：${date + " " + row['h'] + ":00:00"}</span>` + '<br>' +
              `<span style="color: #777">活动区域: ${row['city']}</span>`
          );
      scene.addPopup(popup);
      dl1()
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
    handleSubmit() {
      this.$message({
        message: "上传成功！",
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
      fetch(localhost + date + "/d101")
          .then((res) => res.json())
          .then((data) => {
            document.getElementById('t101').innerHTML = date + "密接人员信息"
            this.table_columns = data['columns']
            var dataArray = data['data']
            this.table_data = []
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
  },
  mounted() {

    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        pitch: 0,
        type: 'amap',
        style: 'amap://styles/a744d30c08959067c602b2251d5bb58b?isPublic=true',
        center: [119.295469, 36.357701],
        zoom: 6,
      })
    });


    fetch(localhost + date + "/" + ids + "/l1")
        .then(res => res.json())
        .then(data => {
          l1 = new LineLayer({
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
              .size(2)
              .shape('greatcircle')
              .animate({
                enable: true,
                interval: 0.2,
                trailLength: 0.5,
                duration: 2
              })
              .color(color[0])
              .style({
                opacity: 1
              });
          scene.addLayer(l1);
          l1.on('click', (ev) => {
            const popup = new Popup({
              offsets: [0, 0],
              closeButton: false
            })
                .setLnglat(ev.lngLat)
                .setHTML(
                    `<span style="color: #777">时间：${date + " " + ev.feature['city'] + ":00:00"}</span>` + '<br>' +
                    `<span style="color: #777">活动区域: ${ev.feature['city']}</span>`
                );
            scene.addPopup(popup);
          })
        });

    fetch(localhost + date + "/l2")
        .then((res) => res.json())
        .then((data) => {
          l2 = new HeatmapLayer({})
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
                radius: 20,
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
          scene.addLayer(l2)
        })

    fetch(localhost + 'd105')
        .then((res) => res.json())
        .then((data) => {
          // data.features = data.features.filter(item => {
          //   return (
          //       item.properties.jd >= Math.min(lng1, lng2) &&
          //       item.properties.jd <= Math.max(lng1, lng2) &&
          //       item.properties.wd >= Math.min(lat1, lat2) &&
          //       item.properties.wd <= Math.max(lat1, lat2)
          //   );
          // });
          // console.log(data)
          l3 = new PointLayer({})
              .source(data, {
                parser: {
                  type: 'json',
                  x: 'jd',
                  y: 'wd'
                }
              })
              .shape('name', 'text')
              .size('value', [12, 20])
              .color('dateId', ['#999999', '#888888', '#777777', '#666666', '#555555', '#444444', '#333333'])
              .style({
                textAnchor: 'center', // 文本相对锚点的位置 center|left|right|top|bottom|top-left
                textOffset: [0, 0], // 文本相对锚点的偏移量 [水平, 垂直]
                spacing: 1,
                padding: [1, 1],
                strokeOpacity: 1.0
              });
          scene.addLayer(l3)
        })


    this.initEditAttribute()


    d101()
    d102()
    d103()
    d104()
    d105()


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
  width: 98%;
  height: 90%;
  left: 1%;
  top: 25px;
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
  background-color: #40555A;
}

.divs {
  position: absolute;
  text-align: center;
  background-color: #e5f3f8;
  border-width: 1px;
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
  background-color: #e5f3f8;
  border-color: #eee;
  border-width: 1px;
  color: #000;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>
