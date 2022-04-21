<template>
  <div style="position: absolute; width: 100%; height: 100%; left: 0; top: 0; background-color: #000000; opacity: 1">
    <div
        style="position: absolute; width: 25%; height: 90%; left: 37.5%; top:5%; opacity: 0.9; background-color: #EEFFFF; border-radius: 10px">
      <div class="title" id="mapTitle" style="color: #ffffff; font-size: 20px"></div>
      <div class="content" id="map1"></div>

      <div style="
        position: absolute;width: 40%;height: 20%;left: 2%;top: 2%;border-radius: 15px;background-color: #f5ffff;
        box-shadow: #ddffff 1px 1px 5px 5px; font-size: 5px;
      ">
        <div class="content" id="weather"></div>
      </div>

      <input className="selects" style="position: absolute; width: 25%; height: 2.5%; left: 1%; bottom: 5%" value="起点">
      <input className="selects" style="position: absolute; width: 25%; height: 2.5%; left: 35%; bottom: 5%" value="终点">
      <input className="selects" style="position: absolute; width: 25%; height: 2.5%; left: 70%; bottom: 5%"
             value="公交线路查询">
    </div>

  </div>

</template>

<script>
// eslint-disable-next-line no-unused-vars
import {GaodeMap, Layers, LineLayer, PointLayer, Scale, Scene, Zoom} from "@antv/l7";

// eslint-disable-next-line no-unused-vars
let scene, layer1, layer2, layer3, layer4, layer5, layer6, layer7, linesearch

// eslint-disable-next-line no-unused-vars
function gongJiao(id) {
  scene.on('loaded', () => {
    window.AMap.plugin(['AMap.ToolBar', 'AMap.LineSearch'], () => {
      // eslint-disable-next-line no-undef
      // scene.map.addControl(new AMap.ToolBar());
      // eslint-disable-next-line no-undef
      linesearch = new AMap.LineSearch({
        pageIndex: 1, // 页码，默认值为1
        pageSize: 1, // 单页显示结果条数，默认值为20，最大值为50
        city: '聊城', // 限定查询城市，可以是城市名（中文/中文全拼）、城市编码，默认值为『全国』
        extensions: 'all' // 是否返回公交线路详细信息，默认值为『base』
      });
      linesearch.search(id, function (status, result) {
        // 打印状态信息status和结果信息result
        const {path, via_stops} = result.lineInfo[0];
        const startPoint = [path[0]];
        const endpoint = [path[path.length - 1]];
        // eslint-disable-next-line no-unused-vars
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

        const busLine = new LineLayer({blend: 'normal'})
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
        scene.addLayer(busLine);
        const startPointLayer = new PointLayer({zIndex: 1})
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
        scene.addLayer(startPointLayer);

        const endPointLayer = new PointLayer({zIndex: 1})
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
        scene.addLayer(endPointLayer);

        // const busStops = new PointLayer()
        //     .source(budStopsData, {
        //       parser: {
        //         x: 'lng',
        //         y: 'lat',
        //         type: 'json'
        //       }
        //     })
        //     .shape('busStop')
        //     .size(13)
        //     .style({
        //       offsets: [20, 0]
        //     });
        // scene.addLayer(busStops);

        // const busStopsName = new PointLayer()
        //     .source(budStopsData, {
        //       parser: {
        //         x: 'lng',
        //         y: 'lat',
        //         type: 'json'
        //       }
        //     })
        //     .shape('name', 'text')
        //     .size(12)
        //     .color('#000')
        //     .style({
        //       textAnchor: 'left',
        //       textOffset: [80, 0],
        //       stroke: '#fff',
        //       strokeWidth: 1
        //     });
        // scene.addLayer(busStopsName);
      });
    });
  });
}


export default {
  name: "back",
  data() {
    return {}
  },
  methods: {},
  mounted() {
    // eslint-disable-next-line no-undef
    scene = new Scene({
      id: 'map1',
      map: new GaodeMap({
        style: 'amap://styles/83b73ccd633185b096afe1b7035f9a1c?isPublic=true',
        pitch: 45,
        center: [116.000651, 36.45137],
        zoom: 11,
        plugin: [
          'AMap.ToolBar',
          'AMap.LineSearch',
          'AMap.Weather',
          'AMap.Driving',
          "AMap.DragRoute"
        ]
      })
    });


    scene.on('loaded', () => {
      // eslint-disable-next-line no-undef
      window.AMap.plugin('AMap.Weather', () => {
        //创建天气查询实例
        // eslint-disable-next-line no-undef
        let weather = new AMap.Weather();
        //执行实时天气信息查询
        weather.getLive('聊城市', function (err, data) {
          document.getElementById('weather').innerHTML = "" +
              "时间：" + data['reportTime'] + '<br>' +
              "城市：" + data['city'] + '<br>' +
              "气温：" + data['temperature'] + "℃" + '<br>' +
              "风向：" + data['windDirection'] + '<br>' +
              "风速：" + data['windPower'] + '<br>' +
              "AQI：" + data['humidity'] + '<br>'
        });
      });
    })


    scene.on('loaded', () => {
      window.AMap.plugin('AMap.Driving', function () {
        // eslint-disable-next-line no-undef
        const driving = new AMap.Driving({
          // 驾车路线规划策略，AMap.DrivingPolicy.LEAST_TIME是最快捷模式
          // eslint-disable-next-line no-undef
          policy: AMap.DrivingPolicy.LEAST_TIME
        });

        const points = [
          {keyword: '北京市地震局（公交站）', city: '北京'},
          {keyword: '亦庄文化园（地铁站）', city: '北京'}
        ];

        // eslint-disable-next-line no-unused-vars
        driving.search(points, function (status, result) {
          // 未出错时，result即是对应的路线规划方案
        })
      })
    })


    const zoomControl = new Zoom({
      position: 'topright'
    });
    const scaleControl = new Scale({
      position: 'bottomright'
    });
    scene.addControl(zoomControl);
    scene.addControl(scaleControl);
    const overlayers = {
      // 气泡图: pointLayer
    };
    const layersControl = new Layers({
      overlayers,
      position: 'topright'
    });
    scene.addControl(layersControl);
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
    // scene.addImscene.addImage(
    //     'busStop',
    //     'https://gw.alipayobjects.com/zos/bmw-prod/54345af2-1d01-43e1-9d11-cd9bb953202c.svg'
    // );age(
    //     'busStop',
    //     'https://gw.alipayobjects.com/zos/bmw-prod/54345af2-1d01-43e1-9d11-cd9bb953202c.svg'
    // );


    gongJiao('k22')


  }
}

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

html {
  background-color: #efefff;
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  text-align: center;
}

.content {
  position: absolute;
  width: 96%;
  height: 92%;
  left: 2%;
  top: 7%;
  text-align: center;
}

.title {
  position: absolute;
  width: 50%;
  height: 6%;
  left: 25%;
  top: 0;
  text-align: center;
  font-size: 20%;
  color: #000000;
  font-weight: bold;

}

.divs {
  position: absolute;
  border-radius: 10px;
  background-color: #ffffff;
  text-align: center;
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