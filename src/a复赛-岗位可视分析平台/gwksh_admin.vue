<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0;background-color: #fff">
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#445566"
        text-color="#fff"
        active-text-color="#ffd04b">

      <el-menu-item index="1" @click="fd1">招聘数据</el-menu-item>
      <el-menu-item index="2" @click="fd2">公司数据</el-menu-item>
      <el-menu-item index="3" @click="fd3">面试数据</el-menu-item>

    </el-menu>


    <div v-show="d3" class="divs" style="width: 100%; height: 90%; left: 0; top: 10%; opacity: unset;z-index: 10000">
      <div id="d101" class="content" style="top: 10%">
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
          <el-table-column fixed label="操作" align="center">
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
      <div id="t101" class="title"></div>
      <div style="position:absolute; left: 1%; top: 5%">
        <el-button @click="handleAdd()" type="primary">增加</el-button>
      </div>
    </div>
    <div v-show="d2" class="divs" style="width: 100%; height: 90%; left: 0; top: 10%; opacity: unset;z-index: 10000">
      <div id="d102" class="content" style="top: 10%">
        <el-table
            ref="mytable"
            :data="table_data2"
            style="width: 100%"
            @selection-change="handleSelectionChange"
            height="500"
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
          <el-table-column fixed label="操作" align="center">
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
      <div id="t102" class="title"></div>
      <div style="position:absolute; left: 1%; top: 5%">
        <el-button @click="handleAdd()" type="primary">增加</el-button>
      </div>
    </div>
    <div v-show="d1" class="divs" style="width: 100%; height: 90%; left: 0; top: 10%; opacity: unset;z-index: 10000">
      <div id="d103" class="content" style="top: 10%">
        <el-table
            ref="mytable"
            :data="table_data3"
            style="width: 100%"
            @selection-change="handleSelectionChange"
            height="500"
        >
          <el-table-column v-if="radio" type="index" width="50"></el-table-column>
          <el-table-column v-if="selection" type="selection" width="55"></el-table-column>
          <el-table-column
              align="center"
              v-for="(item,index,key) in table_columns3"
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
              <span @click="consTable(scope.row)" v-if="  !scope.row.edit">{{ scope.row[item.prop] }}</span>
            </template>
          </el-table-column>
          <el-table-column fixed label="操作" align="center" width="150">
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
      <div id="t103" class="title"></div>
      <div style="position:absolute; left: 1%; top: 5%">
        <el-button @click="handleAdd()" type="primary">增加</el-button>
      </div>
    </div>


  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
let localhost = 'http://127.0.0.1:1500/'


export default {
  name: "app",
  components: {},
  data() {
    return {
      d1: 1,
      d2: 0,
      d3: 0,


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


      table_columns2: [],
      table_data2: [],

      table_columns3: [],
      table_data3: [],


      activeIndex2: '1'
    }
  },
  methods: {
    consTable(data) {
      console.log(data['公司名称'])
    },
    fd1() {
      this.d1 = 1
      this.d2 = 0
      this.d3 = 0
    },
    fd2() {
      this.d1 = 0
      this.d2 = 1
      this.d3 = 0
    },
    fd3() {
      this.d1 = 0
      this.d2 = 0
      this.d3 = 1
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


      fetch(localhost + "/gssj")
          .then((res) => res.json())
          .then((data) => {
            let columns = data['columns']
            this.table_columns2 = columns

            data = data['data']
            var self = this;
            // eslint-disable-next-line no-unused-vars
            var edit = self.edit;

            var dataArray = data

            if (dataArray.length > 0) {
              //添加编辑事件
              for (var index in dataArray) {
                dataArray[index]["edit"] = false;
                this.table_data2.push(dataArray[index]);
              }

              if (Object.keys(this.new_date_json).length === 0) {
                //新增时，初始化数据结构
                this.initAddDataJson(dataArray[0]);
              }
            }
          })



      fetch(localhost + "/zpsj")
          .then((res) => res.json())
          .then((data) => {
            let columns = data['columns']
            this.table_columns3 = columns

            data = data['data']
            var self = this;
            // eslint-disable-next-line no-unused-vars
            var edit = self.edit;

            var dataArray = data

            if (dataArray.length > 0) {
              //添加编辑事件
              for (var index in dataArray) {
                dataArray[index]["edit"] = false;
                this.table_data3.push(dataArray[index]);
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

    this.initEditAttribute();
    //确保方法在页面渲染后调用
    this.$nextTick(function () {
      /////方法
      this.tableRowClassName();
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
  height: 90%;
  left: 2%;
  top: 7%;
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
  top: 0;
  text-align: center;
  font-size: 20%;
  color: #000;
  font-weight: bold;

}

.divs {
  position: absolute;
  background-color: #fff;
  text-align: center;
  border-width: 3px;
  border-color: #222;
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