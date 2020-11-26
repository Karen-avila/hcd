<template lang='pug'>
  include ./ProfilingAdd.pug
</template>

<script>
import TreeFiles from '@view/components/TreeFiles.vue'
import HeadersFiles from './components/HeadersFiles.vue'
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
      dialog: false
    }
  },
  methods: {
    validatorNext () {
      if (this.step === 1) {
        if (this.selected.length <= 0) return true
      }
      return false
    },
    beforeTransition (newStep, oldStep) {
      if (newStep === 2 && oldStep === 1) {
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
                files:[
                  ${inputfiles}
                ]
              ){
                id
              }
            }
          `
        }).then(({ data }) => {
          this.dialog = true
        }).catch((error) => {
          console.error('ProfilingAdd, setProfiling: ', error)
        })
    }
  }
}
</script>
