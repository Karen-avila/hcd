import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'UrlCard',
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
      tab1: '',
      show: false
    }
  }
}
