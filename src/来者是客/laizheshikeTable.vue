<template>
  <div style="left: 0; top: 0; width: 100%; height: 100%; position: absolute">
    <el-table
        ref="mytable"
        :data="table_data"
        style="width: 100%"
        @selection-change="handleSelectionChange"
        height="340"
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
          >查看</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
let localhost = "http://127.0.0.1:5000/"


// eslint-disable-next-line no-unused-vars
let y = 2022, m = 4, d = 5, date = "2022-04-01"

export default {
  name: "shuashuaxip3",
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
    initDate() {
      let ev = document.getElementById('date')
      y = ev.value.split("-")[0]
      m = ev.value.split("-")[1]
      d = ev.value.split("-")[2]
      this.initEditAttribute()
    },

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
    handleSelect(index, row) {
      this.id = row['id']
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

    this.initEditAttribute()


  }
}
</script>

<style scoped>
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
  height: 15px;
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