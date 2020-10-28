<template lang='pug'>
  div
    template(v-if="file.headers.length < 1 && !error")
      q-spinner.q-mr-md(color='primary', size='1rem', :thickness='10')
      span.q-mr-sm Descargando:
      span.text-weight-bold {{file.path.split('/').pop()}}
    template(v-if="file.headers.length > 1 && !error")
      p
        span.text-weight-bold {{file.path.split('/').pop()}}
        q-toggle(
          :label='`${file.haveHeaders ? "Tiene encabezados" : "No tiene encabezados"}`'
          v-model='file.haveHeaders'
        )
      q-table.q-mt-lg(
        dense=true
        bordered=false
        flat=true
        title=''
        :data='data'
        :columns='columns'
        row-key='name'
        :separator='separator'
        hide-bottom=true,
        virtual-scroll
      )
    template(v-if="error")
      p.text-weight-bold {{file.path.split('/').pop()}}
      p.text-negative Error: {{error}}
      q-form()
        .q-pb-md
          .q-gutter-md.row.items-start
            q-input(
              clearable=''
              label='Separador'
              clear-icon='close'
              dense=true
              v-model='file.separator'
            )
            q-input(
              clearable=''
              label='Codificación'
              clear-icon='close'
              dense=true
              v-model='file.codification'
            )
        div
          q-btn.q-mr-md(
            label='Descargar de nuevo'
            type='button'
            color='primary'
            @click='getHeaders()'
            size="sm"
          )
          q-btn(
            label='Eliminar'
            type='button'
            color='negative'
            @click='getHeaders()'
            size="sm"
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
      separator: 'vertical',
      columns: [],
      error: false,
      data: []
    }
  },
  mounted () {
    this.getHeaders()
  },
  methods: {
    getHeaders () {
      this.error = false
      const sep = this.file.separator ? `sep: "${this.file.separator}"` : ''
      const encoding = this.file.encoding ? `encoding: "${this.file.codification}"` : ''
      return this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
              qudaFileGetHeaders(
                filename: "${this.file.path}"
                ${sep}
                ${encoding}
              )
            }`
        }).then(({ data }) => {
          this.file.headers = data.qudaFileGetHeaders
          this.columns = this.file.headers.map(header => {
            return {
              name: header,
              align: 'center',
              label: header,
              field: header,
              sortable: false
            }
          })
          return data
        }).catch((error) => {
          this.error = 'Error: No se pudo abrir el archivo, intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    }
  },
  watch: {
    'file.haveHeaders' (value) {
      this.$emit('update:selectedFiles', value)
    }
  }
}
</script>
