import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'CategoricalCard',
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
      tab: 'estadisticas',
      tab1: '',
      show: false,
      chartOptions3: {
        chart: {
          width: 380,
          type: 'pie'
        },
        labels: ['1', '2', '3'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      },
      series3: [44, 55, 13],
      chartOptions: {
        chart: {
          id: this.key
        },
        xaxis: {
          categories: this.string2array(this.cardData.histogram_frequencies[1])
        },
        dataLabels: {
          enabled: false
        },
        plotOptions: {
          bar: {
            distributed: true,
            dataLabels: {
              position: 'top'
            }
          }
        },
        colors: ['#935116']
      },
      series: [{
        name: '',
        data: this.string2array(this.cardData.histogram_frequencies[0])
      }],
      chartOptions2: {
        chart: {
          id: this.key
        },
        xaxis: {
          categories: this.string2array(this.cardData.histogram_length[1])
        },
        dataLabels: {
          enabled: false
        },
        plotOptions: {
          bar: {
            distributed: true,
            dataLabels: {
              position: 'top'
            }
          }
        },
        colors: ['#935116']
      },
      series2: [{
        name: '',
        data: this.string2array(this.cardData.histogram_length[0])
      }],
      series4: [{
        data: [549, 342]
      }],
      chartOptions4: {
        chart: {
          type: 'bar',
          height: 200
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
  },
  methods: {
    string2array (string) {
      return string
        .replaceAll('[', '')
        .replaceAll(']', '')
        .replaceAll('\n', '')
        .split(' ')
        .map(item => { return parseInt(item) })
        .filter(value => !Number.isNaN(value))
    }
  }
}
