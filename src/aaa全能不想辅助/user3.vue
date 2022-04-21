<template>
  <div style="position: absolute;width: 100%;height: 100%;left: 0;top: 0">
    <dv-border-box13
        style="position: absolute; width: 33%; height: 30%; left: 0; top: 11%"
        :color="['#55ddaa', '#99ffcc']"
    >
      <div id="div601" class="content">
        <img alt="" src="./img/乒乓球.png" style="position: absolute;width: 80%;height: 80%;left: 10%;top: 10%">
      </div>
      <div id="t601" class="title">VR乒乓球</div>
    </dv-border-box13>
    <dv-border-box13
        style="position: absolute; width: 33%; height: 30%; left: 33%; top: 11%"
        :color="['#55ddaa', '#99ffcc']"
    >
      <div id="div602" class="content">
        <img alt="" src="./img/篮球.png" style="position: absolute;width: 80%;height: 80%;left: 10%;top: 10%">
      </div>
      <div id="t602" class="title">VR篮球</div>
    </dv-border-box13>
    <dv-border-box13
        style="position: absolute; width: 33%; height: 30%; left: 66%; top: 11%"
        :color="['#55ddaa', '#99ffcc']"
    >
      <div id="div603" class="content">
        <img alt="" src="./img/象棋.png" style="position: absolute;width: 80%;height: 80%;left: 10%;top: 10%">
      </div>
      <div id="t603" class="title">VR象棋</div>
    </dv-border-box13>
    <dv-border-box13
        style="position: absolute; width: 33%; height: 30%; left: 0; top: 41%"
        :color="['#55ddaa', '#99ffcc']"
    >
      <div id="div604" class="content">
        <img alt="" src="./img/养老院参观.png" style="position: absolute;width: 80%;height: 80%;left: 10%;top: 10%">
      </div>
      <div id="t604" class="title">VR养老院参观</div>
    </dv-border-box13>

  </div>
</template>

<script>


// eslint-disable-next-line no-unused-vars
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


export default {
  name: "yantaiyanglaofusaip6",
  mounted() {


  },
  methods: {},
  data() {
    return {

    }
  }
}
</script>

<style scoped>
.content {
  position: absolute;
  width: 96%;
  height: 80%;
  left: 2%;
  top: 16%;
  text-align: center;
  font-size: 20%;
  color: #eeffee;
  font-weight: bold;
}

.title {
  position: absolute;
  width: 50%;
  height: 6%;
  left: 25%;
  top: 7%;
  text-align: center;
  font-size: 20%;
  color: #007700;
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
  background-color: #efe;
  border-color: #ded;
  border-width: 1px;
  color: #070;
  border-radius: 5px;
  z-index: 20;
  font-size: 9px;
  text-align: center;
}
</style>