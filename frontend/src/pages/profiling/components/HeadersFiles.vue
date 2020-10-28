<template lang='pug'>
  div
    template(v-if="file.headers.length < 1 && !file.errors")
      q-spinner.q-mr-md(color='primary', size='1rem', :thickness='10')
      span.q-mr-sm Descargando:
      span.text-weight-bold {{file.path.split('/').pop()}}
    template(v-if="file.headers.length > 1 && !file.errors")
      p
        q-toggle.absolute-top-right.q-mr-md(
          :label='`${file.haveHeaders ? "Tiene encabezados" : "No tiene encabezados"}`'
          v-model='file.haveHeaders'
          left-label
        )
        span.text-weight-bold {{file.path.split('/').pop()}}
      q-table.q-mt-lg(
        dense=true
        bordered=false
        flat=true
        title=''
        :data='file.data'
        :columns='file.headers'
        row-key='name'
        separator='vertical'
        hide-bottom=true,
        virtual-scroll
      )
    template(v-if="this.file.errors")
      span.text-negative Error: {{this.file.errors}}
      p.text-weight-bold {{file.path.split('/').pop()}}
      q-form()
        .q-gutter-md.row.items-start
          q-input(
            clearable=''
            label='Separador'
            clear-icon='close'
            v-model='file.separator'
          )
          q-input(
            clearable=''
            label='Codificación'
            clear-icon='close'
            v-model='file.codification'
          )
          q-btn.q-mr-md(
            label='Descargar'
            type='button'
            color='primary'
            @click='getHeaders()'
          )
</template>

<script>
export default {
  name: 'HeaderFiles',
  props: [
    'file'
  ],
  data () {
    return {
    }
  },
  mounted () {
    this.getHeaders()
    this.getSamples()
  },
  methods: {
    getHeaders () {
      this.file.errors = null
      return this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
              qudaFileGetHeaders(
                filename: "${this.file.path}"
                ${this.file.separator ? `sep: "${this.file.separator}"` : ''}
                ${this.file.encoding ? `encoding: "${this.file.codification}"` : ''}
                ${this.file.haveHeaders ? '' : 'header: false'}
              )
            }`
        }).then(({ data }) => {
          this.file.headers = data.qudaFileGetHeaders.map(header => {
            return {
              align: 'center',
              label: header
            }
          })
        }).catch((error) => {
          this.file.errors = 'Error: No se pudo abrir el archivo, intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    },
    getSamples () {
      this.file.errors = null
      return this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
              qudaFileGetSamples(
                filename: "${this.file.path}"
                ${this.file.separator ? `sep: "${this.file.separator}"` : ''}
                ${this.file.encoding ? `encoding: "${this.file.codification}"` : ''}
                ${this.file.haveHeaders ? '' : 'header: false'}
              )
            }`
        }).then(({ data }) => {
          this.file.data = data.qudaFileGetSamples
          console.log(data.qudaFileGetSamples)
        }).catch((error) => {
          // this.file.errors = 'Error: No se pudo abrir el archivo, intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getSamples: ', error)
        })
    }
  },
  watch: {
    'file.haveHeaders' (value) {
      this.getHeaders()
    }
  }
}
</script>
