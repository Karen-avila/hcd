import RealNumberCard from '@view/profiling/components/RealNumberCard/RealNumberCard.vue'
export default {
  name: 'ProfilingFileView',
  components: {
    RealNumberCard
  },
  data () {
    return {
      variables: null
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
          this.variables = JSON.parse(data.prflProfilingFile.variables)
        })
    }
  }
}
