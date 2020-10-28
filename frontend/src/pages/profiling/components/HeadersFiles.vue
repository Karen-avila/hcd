<template lang='pug'>
  div
    template(v-if="file.headers.length < 1 && file.data.length < 1 && !file.error")
      q-spinner.q-mr-md(color='primary', size='1rem', :thickness='10')
      span.q-mr-sm Descargando:
      span.text-weight-bold {{file.path.split('/').pop()}}
    template(v-if="file.headers.length > 1 && file.data.length > 1 && !file.error")
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
        :data='this.file.data'
        :columns='this.file.headers'
        row-key='name'
        separator='vertical'
        hide-bottom=true,
        virtual-scroll
      )
    template(v-if="file.error")
      span.text-negative {{this.file.error}}
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
            @click='updateTable()'
          )
</template>

<script>
export default {
  name: 'HeaderFiles',
  props: [
    'file',
    'index'
  ],
  data () {
    return {
    }
  },
  mounted () {
    setTimeout(() => {
      this.updateTable()
    }, (this.index + 1) * 1000)
  },
  methods: {
    async updateTable () {
      await this.getHeaders()
      await this.getSamples()
    },
    getHeaders () {
      this.file.error = null
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
          this.file.headers = data.qudaFileGetHeaders.map((header, index) => {
            return {
              align: 'center',
              label: header,
              field: index
            }
          })
        }).catch((error) => {
          this.file.error = 'Error: No se pudo abrir el archivo, intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    },
    getSamples () {
      this.file.error = null
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
          this.file.data = data.qudaFileGetSamples.map(row => {
            const dict = {}
            row.map((field, i) => {
              dict[i] = field
            })
            return dict
          })
        }).catch((error) => {
          this.file.error = 'Error: No se pudo abrir el archivo, intenta de nuevo cambiando la separacion o la codificación'
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
