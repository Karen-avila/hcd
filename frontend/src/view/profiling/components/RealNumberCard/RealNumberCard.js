import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'RealNumberCard',
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
      chartOptions: {
        chart: {
          id: this.key
        },
        xaxis: {
          categories: this.string2array(this.cardData.histogram[1])
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
        colors: ['#691c32']
      },
      series: [{
        name: '',
        data: this.string2array(this.cardData.histogram[0])
      }]
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
