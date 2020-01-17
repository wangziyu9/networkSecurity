$(function () {
    // echart_1();
    echart_2();

    // echart_2河南省地图
    function echart_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_2'));
        $.post("/data/henan_aqirank", function (data, status) {
            myChart.setOption(option = {
                // backgroundColor: '#ffffff',
                visualMap: {
                    show: false,
                    min: 0,
                    max: 5000,
                    left: 'left',
                    top: 'bottom',
                    text: ['高', '低'], // 文本，默认为数值文本
                    calculable: true,
                    inRange: {
                        color: ['lightskyblue', 'lightgreen', 'red']
                    }
                },
                series: [{
                    type: 'map',
                    mapType: '河南',
                    roam: true,
                    label: {
                        normal: {
                            show: true
                        },
                        emphasis: {
                            textStyle: {
                                color: '#fff'
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            borderColor: '#389BB7',
                            areaColor: '#fff',
                        },
                        emphasis: {
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    },
                    animation: false,
                    data: data
                }]
            });
        });
        myChart.on('click', function (params) {
            window.open('/citymap/' + encodeURIComponent(params.name).replace("%E5%B8%82", ""));
        });
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

});