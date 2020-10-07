import Vue from 'vue'

Vue.config.productionTip = false
Vue.prototype.$appName = 'QUDA'

import gql from 'graphql-tag'
Vue.prototype.$gql = gql

import sweetAlert from 'sweetalert2'
Vue.prototype.$sweetAlert = sweetAlert
