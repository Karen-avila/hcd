import Vue from 'vue'

Vue.config.productionTip = false
Vue.prototype.$appName = process.env.ORGANIZATION

import gql from 'graphql-tag'
Vue.prototype.$gql = gql

import moment from 'moment'
Vue.prototype.$moment = moment

Vue.prototype.$filters = Vue.options.filters
