<template lang="pug">
.full-height(:class="$q.dark.isActive?'drawer_dark':'drawer_normal'")
  div.text-white(style='height: calc(100% - 117px);padding:10px;')
    q-toolbar
      q-toolbar-title.text-caption Bienvenido,
        span.text-weight-bold  {{currentUser}}
    hr
    q-scroll-area(style='height:100%;')
      q-list(padding='')
        q-item.q-ma-sm.navigation-item(active-class='tab-active', :to="{ name: 'profilingList' }", exact='', clickable='', v-ripple='')
          q-item-section(avatar='')
            q-icon(name='dashboard')
          q-item-section
            | Perfilamiento
        q-item.q-ma-sm.navigation-item(active-class='tab-active', to='/standardization', exact='', clickable='', v-ripple='')
          q-item-section(avatar='')
            q-icon(name='dashboard')
          q-item-section
            | Estandarización
        q-item.q-ma-sm.navigation-item(active-class='tab-active', to='/enrichment', exact='', clickable='', v-ripple='')
          q-item-section(avatar='')
            q-icon(name='dashboard')
          q-item-section
            | Enriquecimiento
        q-item.q-ma-sm.navigation-item(active-class='tab-active', to='/macth', exact='', clickable='', v-ripple='')
          q-item-section(avatar='')
            q-icon(name='dashboard')
          q-item-section
            | Igualar
</template>

<style>
  .q-drawer {
    /*background-image: url(https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg) !important;*/
    background-image: url(~assets/img/dashboard/aside.png);
    background-size: cover !important;
    background-position: right;
  }
  .q-drawer--right {
    border-left: 3px solid #b38e5d;
  }
</style>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'RigthAside',
  computed: {
    ...mapGetters([
      'currentUser'
    ])
  }
}
</script>
