<template>
  <div
      style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">
    <div
        style="position: absolute; width: 100%; height: 5%; left: 0; top: 0; background-color: #445566; z-index: 1000">
      <div
          style="position: absolute; width: 50%; left: 25%; text-align: center; font-size: 20px; color: #f9f9f9; font-weight: bold">
        基 层 岗 位 分 析 推 荐 平 台
      </div>
    </div>
    <div v-show="p1"
         style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">


      <div id="map" style="position: absolute;width: 59.8%;height: 66%;left: 20.1%;top: 5%; z-index: 1000">
        <div class="title" style="z-index: 100"></div>
      </div>
      <div style="position: absolute; width: 100%; height: 95%; left: 0; top: 5%">
        <div class="divs" style="width: 20%; height: 30%; left: 0; top: 0;">
          <div class="content" id="d1" style="height: 75%"></div>
          <div class="title" id="t1"></div>
        </div>
        <div class="divs" style="width: 20%; height: 30%; left: 0; top: 30%;">
          <div class="content" id="d2" style="top: 20%"></div>
          <div class="title" id="t2"></div>
        </div>
        <div class="divs" style="width: 20%; height: 40%; left: 0; top: 60%;">
          <div class="content" id="d3"></div>
          <div class="title" id="t3"></div>
        </div>
        <div class="divs" style="width: 79.9%; height: 30%; left: 20.1%; bottom: 0;">
          <div class="content" id="d4"></div>
          <div class="title" id="t4"></div>
        </div>
        <div class="divs" style="width: 0; height: 30%; right: 0; bottom: 0;">
          <div class="content" id="d5"></div>
          <div class="title" id="t5"></div>
        </div>
        <div v-show="d6" class="divs" style="width: 100%; height: 100%; left: 0; top: 0;opacity: unset;z-index: 10000">
          <div class="content" id="d6" style="top: 15%;">
            <el-table
                :data="tableData"
                border
                style="width: 100%"
                height="500">
              <el-table-column
                  fixed
                  prop="岗位名称"
                  label="岗位名称"
                  width="120">
              </el-table-column>
              <el-table-column
                  fixed
                  prop="匹配度"
                  label="匹配度"
                  width="50">
              </el-table-column>
              <el-table-column
                  prop="岗位类型"
                  label="岗位类型"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="城市"
                  label="城市"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="工作经验"
                  label="工作经验"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="学历"
                  label="学历"
                  width="300">
              </el-table-column>
              <el-table-column
                  prop="工作类型"
                  label="工作类型"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="公司名称"
                  label="公司名称"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="招聘人数"
                  label="招聘人数"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="薪资"
                  label="薪资"
                  width="120">
              </el-table-column>
              <el-table-column
                  fixed="right"
                  label="操作"
                  width="300">
                <template slot-scope="scope">

                  <el-button type="warning" size="mini" @click="d6ms(scope.row)">描述</el-button>
                  <el-button type="success" size="mini" @click="d6xq(scope.row)">需求</el-button>
                  <el-button type="primary" size="mini" @click="fDH">导航</el-button>
                  <el-button type="info" size="mini" @click="fVr">参观</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div class="title" id="t6"></div>
          <div style="position:absolute; left: 1%; top: 6%">
            <el-button type="info" size="mini" @click="d6Back">返回</el-button>
          </div>
        </div>

        <div v-show="d6_1" class="divs"
             style="width: 100%; height: 100%; left: 0; top: 0;opacity: unset;z-index: 10000">
          <div id="d601" class="content" style="top: 15%"></div>
          <div id="t6_1" class="title"></div>
          <div style="position:absolute; left: 1%; top: 6%">
            <el-button type="info" @click="d6_1Back">返回</el-button>
          </div>
        </div>
        <div v-show="d6_2" class="divs"
             style="width: 100%; height: 100%; left: 0; top: 0;opacity: unset;z-index: 10000">
          <div id="d602" class="content" style="top: 15%"></div>
          <div id="t6_2" class="title"></div>
          <div style="position:absolute; left: 1%; top: 6%">
            <el-button type="info" @click="d6_2Back">返回</el-button>
          </div>
        </div>
        <div v-show="d6_3" class="divs"
             style="width: 100%; height: 100%; left: 0; top: 0;opacity: unset;z-index: 10000">
          <div id="d603" class="content" style="top: 15%">
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
              <el-table-column label="操作" align="center">
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
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div id="t6_3" class="title"></div>
          <div style="position:absolute; left: 1%; top: 6%">
            <el-button type="info" @click="d6_3Back">返回</el-button>
            <el-button @click="handleAdd()" type="primary">增加</el-button>
          </div>
        </div>
        <div v-show="dvr" class="divs"
             style="width: 100%; height: 100%; left: 0; top: 0;opacity: unset;z-index: 10000">
          <div style="position:absolute; left: 1%; top: 6%">
            <el-button type="info" @click="dvrBack">返回</el-button>
          </div>
        </div>
        <iframe
            v-if="dvr"
            src="办公室.html"
            style="position: absolute; width: 90%; height: 80%; left: 5%; top: 15%;opacity: unset;z-index: 20000">
        </iframe>


        <div class="divs" style="width: 20%; height: 29.8%; right: 0; top: 40%;">
          <div class="content" id="d7" style="top: 20%; height: 75%"></div>
          <div class="title" id="t7"></div>
        </div>
        <div class="divs" style="width: 20%; height: 20%; right: 0; top: 20%;">
          <div class="content" id="d8"></div>
          <div class="title" id="t8"></div>
        </div>
        <div class="divs" style="width: 20%; height: 20%; right: 0; top: 0;">
          <div class="content" id="d9">
            <div style="position: absolute; height: 80%; top: 0; width: 100%; left: 0">
              <select
                  id="s900" class="selects" v-model="inputSex" @change="fs900"
                  style="position:absolute;width: 49%;height: 30%;left: 1%;top: 1%; z-index: 3000">
              </select>
              <select
                  id="s901" class="selects" v-model="inputPro" @change="fs901"
                  style="position:absolute;width: 49%;height: 30%;left: 50%;top: 1%; z-index: 3000">
              </select>
              <select
                  id="s902" class="selects" v-model="inputEdu" @change="fs902"
                  style="position:absolute;width: 49%;height: 30%;left: 1%;top: 30%; z-index: 3000">
              </select>
              <el-input
                  style="position:absolute;width: 49%;height: 5%;left: 50%;top: 30%;text-align: center"
                  v-model="inputAge"
                  placeholder="请输入年龄">
              </el-input>
            </div>
            <div style="position:absolute; width: 100%;height: 20%;left: 0;top: 60%">
              <!--            <el-button type="info" size="mini">注册</el-button>-->
              <el-button type="success" @click="queren" size="mini">岗位搜索</el-button>
              <el-button type="warning" @click="queren2" size="mini">信息匹配</el-button>
              <!--            <el-button type="primary" @click="queren3" size="mini">信息管理</el-button>-->
            </div>
          </div>
          <div class="title" id="t9"></div>
        </div>
      </div>

      <button id="l1" @click="fl1" class="selects"
              style="position: absolute; left: 25%; top: 5%; background-color: #dddd00; border-radius: 5px;">薪资热力
      </button>
      <button id="l2" @click="fl2" class="selects" style="position: absolute; left: 35%; top: 5%; border-radius: 5px;">
        招聘热度
      </button>
      <button id="l3" @click="fl3" class="selects" style="position: absolute; right: 35%; top: 5%; border-radius: 5px;">
        学历分布
      </button>
      <button id="l4" @click="fl4" class="selects" style="position: absolute; right: 25%; top: 5%; border-radius: 5px;">
        学历薪资
      </button>


      <select id="s1" @change="fs1" class="selects" style="left: 44%; top: 5%; width: 5%"></select>

    </div>
    <div v-show="p2"
         style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">
      <div style="position: absolute; width: 100%; height: 95%; left: 0; top: 5%">
        <div class="divs" style="left: 0; top: 0; width: 35%; height: 70%">
          <div class="content" id="d201"></div>
          <div class="title" id="t201"></div>
        </div>
        <div class="divs" style="left: 35%; top: 0; width: 35%; height: 70%">
          <div class="content" id="d202"></div>
          <div class="title" id="t202"></div>
        </div>
        <div class="divs" style="left: 0; top: 60%; width: 70%; height: 40%">
          <div class="content" id="d203"></div>
          <div class="title" id="t203"></div>
        </div>
        <div class="divs" style="left: 70%; top: 0; width: 30%; height: 100%">
          <div class="content" id="d204">
            <div class="divs" style="width: 90%; height: 30%; left: 5%; top: 5%">
              <div class="content" id="d2041"></div>
              <div class="title" id="t2041"></div>
            </div>
            <div class="divs" style="width: 90%; height: 30%; left: 5%; top: 37.5%">
              <div class="content" id="d2042"></div>
              <div class="title" id="t2042"></div>
            </div>
            <div class="divs" style="width: 90%; height: 45%; left: 5%; top: 70%">
              <div class="content" id="d2043" style="text-align: left"></div>
              <div class="title" id="t2043"></div>
            </div>
          </div>
          <div class="title" id="t204"></div>
        </div>
      </div>
    </div>
    <div v-show="p3"
         style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">
      <div style="position: absolute; width: 100%; height: 95%; left: 0; top: 5%">
        <div class="divs" style="left: 30%; top: 0; width: 70%; height: 40%">
          <div class="content" id="d302"></div>
          <div class="title" id="t302"></div>
        </div>
        <div class="divs" style="left: 0; top: 0; width: 30%; height: 100%">
          <div class="content" id="d301" style="position: absolute; height: 90%; top: 25px"></div>
          <div class="title" id="t301"></div>
        </div>
        <div class="divs" style="left: 30%; top: 40%; width: 35%; height: 60%">
          <div class="content" id="d303" style="position: absolute; height: 90%; top: 25px"></div>
          <div class="title" id="t303"></div>
        </div>
        <div class="divs" style="left: 65%; top: 40%; width: 35%; height: 60%">
          <div class="content" id="d304" style="position: absolute; height: 90%; top: 25px"></div>
          <div class="title" id="t304"></div>
        </div>
      </div>

      <select id="s3" @change="fs3" class="selects" style="left: 1%; top: 5%; width: 5%"></select>
      <select id="s5" @change="fs5" class="selects" style="left: 13%; top: 5%; width: 5%"></select>
      <select id="s4" @change="fs4" class="selects" style="left: 25%; top: 5%; width: 5%"></select>

    </div>
    <div v-show="p4"
         style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">
      <gwksh_company style="position: absolute; width: 100%; height: 95%; left: 0; top: 5%"/>
    </div>
    <div v-show="p5"
         style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;">
      <gwksh_admin style="position: absolute; width: 100%; height: 95%; left: 0; top: 5%"/>
    </div>

    <button id="b1" @click="fp1" class="selects"
            style="position: absolute; left: 1%; top: 1%; background-color: #f9f9f9">推荐查找
    </button>
    <button id="b2" @click="fp2" class="selects"
            style="position: absolute; left: 25%; top: 1%; background-color: #dddd00">岗位特征
    </button>
    <button id="b3" @click="fp3" class="selects"
            style="position: absolute; right: 25%; top: 1%; background-color: #f9f9f9">分析对比
    </button>
    <button id="b4" @click="fp4" class="selects"
            style="position: absolute; right: 4%; top: 1%; width: 3%; background-color: #f9f9f9">信息
    </button>
    <button id="b5" @click="fp5" class="selects"
            style="position: absolute; right: 1%; top: 1%; width: 3%; background-color: #f9f9f9">管理
    </button>


    <select v-if="!this.p4&&!this.p5" id="s2" @change="fs2" class="selects"
            style="left: 51%; top: 5%; width: 5%"></select>
  </div>

</template>

<script>

// eslint-disable-next-line no-unused-vars
import gwksh_admin from "@/a复赛-岗位可视分析平台/gwksh_admin";
import gwksh_company from "@/a复赛-岗位可视分析平台/gwksh_company";

// eslint-disable-next-line no-unused-vars
import {GaodeMap, HeatmapLayer, LineLayer, PointLayer, Popup, Scene} from "@antv/l7";

// eslint-disable-next-line no-unused-vars
import {
  Heatmap,
  WordCloud,
  Bar,
  Rose,
  // eslint-disable-next-line no-unused-vars
  Line,
  // eslint-disable-next-line no-unused-vars
  Liquid,
  Scatter,
  Sankey,
  // eslint-disable-next-line no-unused-vars
  Area,
  BidirectionalBar,
  // eslint-disable-next-line no-unused-vars
  Sunburst, Pie, Column
} from "@antv/g2plot";

// eslint-disable-next-line no-unused-vars
import * as echarts from 'echarts';

// eslint-disable-next-line no-unused-vars
import G6 from '@antv/g6';
// eslint-disable-next-line no-unused-vars
import insertCss from "insert-css";
// eslint-disable-next-line no-unused-vars
import {each, groupBy} from "@antv/util";

// eslint-disable-next-line no-unused-vars
let scene, layer1, layer2, layer3, layer4,
    // eslint-disable-next-line no-unused-vars
    city = '上海', gwlx = '英语老师', xl = "大专", zy = "法律类", gzjy = '1-3年', gsmc = '精锐教育', _gsmc = "尚孔教育",
    // eslint-disable-next-line no-unused-vars
    linesearch, busLine, startPointLayer, endPointLayer, busStops, busStopsName,
    // eslint-disable-next-line no-unused-vars
    scene4, layer401, layer402, layer403, layer404,
    // eslint-disable-next-line no-unused-vars
    lJd = 121, lWd = 31


// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:1500/'

let color = [
  // '#086568',
  '#0F3F61',
  '#1D4042',
  '#2A4233',
  '#454325',
  '#4C4C2E',
  '#575746',
  '#917F54',
  // '#9B8471',
].reverse()

// let color = [
//     '#445566',
//     '#555566',
//     '#666666',
//     '#776666',
//     '#887755',
//     '#997755',
//     '#aa8855',
//     '#bb8855'
// ].reverse()


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

function c1() {
  fetch(localhost + city + "/" + gwlx + "/" + xl + "/" + selectTxt('s1'))
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t1').innerHTML = city + gwlx + xl + selectTxt('s1') + "词云"
        document.getElementById('d1').innerHTML = ""
        const wordCloud = new WordCloud('d1', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'value',
          color,
          wordStyle: {
            fontFamily: 'Verdana',
            fontSize: [8, 32],
            rotation: 40,
          },
          // 返回值设置成一个 [0, 1) 区间内的值，
          // 可以让每次渲染的位置相同（前提是每次的宽高一致）。
          random: () => 0.5,
        });
        wordCloud.render();
      });
}

function c2() {
  fetch(localhost + gwlx + '/div2')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return -x.招聘信息数量 + y.招聘信息数量
        }

        data = data.sort(cmp)
        document.getElementById('t2').innerHTML = gwlx + "学历需求热度"
        document.getElementById('d2').innerHTML = ""
        const rosePlot = new Rose('d2', {
          data,
          xField: 'name',
          yField: '招聘信息数量',
          seriesField: '招聘信息数量',
          color,
          radius: 0.7,
        });
        rosePlot.render();
        let hoverData = {}
        rosePlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        rosePlot.on('plot:click', ev => {
          ev = ""
          xl = ev + hoverData['name']
          fXl()
        })
      });
}

function c3() {
  fetch(localhost + gwlx + '/div3')
      .then((res) => res.json())
      .then((data) => {
        function cmp(x, y) {
          return -x.招聘信息数量 + y.招聘信息数量
        }

        data = data.sort(cmp)
        document.getElementById('t3').innerHTML = "不同城市" + gwlx + "招聘热度"
        document.getElementById('d3').innerHTML = ""
        const bar = new Bar('d3', {
          data,
          xField: '招聘信息数量',
          yField: 'name',
          seriesField: '招聘信息数量',
          color,
          legend: {
            position: 'top-left',
          },
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
          hoverData = ev.data.items[0].data;
        })
        bar.on('plot:click', ev => {
          ev = ""
          city = ev + hoverData['name']
          fCity()
        })
      });
}

function c4() {
  fetch(localhost + city + '/div4')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t4').innerHTML = city + "薪资分布情况"
        document.getElementById('d4').innerHTML = ""
        const line = new Area('d4', {
          data,
          xField: 'name',
          yField: '平均薪资',
          seriesField: 'type',
          color,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          smooth: true,
          slider: {
            start: 0.1,
            end: 0.2
          }
        });

        line.render();
        let hoverData = {}
        line.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        line.on('plot:click', ev => {
          ev = ""
          gwlx = ev + hoverData['name']
          fGwlx()
        })
      });

}

function c5() {

}

function c6() {

}

function c7() {
  fetch(localhost + city + "/" + gwlx + "/div7")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t7').innerHTML = city + gwlx + '学历经验热力'
        document.getElementById('d7').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d7'), {
          data,
          xField: '学历',
          yField: '工作经验',
          colorField: '平均薪资',
          color,
        });
        heatmapPlot.render();
        let hoverData = {}
        heatmapPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        heatmapPlot.on('plot:click', ev => {
          ev = ""
          xl = ev + hoverData['学历']
          fXl()
        })
      });
}

function c8() {
  fetch(localhost + gwlx + "/" + xl + '/div8')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t8').innerHTML = gwlx + xl + "工作经验与薪资发展的趋势"
        document.getElementById('d8').innerHTML = ""
        const scatterPlot = new Scatter('d8', {
          data,
          xField: '工作经验',
          yField: '平均薪资',
          size: 5,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          pointStyle: {
            stroke: color[3],
            lineWidth: 1,
            fill: color[0],
          },
          regressionLine: {
            type: 'quad', // linear, exp, loess, log, poly, pow, quad
          },
        });
        scatterPlot.render();
        let hoverData = {}
        scatterPlot.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        scatterPlot.on('plot:click', ev => {
          ev = ""
          gzjy = ev + hoverData['工作经验']
        })
      });
}

function c9() {

}

// eslint-disable-next-line no-unused-vars
function l1() {
  fetch(localhost + gwlx + "/l1_2")
      .then(res => res.json())
      .then(data => {
        layer1.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function l2() {
  fetch(localhost + gwlx + "/l1_2")
      .then(res => res.json())
      .then(data => {
        layer2.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function l3() {
  fetch(localhost + gwlx + "/" + xl + "/l3_4")
      .then(res => res.json())
      .then(data => {
        layer3.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function l4() {
  fetch(localhost + gwlx + "/" + xl + "/l3_4")
      .then(res => res.json())
      .then(data => {
        layer4.setData(data)
      });
}

// eslint-disable-next-line no-unused-vars
function fCity() {
  c1()
  c4()
  c7()
  c202()
}

// eslint-disable-next-line no-unused-vars
function fXl() {
  c1()
  c6()
  c8()
  l3()
  l4()
  c203()
}

// eslint-disable-next-line no-unused-vars
function fGwlx() {
  c1()
  c2()
  c3()
  c7()
  c8()
  l1()
  l2()
  l3()
  l4()
  c202()
  c203()
  c201()
  c2043()
  c301()
  c302()
  c303()
  c304()
}

// eslint-disable-next-line no-unused-vars
function fZy() {
  c5()
}

// eslint-disable-next-line no-unused-vars
function c201() {
  let chartDom = document.getElementById('d201');
  document.getElementById('t201').innerHTML = gwlx + "公司分布关系图"
  let myChart = echarts.init(chartDom);
  let option;

  // myChart.showLoading();
  fetch(localhost + gwlx + "/" + lJd + "/" + lWd + "/d201")
      .then((res) => res.json())
      .then((graph) => {
        // myChart.hideLoading();
        option = {
          title: false,
          tooltip: {},
          color,
          // width: 600,
          // height: 400,
          legend: [
            {
              // selectedMode: 'single',
              data: graph.categories.map(function (a) {
                return a.name;
              })
            }
          ],
          animationDuration: 1500,
          animationEasingUpdate: 'quinticInOut',
          series: [
            {
              name: '',
              type: 'graph',
              layout: 'none',
              data: graph.nodes,
              links: graph.links,
              categories: graph.categories,
              roam: true,
              label: {
                position: 'right',
                formatter: '{b}'
              },
              lineStyle: {
                color: 'source',
                curveness: 0.3
              },
              emphasis: {
                focus: 'adjacency',
                lineStyle: {
                  width: 3
                }
              }
            }
          ]
        };
        myChart.setOption(option);
        option && myChart.setOption(option);
      });
  myChart.on('click', ev => {
    gsmc = ev['data']['name']
    fGsmc()
  })

}

// eslint-disable-next-line no-unused-vars
function fGsmc() {
  c2041()
  c2042()
  c2043()
}

// eslint-disable-next-line no-unused-vars
function c202() {
  fetch(localhost + gwlx + "/" + city + "/d202")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d202').innerHTML = ""
        const sankey = new Sankey('d202', {
          data,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          color,
          edgeStyle: {
            fill: '#ccc',
            fillOpacity: 0.4,
          },
        });

        sankey.render();
      });
}

// eslint-disable-next-line no-unused-vars
function c203() {
  fetch(localhost + gwlx + "/d203")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t203').innerHTML = gwlx + "招聘人数分布图"
        document.getElementById('d203').innerHTML = ""
        const sankey = new Sankey('d203', {
          data,
          sourceField: 'source',
          targetField: 'target',
          weightField: 'value',
          color,
          edgeStyle: {
            fill: '#ccc',
            fillOpacity: 0.4,
          },
        });
        sankey.render();
      });
}

// eslint-disable-next-line no-unused-vars
function c2041() {
  fetch(localhost + gsmc + '/d2041')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t2041').innerHTML = gsmc + "岗位特征词云"
        document.getElementById('d2041').innerHTML = ""
        const wordCloud = new WordCloud('d2041', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'name',
          color,
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
      });
}

// eslint-disable-next-line no-unused-vars
function c2042() {
  fetch(localhost + gsmc + '/d2042')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t2042').innerHTML = gsmc + "技能特征词云"
        document.getElementById('d2042').innerHTML = ""
        const wordCloud = new WordCloud('d2042', {
          data,
          wordField: 'name',
          weightField: 'value',
          colorField: 'name',
          color,
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
      });
}

// eslint-disable-next-line no-unused-vars
function c2043() {
  fetch(localhost + gwlx + "/" + gsmc + '/d2043')
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t2043').innerHTML = gsmc + gwlx + "AI分析"
        document.getElementById('d2043').innerHTML = data['value1'] + "<br>" + "<br>" +
            data['value2'] + "<br>" + "<br>" +
            data['value3'] + "<br>" + "<br>" +
            data['value4'] + "<br>" + "<br>" +
            data['value5']
      });
}

// eslint-disable-next-line no-unused-vars
function c301() {
  fetch(localhost + selectTxt('s3') + "/" + selectTxt('s4') + "/" + gwlx + "/" + selectTxt('s5') + "/d301")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('d301').innerHTML = ""
        const BidirectionalBarPlot = new BidirectionalBar('d301', {
          data,
          xField: 'name',
          xAxis: {
            position: 'bottom',
            grid: null
          },
          yAxis: {
            grid: null
          },
          color: [color[0], color[5]],
          interactions: [{type: 'active-region'}],
          yField: [selectTxt('s3'), selectTxt('s4')],
          tooltip: {
            shared: true,
            showMarkers: false,
          },
        });
        BidirectionalBarPlot.render();
      })
}

// eslint-disable-next-line no-unused-vars
function c302() {
  fetch(localhost + gwlx + "/" + selectTxt('s5') + "/d302")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t302').innerHTML = gwlx + "不同" + selectTxt('s5') + "不同公司招聘人数对比分析"
        document.getElementById('d302').innerHTML = ""
        const line = new Area('d302', {
          data,
          xField: 'name',
          yField: 'value',
          seriesField: 'type',
          color,
          smooth: true,
          xAxis: {
            grid: null
          },
          yAxis: {
            grid: null
          },
          slider: {
            start: 0,
            end: 0.2
          }
        });

        line.render();
        let hoverData = {}
        line.on('tooltip:change', ev => {
          hoverData = ev.data.items[0].data;
        })
        line.on('plot:click', ev => {
          ev = ""
          gsmc = hoverData['name'] + ev
          c303()
        })
        // contextmenu
        line.on('plot:contextmenu', ev => {
          ev = ""
          _gsmc = hoverData['name'] + ev
          c304()
        })
      });
}

// eslint-disable-next-line no-unused-vars
function c303() {
  fetch(localhost + gwlx + "/" + gsmc + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t303').innerHTML = gsmc + gwlx + "薪资热力图"
        document.getElementById('d303').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d303'), {
          data,
          xField: 'name',
          yField: 'type',
          colorField: 'value',
          sizeField: 'value',
          shape: 'square',
          color,
        });
        heatmapPlot.render();
      });

}

// eslint-disable-next-line no-unused-vars
function c304() {
  fetch(localhost + gwlx + "/" + _gsmc + "/d303_4")
      .then((res) => res.json())
      .then((data) => {
        document.getElementById('t304').innerHTML = _gsmc + gwlx + "薪资热力图"
        document.getElementById('d304').innerHTML = ""
        const heatmapPlot = new Heatmap(document.getElementById('d304'), {
          data,
          xField: 'name',
          yField: 'type',
          colorField: 'value',
          sizeField: 'value',
          shape: 'square',
          color,
        });
        heatmapPlot.render();
      });

}


export default {
  name: "app",
  components: {
    gwksh_admin,
    gwksh_company
  },
  watch: {
    space_color: function () {
      //监听数据变化
      this.$nextTick(function () {
        /////方法
        this.tableRowClassName();
      });
    },
    table_data: function () {
      //监听数据变化f
      this.$nextTick(function () {
        /////方法
        this.tableRowClassName();
      });
    }
  },
  data() {
    return {
      p1: 0,
      p2: 1,
      p3: 0,
      p4: 0,
      p5: 0,


      inputSex: '',
      inputAge: '22',
      inputEdu: '',
      inputPro: '',
      d6: 0,
      d6_1: 0,
      d6_2: 0,
      d6_3: 0,
      dvr: 0,
      dh: 0,


      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        province: '上海',
        city: '普陀区',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }],
      tableData2: [
        {
          date: "2016-05-03",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333,
          sex: 18
        },
        {
          date: "2016-05-02",
          sex: 18,
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          sex: 18,
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        }
      ],
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
      //表头信息
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
        {
          prop: "专业类",
          label: "专业类",
          width: "150"
        },
        {
          prop: "岗位类型",
          label: "岗位类型",
          width: "150"
        },
        {
          prop: "面试通过",
          label: "面试通过",
          width: "150"
        },
        {
          prop: "面试预约",
          label: "面试预约",
          width: "150"
        }
      ],
      //表格数据
      table_data: [],

      p4_table_data: [],
      p4_table_columns: [],

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
      fetch(localhost + "/div603")
          .then((res) => res.json())
          .then((data) => {
            var self = this;
            // eslint-disable-next-line no-unused-vars
            var edit = self.edit;

            var dataArray = data

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
      fetch(localhost + gwlx + "/zpsj")
          .then((res) => res.json())
          .then((data) => {
            let columns = data['columns']
            this.p4_table_columns = columns

            data = data['data']
            var self = this;
            // eslint-disable-next-line no-unused-vars
            var edit = self.edit;

            var dataArray = data

            if (dataArray.length > 0) {
              //添加编辑事件
              for (var index in dataArray) {
                dataArray[index]["edit"] = false;
                this.p4_table_data.push(dataArray[index]);
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


    fs900() {
      this.inputSex = selectTxt('s900')
    },
    fs901() {
      this.inputPro = selectTxt('s901')
      zy = selectTxt('s901')
      fZy()
    },
    fs902() {
      this.inputEdu = selectTxt('s902')
      xl = selectTxt('s902')
    },
    queren() {
      zy = selectTxt('s901')
      let nl = this.inputAge
      fetch(localhost + selectTxt('s902') + "/" + city + "/" + gwlx + "/" + selectTxt('s900') + "/" + nl + "/" + selectTxt('s901') + "/" + gzjy + "/div6")
          .then((res) => res.json())
          .then((data) => {
            this.d6 = 1
            this.d6_1 = 0
            this.d6_2 = 0
            this.d6_3 = 0
            this.dvr = 0
            this.tableData = data
            fZy()
          })
    },
    queren2() {
      zy = selectTxt('s901')
      let nl = this.inputAge
      fetch(localhost + selectTxt('s900') + "/" + nl + "/" + selectTxt('s902') + "/" + selectTxt('s901') + "/" + gzjy + "/div6")
          .then((res) => res.json())
          .then((data) => {
            this.d6 = 1
            this.d6_1 = 0
            this.d6_2 = 0
            this.d6_3 = 0
            this.dvr = 0
            this.tableData = data['data']
            // console.log(data['data'])
            fXl()
            fZy()
            gwlx = data['gwlx']
            fGwlx()
          });
    },
    queren3() {
      this.d6 = 0
      this.d6_1 = 0
      this.d6_2 = 0
      this.dvr = 0
      this.d6_3 = 1
    },
    fVr() {
      this.d6 = 0
      this.d6_1 = 0
      this.d6_2 = 0
      this.dvr = 1
      this.d6_3 = 0
    },
    d6Back() {
      this.d6 = 0
    },
    d6_1Back() {
      this.d6_1 = 0
      this.d6 = 1
    },
    d6_2Back() {
      this.d6_2 = 0
      this.d6 = 1
    },
    d6_3Back() {
      this.d6_3 = 0
    },
    dvrBack() {
      this.d6 = 1
      this.dvr = 0
    },
    d6ms(ev) {
      this.d6 = 0
      this.d6_1 = 1
      document.getElementById('d601').innerHTML = ev['岗位描述']
    },
    d6xq(ev) {
      this.d6 = 0
      this.d6_2 = 1
      document.getElementById('d602').innerHTML = ev['技能需求']
    },


    fp1() {
      document.getElementById('b1').style.backgroundColor = '#dddd00'
      document.getElementById('b2').style.backgroundColor = '#f9f9f9'
      document.getElementById('b3').style.backgroundColor = '#f9f9f9'
      document.getElementById('b4').style.backgroundColor = '#f9f9f9'
      document.getElementById('b5').style.backgroundColor = '#f9f9f9'

      this.p1 = 1
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
      this.p5 = 0
    },
    fp2() {
      document.getElementById('b1').style.backgroundColor = '#f9f9f9'
      document.getElementById('b2').style.backgroundColor = '#dddd00'
      document.getElementById('b3').style.backgroundColor = '#f9f9f9'
      document.getElementById('b4').style.backgroundColor = '#f9f9f9'
      document.getElementById('b5').style.backgroundColor = '#f9f9f9'

      this.p1 = 0
      this.p2 = 1
      this.p3 = 0
      this.p4 = 0
      this.p5 = 0
    },
    fp3() {
      document.getElementById('b1').style.backgroundColor = '#f9f9f9'
      document.getElementById('b2').style.backgroundColor = '#f9f9f9'
      document.getElementById('b3').style.backgroundColor = '#dddd00'
      document.getElementById('b4').style.backgroundColor = '#f9f9f9'
      document.getElementById('b5').style.backgroundColor = '#f9f9f9'

      this.p1 = 0
      this.p2 = 0
      this.p3 = 1
      this.p4 = 0
      this.p5 = 0
    },
    fp4() {
      document.getElementById('b1').style.backgroundColor = '#f9f9f9'
      document.getElementById('b2').style.backgroundColor = '#f9f9f9'
      document.getElementById('b3').style.backgroundColor = '#f9f9f9'
      document.getElementById('b4').style.backgroundColor = '#dddd00'
      document.getElementById('b5').style.backgroundColor = '#f9f9f9'

      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 1
      this.p5 = 0
    },
    fp5() {
      document.getElementById('b1').style.backgroundColor = '#f9f9f9'
      document.getElementById('b2').style.backgroundColor = '#f9f9f9'
      document.getElementById('b3').style.backgroundColor = '#f9f9f9'
      document.getElementById('b4').style.backgroundColor = '#f9f9f9'
      document.getElementById('b5').style.backgroundColor = '#dddd00'

      this.p1 = 0
      this.p2 = 0
      this.p3 = 0
      this.p4 = 0
      this.p5 = 1
    },

    fl1() {
      layer1.show()
      layer2.hide()
      layer3.hide()
      layer4.hide()
      document.getElementById('l1').style.backgroundColor = '#dddd00'
      document.getElementById('l2').style.backgroundColor = '#f9f9f9'
      document.getElementById('l3').style.backgroundColor = '#f9f9f9'
      document.getElementById('l4').style.backgroundColor = '#f9f9f9'
    },
    fl2() {
      layer1.hide()
      layer2.show()
      layer3.hide()
      layer4.hide()
      document.getElementById('l1').style.backgroundColor = '#f9f9f9'
      document.getElementById('l2').style.backgroundColor = '#dddd00'
      document.getElementById('l3').style.backgroundColor = '#f9f9f9'
      document.getElementById('l4').style.backgroundColor = '#f9f9f9'
    },
    fl3() {
      layer1.hide()
      layer2.hide()
      layer3.show()
      layer4.hide()
      document.getElementById('l1').style.backgroundColor = '#f9f9f9'
      document.getElementById('l2').style.backgroundColor = '#f9f9f9'
      document.getElementById('l3').style.backgroundColor = '#dddd00'
      document.getElementById('l4').style.backgroundColor = '#f9f9f9'
    },
    fl4() {
      layer1.hide()
      layer2.hide()
      layer3.hide()
      layer4.show()
      document.getElementById('l1').style.backgroundColor = '#f9f9f9'
      document.getElementById('l2').style.backgroundColor = '#f9f9f9'
      document.getElementById('l3').style.backgroundColor = '#f9f9f9'
      document.getElementById('l4').style.backgroundColor = '#dddd00'
    },

    fs1() {
      c1()
    },
    fs2() {
      gwlx = selectTxt('s2')
      fGwlx()
      this.initEditAttribute()
    },
    fs3() {
      c301()
    },
    fs4() {
      c301()
    },
    fs5() {
      c301()
      c302()
    },
    fDH() {
      if (this.dh === 0) {
        busLine.show()
        startPointLayer.show()
        endPointLayer.show()
        busStops.show()
        busStopsName.show()
        this.dh = 1
        this.d6 = 0
        this.d6_1 = 0
        this.d6_2 = 0
      } else {
        busLine.hide()
        startPointLayer.hide()
        endPointLayer.hide()
        busStops.hide()
        busStopsName.hide()
        this.dh = 0
      }

    }
  },
  mounted() {


    this.initEditAttribute();
    //确保方法在页面渲染后调用
    this.$nextTick(function () {
      /////方法
      this.tableRowClassName();
    });


    addListOption('s1', ['技能需求', '岗位描述'])
    addListOption('s2', ['英语老师', '店长', '导购员', '客服', '物流跟单', '报检报关', '仓储管理', '课程顾问', '教务', '助教', '编导', '编剧', '后期制作', '化妆师', '广告创意', '美术指导', '文案', '媒介', '网页设计', '插画师', '工业设计', '视觉设计', '教师', '英语', '美术老师', '幼教', '小学教师', '班主任', '摄影师', '摄影', '制片', '记者', '剪辑', '策划经理', '广告制作', '广告审核', '平面设计', '美容师', '医美', '导游', '旅游计调', '旅游销售', '收银员', '收银', '家政', '美容导师', '健身教练', '旅游顾问', '签证', '票务', '服务业', '酒店前台', '酒店管理', '餐饮管理', '保安', '保洁', '司机', '市场策划', '市场顾问', '市场推广', 'sem', '网络营销', '活动策划', '销售经理', '销售代表', '大客户销售', '电话销售', '商品经理', '广告销售', '销售总监', '市场营销', '市场总监', 'seo', '品牌经理', '商务渠道', '销售专员', '客户代表', 'bd经理', '渠道销售', '销售助理', '销售顾问', '营销主管', '商务总监', '城市经理', '招聘', '人力资源专员', '人力资源经理', '员工关系', '出纳', '税务', '财务分析', '法务专员', '法律顾问', '法务主管', '前台', '经理助理', '行政经理', '行政总监', '人力资源主管', 'hrbp', '培训', '薪资福利', '人力资源总监', '会计', '财务顾问', '结算', '风控', '财务主管', '律师', '物流运营', '绩效考核', '组织发展', '理货员', '育婴师', '财务经理', '美甲师', '月嫂', '催乳师', '保姆', '纹绣师', 'app推广', '物仓调度', '婚礼策划'])
    addListOption('s3', ['上海', '青浦区', '杨浦区', '徐汇区', '浦东新区', '长宁区', '黄浦区', '普陀区', '闵行区', '松江区', '虹口区', '宝山区', '嘉定区', '静安区', '崇明区', '金山区', '奉贤区'])
    addListOption('s4', ['青浦区', '上海', '杨浦区', '徐汇区', '浦东新区', '长宁区', '黄浦区', '普陀区', '闵行区', '松江区', '虹口区', '宝山区', '嘉定区', '静安区', '崇明区', '金山区', '奉贤区'])
    addListOption('s5', ['学历', '工作经验'])

    addListOption('s900', ['男', '女'])
    addListOption('s901', ['文秘类', '哲学、马克思主义理论类', '教育学类', '新闻传播学类', '历史学类', '档案学类', '法律类', '计算机与信息科学类', '政治学类', '经济管理类', '工商管理类', '社会学类', '财会、税务、审计与统计类', '环境与安全类', '建筑类', '海洋与渔业类', '生物类', '动物生产类', '植物生产类', '林业类', '农林业工程类', '水电类', '交通运输类', '艺术类', '公安类', '地质及测绘类', '药学类', '理化类', '轻工纺织品食品类', '大气科学类', '心理学类', '材料类', '机械与仪表类', '体育学类', '非汉语言文学类'])
    addListOption('s902', ['大专', '学历不限', '本科', '高中', '中专/中技', '初中及以下', '硕士', '博士', '中技', 'MBA/EMBA'])

    c202()
    c2041()
    c2042()
    c2043()
    c201()
    c203()

    c1()
    c2()
    c3()
    c4()
    c5()
    c6()
    c7()
    c8()
    c9()


    c301()
    c302()
    c303()
    c304()


    scene = new Scene({
      id: 'map',
      map: new GaodeMap({
        style: 'light',
        pitch: 40,
        // style: 'amap://styles/45acf9c63991132cf759a67613e1f2d5?isPublic=true',
        center: [121.472666, 31],
        zoom: 8,
        plugin: ['AMap.ToolBar', 'AMap.LineSearch']
      })
    });


    scene.addImage(
        'road',
        'https://gw.alipayobjects.com/zos/bmw-prod/ce83fc30-701f-415b-9750-4b146f4b3dd6.svg'
    );
    scene.addImage(
        'start',
        'https://gw.alipayobjects.com/zos/bmw-prod/1c301f25-9bb8-4e67-8d5c-41117c877caf.svg'
    );
    scene.addImage(
        'end',
        'https://gw.alipayobjects.com/zos/bmw-prod/f3db4998-e657-4c46-b5ab-205ddc12031f.svg'
    );

    scene.addImage(
        'busStop',
        'https://gw.alipayobjects.com/zos/bmw-prod/54345af2-1d01-43e1-9d11-cd9bb953202c.svg'
    );


    scene.on('loaded', () => {
      window.AMap.plugin(['AMap.ToolBar', 'AMap.LineSearch'], () => {
        // eslint-disable-next-line no-undef
        // scene.map.addControl(new AMap.ToolBar());

        // eslint-disable-next-line no-undef
        linesearch = new AMap.LineSearch({
          pageIndex: 1, // 页码，默认值为1
          pageSize: 1, // 单页显示结果条数，默认值为20，最大值为50
          city: '上海', // 限定查询城市，可以是城市名（中文/中文全拼）、城市编码，默认值为『全国』
          extensions: 'all' // 是否返回公交线路详细信息，默认值为『base』
        });

        // 执行公交路线关键字查询
        linesearch.search('1', function (status, result) {
          // 打印状态信息status和结果信息result

          const {path, via_stops} = result.lineInfo[0];
          const startPoint = [path[0]];
          const endpoint = [path[path.length - 1]];
          const budStopsData = via_stops.map(stop => ({
            lng: stop.location.lng,
            lat: stop.location.lat,
            name: stop.name
          }));
          const data = [
            {
              id: '1',
              coord: path.map(p => [p.lng, p.lat])
            }
          ];

          busLine = new LineLayer({blend: 'normal'})
              .source(data, {
                parser: {
                  type: 'json',
                  coordinates: 'coord'
                }
              })
              .size(5)
              .shape('line')
              .color('rgb(99, 166, 242)')
              .texture('road')
              .animate({
                interval: 1, // 间隔
                duration: 1, // 持续时间，延时
                trailLength: 2 // 流线长度
              })
              .style({
                lineTexture: true,
                iconStep: 25
              });


          startPointLayer = new PointLayer({zIndex: 1})
              .source(startPoint, {
                parser: {
                  x: 'lng',
                  y: 'lat',
                  type: 'json'
                }
              })
              .shape('start')
              .size(20)
              .style({
                offsets: [0, 25]
              });


          endPointLayer = new PointLayer({zIndex: 1})
              .source(endpoint, {
                parser: {
                  x: 'lng',
                  y: 'lat',
                  type: 'json'
                }
              })
              .shape('end')
              .size(25)
              .style({
                offsets: [0, 25]
              });


          busStops = new PointLayer()
              .source(budStopsData, {
                parser: {
                  x: 'lng',
                  y: 'lat',
                  type: 'json'
                }
              })
              .shape('busStop')
              .size(13)
              .style({
                offsets: [20, 0]
              });


          busStopsName = new PointLayer()
              .source(budStopsData, {
                parser: {
                  x: 'lng',
                  y: 'lat',
                  type: 'json'
                }
              })
              .shape('name', 'text')
              .size(12)
              .color('#000')
              .style({
                textAnchor: 'left',
                textOffset: [80, 0],
                stroke: '#fff',
                strokeWidth: 1
              });

          scene.addLayer(busLine);
          scene.addLayer(startPointLayer);
          scene.addLayer(endPointLayer);
          scene.addLayer(busStops);
          scene.addLayer(busStopsName);

          busLine.hide()
          startPointLayer.hide()
          endPointLayer.hide()
          busStops.hide()
          busStopsName.hide()
        });
      });
      fetch(localhost + gwlx + "/l1_2")
          .then(res => res.json())
          .then(data => {
            layer1 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('heatmap')
                .size('value1', [0, 1.0]) // weight映射通道
                .style({
                  intensity: 2.0,
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
            scene.addLayer(layer1);
          });
      fetch(localhost + gwlx + "/l1_2")
          .then(res => res.json())
          .then(data => {
            layer2 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('heatmap')
                .size('value2', [0, 1.0]) // weight映射通道
                .style({
                  intensity: 2.0,
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
            scene.addLayer(layer2);
            layer2.hide()
          });
      fetch(localhost + gwlx + "/" + xl + "/l3_4")
          .then(res => res.json())
          .then(data => {
            layer3 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('heatmap')
                .size('value1', [0, 1.0]) // weight映射通道
                .style({
                  intensity: 2.0,
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
            scene.addLayer(layer3);
            layer3.hide()
          });
      fetch(localhost + gwlx + "/" + xl + "/l3_4")
          .then(res => res.json())
          .then(data => {
            layer4 = new HeatmapLayer({})
                .source(data, {
                  parser: {
                    type: 'json',
                    x: 'jd',
                    y: 'wd'
                  }
                })
                .shape('heatmap')
                .size('value2', [0, 1.0]) // weight映射通道
                .style({
                  intensity: 2.0,
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
            scene.addLayer(layer4);
            layer4.hide()
          });
    });


    scene.on('click', e => {
      lJd = e.lnglat.lng
      lWd = e.lnglat.lat
      let aaa = new Popup({
            offsets: [0, 0],
            closeButton: false
          }).setLnglat(e.lnglat)
              .setHTML(`<div class="title" style="text-align: center; font-size: 15px">预期工作地点<br>❤️</div>`)
      scene.addPopup(
          aaa
      );
      fetch(localhost + lJd + "/" + lWd + "/city")
          .then((res) => res.json())
          .then((data) => {
            city = data['city']
            fCity()
            c201()
          })
    });
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
  width: 96%;
  height: 80%;
  left: 2%;
  top: 25px;
  text-align: center;
  font-size: 20%;
  color: #000;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 100%;
  height: 25px;
  left: 0;
  top: 0;
  text-align: center;
  font-size: 20%;
  color: #fff;
  background-color: #456;
  font-weight: bold;

}

.divs {
  position: absolute;
  background-color: #eee;
  text-align: center;
  border-radius: 0;
  border-style: dot-dash;
  border-width: 10px;
  border-color: #f9f9f9;
  color: #000;
  box-shadow: #999 0 0 1px 1px;
  opacity: unset;
  z-index: 100;
}

.selects {
  position: absolute;
  width: 5%;
  height: 3%;
  background-color: #f9f9f9;
  border-color: #eee;
  border-width: 2px;
  border-style: dot-dash;
  color: #000;
  font-weight: bold;
  /*border-radius: 5px;*/
  font-size: 9px;
  text-align: center;
  z-index: 1000;
}
</style>
