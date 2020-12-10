import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'BooleanCard',
  components: {
    apexchart: VueApexCharts
  },
  props: {
    cardData: Object,
    cardName: String
  },
  data () {
    return {
      data: this.cardData,
      tab: '',
      show: false,
      series: [44, 55, 13],
      chartOptions: {
        chart: {
          width: 50,
          type: 'pie'
        },
        labels: ['0', '1'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 50
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      },
      series2: [{
        data: [549, 342]
      }],
      chartOptions2: {
        chart: {
          type: 'bar',
          height: 380
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: '100%',
            distributed: true,
            dataLabels: {
              position: 'bottom'
            }
          }
        },
        colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e',
          '#f48024', '#69d2e7'
        ],
        dataLabels: {
          enabled: true,
          textAnchor: 'start',
          style: {
            colors: ['#fff']
          },
          formatter: function (val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ':  ' + val
          },
          offsetX: 0,
          dropShadow: {
            enabled: true
          }
        },
        stroke: {
          width: 1,
          colors: ['#fff']
        },
        xaxis: {
          categories: ['0', '1']
        },
        yaxis: {
          labels: {
            show: false
          }
        }
      }
    }
  }
}
