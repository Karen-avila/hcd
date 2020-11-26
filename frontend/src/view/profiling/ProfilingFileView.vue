<template lang='pug'>
  div
    q-breadcrumbs.text-primary.q-pa-sm(
      active-color='primary'
    )
      template(
        v-slot:separator=''
      )
        q-icon(
          size='1.2em'
          name='arrow_forward'
          color='accent'
        )
      q-breadcrumbs-el(
        label='Inicio'
        icon='home'
        :to='{ name: "dashboard"}'
      )
      q-breadcrumbs-el.text-weight-bolder(
        label='ARCHIVO DE PERFILAMIENTO'
      )
</template>

<script>
export default {
  name: 'ProfilingFileView',
  components: {},
  data () {
    return {}
  },
  methods: {
  }
}
</script>
