export default {
  name: 'ProfilingList',
  data () {
    return {
      columns: [
        { name: 'id', label: 'Folio', field: 'id', style: 'width: 10px' },
        { name: 'name', label: 'Nombre', field: 'name' },
        { name: 'getStatus', label: 'Status', field: 'getStatus' },
        { name: 'getLenProfilingFiles', label: 'No de archivos', field: 'getLenProfilingFiles' },
        { name: 'creationDateTime', label: 'Creación', field: 'creationDateTime' },
        { name: 'initialDateTime', label: 'Inicio', field: 'initialDateTime' },
        { name: 'finalDateTime', label: 'Termino', field: 'finalDateTime' }
      ],
      dataTable: []
    }
  },
  mounted () {
    this.getMyProfilings()
  },
  methods: {
    getMyProfilings () {
      this.$apollo
        .query({
          query: this.$gql`
            query{
              prflProfilingQuery(
                first: 10
              ) {
                edges {
                  node {
                    id
                    name
                    creationDateTime
                    initialDateTime
                    finalDateTime
                    getLenProfilingFiles
                    getStatus
                    getProfilingFiles {
                      id
                      filename
                      initialDateTime
                      finalDateTime
                      getStatus
                    }
                  }
                }
              }
            }
          `
        }).then(({ data }) => {
          this.dataTable = data.prflProfilingQuery.edges.map((item) => {
            return item.node
          })
        }).catch((error) => {
          console.error('ProfilingList, getMyProfilings: ', error)
        })
    }
  }
}
