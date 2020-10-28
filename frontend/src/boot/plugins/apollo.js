import { apolloProvider } from '@/boot/services/apollo.service'
import Vue from 'vue'

export const apolloService = apolloProvider

Vue.prototype.$apollo = apolloProvider.defaultClient
