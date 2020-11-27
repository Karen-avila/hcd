import Vue from 'vue'
import moment from 'moment'

Vue.filter('DateTime', function (value) {
  if (!value) return '-'
  moment.locale('es')
  return moment(value).format('DD/MM/YYYY, h:mm')
})
