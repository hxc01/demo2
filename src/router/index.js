import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import userFont from "../aaa全能不想辅助/userFont";
// import adminFont from "../aaa全能不想辅助/adminFont";
import ybdsj from "../a复赛-医保大数据/ybdsj";
// import gwksh from "../a复赛-岗位可视分析平台/gwksh";
// import jicengdaijiuye from "../基层待就业人员岗位推荐/jicengdaijiuye";
// import ywglm from "../一碗咖喱面不要面/ywglm";
// import csqxpwgkpt from "../七个藤上一个娃--城市气象排污管控平台/csqxpwgkpt";
// import shapankeshihua from "../沙盘可视化/shapankeshihua";
// import xxx from "../a复赛-碳排放分析预测/碳排放分析预测";
// import shuashuaxi from "../刷刷洗/shuashuaxi";
// import laizheshike from "../来者是客/laizheshike";

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/laizheshike',
    //   name: 'laizheshike ',
    //   component: laizheshike
    // },
    // {
    //   path: '/shuashuaxi',
    //   name: 'shuashuaxi ',
    //   component: shuashuaxi
    // }
    {
      path: '/ybdsj',
      name: 'ybdsj ',
      component: ybdsj
    }
    // {
    //   path: '/userFont',
    //   name: 'userFont',
    //   component: userFont
    // },
    // {
    //   path: '/admin',
    //   name: 'adminFont',
    //   component: adminFont
    // },
    // {
    //   path: '/gwksh',
    //   name: 'gwksh',
    //   component: gwksh
    // },
    // {
    //   path: '/jicengdaijiuye',
    //   name: 'jicengdaijiuye',
    //   component: jicengdaijiuye
    // },
    // {
    //   path: '/ywglm',
    //   name: 'ywglm',
    //   component: ywglm
    // },
    // {
    //   path: '/csqxpwgkpt',
    //   name: 'csqxpwgkpt',
    //   component: csqxpwgkpt
    // },
    // {
    //   path: '/shapankeshihua',
    //   name: 'shapankeshihua',
    //   component: shapankeshihua
    // },
    // {
    //   path: '/xxx',
    //   name: 'xxx',
    //   component: xxx
    // }
  ]
})
