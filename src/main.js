// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import user1 from "./aaa全能不想辅助/user1";
// import user2 from "./aaa全能不想辅助/user2";
// import user3 from "./aaa全能不想辅助/user3";
// import userFont from "./aaa全能不想辅助/userFont"
// import admin1 from "./aaa全能不想辅助/admin1"
// import admin2 from "./aaa全能不想辅助/admin2"
// import admin3 from "./aaa全能不想辅助/admin3"
// import adminFont from "./aaa全能不想辅助/adminFont"
import ybdsj from "./a复赛-医保大数据/ybdsj";
// import gwksh from "./a复赛-岗位可视分析平台/gwksh";
// import jicengdaijiuye from "./基层待就业人员岗位推荐/jicengdaijiuye";
// import ywglm from "./一碗咖喱面不要面/ywglm";
// import csqxpwgkpt from "./七个藤上一个娃--城市气象排污管控平台/csqxpwgkpt";
// import shapankeshihua from "./沙盘可视化/shapankeshihua";
// import 碳排放分析预测 from "./a复赛-碳排放分析预测/碳排放分析预测";
// import shuashuaxi from "./刷刷洗/shuashuaxi";
// import laizheshike from "./来者是客/laizheshike";
import dataV from '@jiaminghi/data-view'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
Vue.use(dataV)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
