export default {
  name: 'HeaderFiles',
  props: [
    'File',
    'Index',
    'PrflFiles'
  ],
  data () {
    return {
      tab: 'table',
      dataTypes: [],
      file: this.File,
      index: this.Index,
      prflFiles: this.PrflFiles
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
                ${this.file.haveHeaders ? '' : 'haveHeaders: false'}
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
                ${this.file.haveHeaders ? '' : 'haveHeaders: false'}
              )
            }`
        }).then(({ data }) => {
          this.file.error = null
          this.file.data = data.qudaFileGetSamples.map(row => {
            const dict = {}
            row.map((field, i) => {
              dict[i] = field
              return false
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
        .query({
          query: this.$gql`query{
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
              value: edge.node.code,
              id: edge.node.id
            }
          })
        }).catch((error) => {
          console.error('ProfilingAdd, getHeaders: ', error)
        })
    },
    deleteTable () {
      return this.$delete(this.prflFiles, this.index)
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
