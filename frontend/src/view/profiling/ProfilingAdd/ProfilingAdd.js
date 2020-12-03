import TreeFiles from '@view/components/TreeFiles/TreeFiles.vue'
import HeadersFiles from '@view/profiling/components/HeadersFiles/HeadersFiles.vue'
export default {
  name: 'ProfilingAdd',
  components: {
    TreeFiles,
    HeadersFiles
  },
  data () {
    return {
      step: 1,
      selected: [],
      prflFiles: [],
      path: '/app/static/files/files/',
      dialog: false,
      profilingName: ''
    }
  },
  methods: {
    validateFormProfilingName () {
      if (this.$refs.form.validate()) return 1
      return 0
    },
    validatorNext () {
      if (this.step === 1) {
        if (!this.profilingName || this.profilingName.length <= 3) return true
      }
      if (this.step === 2) {
        if (this.selected.length <= 0) return true
      }
      return false
    },
    reset () {
      this.selected = []
      this.prflFiles = []
    },
    beforeTransition (newStep, oldStep) {
      if (newStep === 1) {
        this.reset()
      }
      if (newStep === 3 && oldStep === 2) {
        this.prflFiles = this.selected.map(file => {
          return {
            path: file,
            headers: [],
            data: [],
            error: null,
            haveHeaders: true,
            separator: ',',
            codification: 'Latin1'
          }
        })
      }
    },
    async setProfiling () {
      let inputfiles = ''
      await this.prflFiles.map(async file => {
        let headersTypes = ''
        await file.headers.map(header => {
          if (header.type) {
            headersTypes += `{
              dataType: "${header.type.id}"
              index: ${header.field}
              headerName: "${header.label}"
            },`
          }
          return null
        })
        if (!file.error) {
          inputfiles += `
          {
            filename: "${file.path}"
            sep: "${file.separator}"
            encoding: "${file.codification}"
            haveHeaders: ${file.haveHeaders}
            datatypes: [${headersTypes}]
          },`
        }
        return null
      })
      this.$apollo
        .mutate({
          mutation: this.$gql`
            mutation{
              prflSetProfiling(
                name: "${this.profilingName}"
                files:[
                  ${inputfiles}
                ]
              ){
                id
              }
            }
          `
        }).then(({ data }) => {
          this.runProfiling(data.prflSetProfiling.id)
          this.dialog = true
        }).catch((error) => {
          console.error('ProfilingAdd, setProfiling: ', error)
        })
    },
    runProfiling (id) {
      this.$apollo
        .mutate({
          mutation: this.$gql`
            mutation{
              prflRunProfiling(profilingid: "${id}") {
                id
              }
            }
          `
        }).then(({ data }) => {
        }).catch((error) => {
          console.error('ProfilingAdd, setProfiling: ', error)
        })
    }
  }
}
