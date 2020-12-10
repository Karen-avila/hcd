import RealNumberCard from '@view/profiling/components/RealNumberCard/RealNumberCard.vue'
import BooleanCard from '@view/profiling/components/BooleanCard/BooleanCard.vue'
import CategoricalCard from '@view/profiling/components/CategoricalCard/CategoricalCard.vue'
import DateCard from '@view/profiling/components/DateCard/DateCard.vue'
import UrlCard from '@view/profiling/components/UrlCard/UrlCard.vue'
export default {
  name: 'ProfilingFileView',
  components: {
    RealNumberCard,
    BooleanCard,
    CategoricalCard,
    DateCard,
    UrlCard
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
          console.log(JSON.parse(data.prflProfilingFile.variables))
        })
    }
  }
}
