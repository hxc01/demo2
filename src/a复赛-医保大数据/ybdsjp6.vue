<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
    <div style="position: absolute;width: 98%;height: 85%;left: 1%;top: 12%;">
      <div class="divs" style="width: 59%; height: 99%; left: 0; top: 0">
        <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
          <div style="position: absolute; width: 100%; height: 90%; left: 0; top: 10%; opacity: unset;z-index: 10000">
            <div id="d601"
                 style="position: absolute; width: 100%; height: 100%; left: 0; top: 0; background-color: #eff">
              <el-table
                  ref="mytable"
                  :data="table_data"
                  style="width: 100%"
                  @selection-change="handleSelectionChange"
                  height="500"
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
                <el-table-column fixed label="操作" align="center" width="250">
                  <template slot-scope="scope">
                    <!-- 全局控制的编辑 -->
                    <div v-if="is_edit&&scope.row.add==undefined" style="display: inline-block;">
                      <!-- 编辑 -->
                      <el-button
                          size="mini"
                          v-if="!scope.row.edit"
                          @click="handleEdit(scope.$index, scope.row)"
                          type="primary"
                      >编辑
                      </el-button>
                      <!-- 保存 -->
                      <el-button
                          size="mini"
                          type="success"
                          :plain="true"
                          v-if="scope.row.edit"
                          @click="handleSave(scope.$index, scope.row)"
                      >保存
                      </el-button>
                    </div>
                    <!-- 添加控制 -->
                    <div v-if="scope.row.add!=undefined&&scope.row.add" style="display: inline-block;">
                      <!-- 保存 -->
                      <el-button
                          size="mini"
                          type="success"
                          :plain="true"
                          v-if="scope.row.edit"
                          @click="handleSave(scope.$index, scope.row)"
                      >保存
                      </el-button>
                    </div>
                    <!-- 全局控制删除 -->
                    <el-button
                        size="mini"
                        v-if="is_delete&&scope.row.add==undefined"
                        :plain="true"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)"
                    >删除
                    </el-button>
                    <!--                      查看-->
                    <el-button
                        size="mini"
                        type="warning"
                        :plain="true"
                    >既往史
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
          <div style="position:absolute; right: 1%; top: 4%">
            <el-button @click="handleAdd()" type="primary" size="mini">增加</el-button>
          </div>
          <div style="position:absolute; right: 10%; top: 4%">
            <el-button @click="handleGx()" type="warning" size="mini">更新</el-button>
          </div>
          <div style="position:absolute; right: 19%; top: 4%">
            <el-button @click="handleBc()" type="success" size="mini">保存</el-button>
          </div>
        </div>
        <div id="t601" class="title"></div>
      </div>
      <div class="divs" style="width: 39%; height: 49%; left: 60%; top: 0">
        <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0">
          <div style="position: absolute; width: 100%; height: 90%; left: 0; top: 10%; opacity: unset;z-index: 10000">
            <div id="d602"
                 style="position: absolute; width: 100%; height: 100%; left: 0; top: 0; background-color: #eff">
              <el-table
                  ref="mytable"
                  :data="table_data2"
                  style="width: 100%"
                  @selection-change="handleSelectionChange"
                  height="260"
              >
                <el-table-column v-if="radio" type="index" width="50"></el-table-column>
                <el-table-column v-if="selection" type="selection" width="55"></el-table-column>
                <el-table-column
                    align="center"
                    v-for="(item,index,key) in table_columns2"
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
              </el-table>
            </div>
          </div>
        </div>
        <div id="t602" class="title"></div>
      </div>
      <div class="divs" style="width: 19.5%; height: 49%; left: 60%; top: 50%">
        <div id="d603" class="content"></div>
        <div id="t603" class="title"></div>
      </div>
      <div class="divs" style="width: 19%; height: 49%; left: 80%; top: 50%">
        <div id="d604" class="content"></div>
        <div id="t604" class="title"></div>
      </div>
      <select id="s601" @change="initEditAttribute" class="selects" style="left: 1%; top: 5%"></select>
      <select id="s602" @change="initEditAttribute" class="selects" style="left: 6%; top: 5%"></select>
      <select id="s603" @change="initEditAttribute" class="selects" style="left: 11%; top: 5%"></select>
      <select id="s604" @change="initEditAttribute" class="selects" style="left: 16%; top: 5%"></select>
      <select id="s605" @change="f605" class="selects" style="left: 60.5%; top: 54.6%"></select>

    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, PointLayer, Popup, Scene} from "@antv/l7";
// eslint-disable-next-line no-unused-vars
import {Area, Bar, Column, Heatmap, DualAxes, Gauge, Radar, Rose, Sunburst, WordCloud} from '@antv/g2plot';

// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:1500/"

// eslint-disable-next-line no-unused-vars
let scene, zdmc = '糖尿病胰岛素治疗', month = '9', day = '30'

// eslint-disable-next-line no-unused-vars
let color = [
  '#00eeff',
  '#00ccee',
  '#0099dd',
  '#0066cc',
  '#0033bb',
  '#0000aa'
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
function fYear() {
  c603()
  c604()
}

// eslint-disable-next-line no-unused-vars
function fMonth() {
  c604()
}

// eslint-disable-next-line no-unused-vars
function fDay() {
  c604()
  this.initEditAttribute()
}

// eslint-disable-next-line no-unused-vars
function fZdmc() {
  c603()
}

// eslint-disable-next-line no-unused-vars
function c603() {
  fetch(localhost + selectTxt('s605') + "/" + zdmc + "/d603")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t603').innerHTML = selectTxt('s605') + zdmc + "热度图"
        document.getElementById('d603').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d603'), {
          data,
          xField: 'day',
          yField: 'month',
          colorField: 'value',
          // legend: true,
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
          // 自己可以在控制台打印一下ev，看下里面的结构，找到自己所需要的信息
          hoverData = ev.data.items[0].data;
        })
        heatmapPlot.on('plot:click', ev => {
          ev = ""
          month = hoverData['month'] + ev
          day = hoverData['day'] + ev
          fDay()
        });
      });
}

// eslint-disable-next-line no-unused-vars
function c604() {
  fetch(localhost + selectTxt('s605') + "/" + month + "/" + day + "/d604")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t604').innerHTML = selectTxt('s605') + "年" + month + "月" + day + "日病症词云"
        document.getElementById('d604').innerHTML = ""
        const wordCloud = new WordCloud('d604', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'value',
          color,
          wordStyle: {
            fontFamily: 'Verdana',
            fontSize: [10, 30],
            rotation: 45,
          },
          random: () => 0.5,
        });
        wordCloud.render();
        let hoverData = {}
        wordCloud.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        wordCloud.on('plot:click', ev => {
          ev = ""
          zdmc = hoverData['text'] + ev
          fZdmc()
        });
      });
}

export default {
  name: 'p6',
  data() {
    return {
      table_columns: [
        {
          prop: "时间",
          label: "时间",
          width: "150"
        },
        {
          prop: "姓名",
          label: "姓名",
          width: "150"
        },
        {
          prop: "性别",
          label: "性别",
          width: "150"
        },
      ],
      //表格数据
      table_data: [],

      table_columns2: [],
      table_data2: [],
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

    addListOption('s601', ['日照市山海天旅游度假区', '日照市岚山区', '日照市东港区', '日照市经济开发区', '日照市莒县', '日照市五莲县'])
    addListOption('s602', ['日照市市辖区', '日照市经济开发区', '日照市东港区', '日照市岚山区', '日照市莒县', '日照市五莲县', '日照市山海天旅游度假区', '济南市'])
    addListOption('s603', ['门诊慢特病', '普通门诊', '住院'])
    addListOption('s604', ['三级', '二级', '一级'])
    addListOption('s605', ['2021', '2020', '2019', '2018', '2017'])


    c603()
    c604()
    this.initEditAttribute()


  },
  methods: {
    f605() {
      fYear()
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
    handleGx() {
      this.initEditAttribute()
      this.$message({
        message: "更新成功！",
        type: "warning"
      });
    },
    handleBc() {
      this.$message({
        message: "上传成功！",
        type: "success"
      });
    },
    //初始化编辑属性
    initEditAttribute() {
      fetch(localhost + selectTxt('s601') + "/" + selectTxt('s602') + "/" + selectTxt('s603') + "/" + selectTxt('s604') + "/d601")
          .then((res) => res.json())
          .then((data) => {
            let dataArray = data['data']
            this.table_columns = data['column']
            this.table_data = []
            if (dataArray.length > 0) {
              for (let index in dataArray) {
                dataArray[index]["edit"] = false;
                this.table_data.push(dataArray[index]);
              }
              if (Object.keys(this.new_date_json).length === 0) {
                this.initAddDataJson(dataArray[0]);
              }
            }
          })
      fetch(localhost + "/d602")
          .then((res) => res.json())
          .then((data) => {
            document.getElementById('t602').innerHTML = "12118122110076900000既往史"
            let dataArray = data['data']
            this.table_columns2 = data['column']
            this.table_data2 = []
            if (dataArray.length > 0) {
              for (let index in dataArray) {
                dataArray[index]["edit"] = false;
                this.table_data2.push(dataArray[index]);
              }
              if (Object.keys(this.new_date_json).length === 0) {
                this.initAddDataJson(dataArray[0]);
              }
            }
          });
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