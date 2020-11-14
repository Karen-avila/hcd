import Vue from 'vue'

Vue.filter('DateTime', function (value) {
  return value.toLocaleString()
})

