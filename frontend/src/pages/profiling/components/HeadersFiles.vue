<template lang='pug'>
  div
    template(
      v-if="file.headers.length < 1 && file.data.length < 1 && !file.error"
    )
      q-toolbar.bg-grey.text-white.rounded-borders.q-mb-md.q-px-xl
        q-spinner.q-mr-md(color='white', size='1rem', :thickness='10')
        span Descargando: {{file.path.split('/').pop()}}
    template(
      v-if="file.headers.length > 1 && file.data.length > 1 && !file.error"
    )
      q-toolbar.bg-secondary.text-white.rounded-borders
        span {{file.path.split('/').pop()}}
        q-space
        q-toggle.q-mr-md(
          :label='`${file.haveHeaders ? "Sin encabezados" : "Con tiene encabezados"}`'
          v-model='file.haveHeaders'
          color="white"
          left-label
        )
        q-tabs(v-model='tab', shrink='', stretch='')
          q-tab(name="table" label="" icon="table_view")
            q-tooltip(content-class='bg-accent' anchor="top middle" self="bottom middle") Ver Tabla
          q-tab(name="type" label="" icon="spellcheck")
            q-tooltip(content-class='bg-accent' anchor="top middle" self="bottom middle") Forzar datos
      q-card.card-file.bg-grey-2.q-mt-sm.q-mb-lg
        q-table.bg-grey-2(
          v-if="tab === 'table'"
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
        q-card-section(
          v-if="tab === 'type' && dataTypes.length > 0"
        )
          p Puedes elegir una opción para forzar el perfilamiento a ese tipo de dato
          .row
            .col-md-6.q-pa-xs(v-for="header in file.headers")
              q-select(
                dense=true
                filled=''
                v-model='header.type'
                :options='dataTypes'
                :label='header.label'
              )
    template(
      v-if="file.error"
      align="center"
    )
      q-toolbar.bg-accent.text-white.rounded-borders
        span {{file.path.split('/').pop()}}
        q-space
        span {{file.error}}
      q-card.card-file.bg-grey-2.q-mt-xs.q-mb-lg
        .absolute-center
          q-form.q-gutter-md.row
            q-input(
              clearable=''
              label='Separador'
              clear-icon='close'
              v-model='file.separator'
              dense=true
            )
            q-input(
              clearable=''
              label='Codificación'
              clear-icon='close'
              v-model='file.codification'
              dense=true
            )
          .row.q-mt-md
            q-btn(
              label='Descargar de nuevo'
              type='button'
              color='primary'
              @click='updateTable'
            )
            q-btn.q-ml-lg(
              label=''
              icon="delete"
              type='button'
              color='negative'
                )
</template>

<style lang="sass" scoped>
.card-file
  min-height: 160px
</style>

<script>
export default {
  name: 'HeaderFiles',
  props: [
    'file',
    'index'
  ],
  data () {
    return {
      tab: 'table',
      dataTypes: []
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
      await this.getOptions()
    },
    async getHeaders () {
      await this.$apollo
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
          this.file.error = null
          this.file.headers = data.qudaFileGetHeaders.map((header, index) => {
            return {
              align: 'center',
              label: header,
              field: index,
              type: null
            }
          })
        }).catch((error) => {
          this.file.error = 'Intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    },
    async getSamples () {
      await this.$apollo
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
          this.file.error = null
          this.file.data = data.qudaFileGetSamples.map(row => {
            const dict = {}
            row.map((field, i) => {
              dict[i] = field
            })
            return dict
          })
        }).catch((error) => {
          this.file.error = 'Intenta de nuevo cambiando la separacion o la codificación'
          console.error('ProfilingAdd, getSamples: ', error)
        })
    },
    async getOptions () {
      this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
            qudaDataTypeQuery(
              after: "DataTypeNode:0"
              isDefault: true
            ) {
              edges {
                node {
                  id
                  name
                  code
                }
              }
            }
          }`
        }).then(({ data }) => {
          this.dataTypes = data.qudaDataTypeQuery.edges.map(edge => {
            return {
              label: edge.node.name,
              value: edge.node.code
            }
          })
        }).catch((error) => {
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    }
  },
  watch: {
    'file.haveHeaders' (value) {
      this.getHeaders()
    },
    'file.headers' (values) {
      this.$emit('update:file', values)
    }
  }
}
</script>
