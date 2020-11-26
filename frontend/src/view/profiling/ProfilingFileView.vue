<template lang='pug'>
  div.q-pa-md
    // BREADCRUMBS
    q-breadcrumbs.text-primary(
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
      q-breadcrumbs-el(
        label='Archicho de Perfilamiento'
        icon='widgets'
        :to='{ name: "profilingList"}'
      )
      q-breadcrumbs-el.text-weight-medium(
      )
    | {{profilingFile.variables}}
</template>

<script>
export default {
  name: 'ProfilingFileView',
  data () {
    return {
      profilingFile: null
    }
  },
  mounted () {
    this.getProfilingFile()
  },
  methods: {
    getProfilingFile () {
      this.$apollo
        .mutate({
          mutation: this.$gql`
            mutation {
              prflProfilingFile(id: "${this.$route.params.Id}") {
                id
                filename
                sep
                encoding
                haveHeaders
                analysis
                variables
                scatter
              }
            }
          `
        }).then(({ data }) => {
          this.profilingFile = data.prflProfilingFile
          console.log(JSON.parse(this.profilingFile.variables))
        })
    }
  }
}
</script>
