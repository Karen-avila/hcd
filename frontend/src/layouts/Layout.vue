<template lang="pug">
q-layout(view='hHr lpr fFr')
  q-header.bg-dark.text-white(elevated=false height-hint='98')
    q-toolbar
      q-toolbar-title.text-subtitle1.text-weight-light
        q-avatar.q-mr-md
          img(src='~assets/img/dashboard/logo.png')
        | Instituto Mexicano del Seguro Social
      q-btn.q-mr-md(flat='' round='' dense='' icon='home')
        q-tooltip(content-class='bg-accent') INICIO
      q-btn.q-mr-md(flat='' round='' dense='' icon='account_box')
        q-tooltip(content-class='bg-accent') PERFIL
      q-btn(@click='onLogout' flat='' round='' dense='' icon='login')
        q-tooltip(content-class='bg-accent') SALIR
      q-btn.q-ml-xl(dense='' flat='' round='' icon='menu' @click='right = !right')
        q-tooltip(content-class='bg-accent') MENU
    q-toolbar.bg-secondary(style="min-height: 2px;")
  q-drawer(show-if-above='' v-model='right' side='right' elevated='')
    RigthAside
  q-page-container
    router-view
  q-footer.bg-footer.text-white
    q-toolbar
      span.q-mb-sm
        | HERRAMIENTA DE CALIDAD DE DATOS | {{new Date().getFullYear()}}
</template>

<style>
  .bg-footer {
    background-image: url(~assets/img/dashboard/footer.svg);
  }
</style>

<script>
import { mapGetters } from 'vuex'
import RigthAside from '@/layouts/aside/RigthAside.vue'
export default {
  components: {
    RigthAside
  },
  data () {
    return {
      right: false
    }
  },
  methods: {
    onLogout () {
      this.$store
        .dispatch('logout')
        .then(() => this.$router.push({ name: 'login' }))
    }
  },
  mounted () {
    if (!this.isAuthenticated) {
      this.$router.push({ name: 'login' })
    }
  },
  computed: {
    ...mapGetters([
      'isAuthenticated'
    ])
  }
}
</script>
