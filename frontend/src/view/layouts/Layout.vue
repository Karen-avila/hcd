<template lang="pug">
q-layout(
  view='hHh lpR fFr'
)
  q-header.bg-primary(
    elevated=false
    height-hint='98'
  )
    q-toolbar
      q-toolbar-title.text-subtitle1.text-weight-light
        //  q-avatar.q-mr-md
          img(
            src='~assets/img/dashboard/logo.png'
          ) Instituto Mexicano del Seguro Social
      q-btn.q-mr-md(
        flat=''
        round=''
        dense=''
        icon='home'
      )
        q-tooltip(
          content-class='bg-accent'
        ) INICIO
      q-btn.q-mr-md(
        flat=''
        round=''
        dense=''
        icon='account_box'
      )
        q-tooltip(
          content-class='bg-accent'
        ) PERFIL
      q-btn(
        flat=''
        round=''
        dense=''
        icon='login'
        @click='onLogout'
      )
        q-tooltip(
          content-class='bg-accent'
        ) SALIR
      q-btn.q-ml-xl(
        dense=''
        flat=''
        round=''
        icon='menu'
        @click='right = !right'
      )
        q-tooltip(
          content-class='bg-accent'
        ) MENU
    q-toolbar.bg-secondary(
      style="min-height: 5px;"
    )
  q-drawer(
    v-model='right'
    show-if-above=''
    side='right'
    elevated=''
  )
    .full-height.bg-aside-right.drawer_normal
      div.text-white(
        style='height: calc(100% - 117px);padding:10px;'
      )
        q-toolbar
          q-toolbar-title.text-caption(
          ) Bienvenido,
            span.text-weight-bold(
            )  {{currentUser}}
        hr
        q-scroll-area(
          style='height:100%;'
        )
          q-list(
            padding=''
          )
            q-item.navigation-item(
              active-class='tab-active'
              exact=''
              clickable=''
              v-ripple=''
              :to="{ name: 'profilingList' }"
            )
              q-item-section(
                avatar=''
              )
                q-icon(
                  name='dashboard'
                )
              q-item-section(
              ) Perfilamiento
            q-item.navigation-item(
              active-class='tab-active'
              exact=''
              clickable=''
              v-ripple=''
              to='/cleaning'
            )
              q-item-section(
                avatar=''
              )
                q-icon(
                  name='dashboard'
                )
              q-item-section(
              ) Limpieza
  q-page-container
    router-view
  q-footer.bg-footer.text-white
    q-toolbar
      //  span.q-mb-sm(
        ) HERRAMIENTA DE CALIDAD DE DATOS | {{new Date().getFullYear()}}
</template>

<style src='./Layout.sass' lang='sass'></style>

<script>
import { mapGetters } from 'vuex'
export default {
  components: {
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
      'isAuthenticated',
      'currentUser'
    ])
  }
}
</script>
