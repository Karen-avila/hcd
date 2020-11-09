<template lang='pug'>
  div
    q-breadcrumbs.text-primary.q-pa-sm(active-color='primary')
      template(v-slot:separator='')
        q-icon(size='1.2em', name='arrow_forward', color='accent')
      q-breadcrumbs-el(label='Inicio', icon='home', :to="{ name: 'dashboard'}")
      q-breadcrumbs-el(label='Perfilamiento', icon='widgets' :to="{ name: 'profilingList'}")
      q-breadcrumbs-el.text-weight-bolder(label='NUEVO PERFILAMIENTO')
    q-stepper(
      v-model='step'
      ref='stepper'
      color='primary'
      animated=true
      done-color="primary"
      active-color="primary"
      inactive-color="secondary"
      @before-transition='beforeTransition'
      flat=true
    )
      q-step(
        :name='1'
        title='SELECCIÓN'
        caption='de archivos'
        icon='create_new_folder'
        :done='step > 1'
      )
        p.text-h6 Selecciona 1 o mas archivo
        span Seleccionados ({{selected.length}}):
        q-badge.q-ml-xs(
          align='middle'
          v-for="file in selected"
          v-bind:data="file"
          v-bind:key="file"
        ) {{file.split('/').pop()}}
        TreeFiles.q-mt-md(
          :selected.sync="selected"
          :path="path"
        )
      q-step(
        :name='2'
        title='VALIDA'
        caption='Revisa las cabeceras'
        icon='file_copy'
        :done='step > 2'
      )
        template(v-if='prflFiles.length > 0')
          p.text-h6 Configura las cabeceras y tipos de dato
          HeadersFiles(
            v-for='(file, index) in prflFiles'
            v-bind:data="file"
            v-bind:key="file.path"
            :file.sync="file"
            :index="index"
          )
      q-step(
        :name='3'
        title='Programa'
        caption='Hora de procesamiento'
        icon='update'
      )
        span {{prflFiles}}
        q-btn(
          ref="btnSetProfiling"
          color='primary'
          size='md'
          @click="setProfiling"
        )
          q-icon(left='', size='2em', name='update')
          div Programar perfilamiento
      template(v-slot:navigation='')
        q-stepper-navigation
          q-btn(@click='$refs.stepper.next()', color='primary', :label="step === 3 ? 'Programar perfilamiento' : 'Continuar'" :disabled="validatorNext()")
          q-btn.q-ml-sm(v-if='step > 1', flat='', color='primary', @click='$refs.stepper.previous()', label='Regresar')
</template>

<script>
import TreeFiles from '@/pages/components/TreeFiles.vue'
import HeadersFiles from './components/HeadersFiles.vue'
export default {
  name: 'profilingAdd',
  components: {
    TreeFiles,
    HeadersFiles
  },
  data () {
    return {
      step: 1,
      selected: [],
      prflFiles: [],
      path: '/app/temp/files'
    }
  },
  methods: {
    validatorNext () {
      if (this.step === 1) {
        if (this.selected.length <= 0) return true
      }
      if (this.step === 2) {
        // this.profilingFiles.find(file => file.headers.length > 0)
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
      // this.$refs.btnSetProfiling.disable = true
      let inputfiles = ''
      await this.prflFiles.map(file => {
        if (!file.error) {
          inputfiles += `{
            filename: "${file.path}"
            sep: "${file.separator}"
            encoding: "${file.codification}"
            haveHeaders: "${file.haveHeaders}"
          },`
        }
      })
      this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
              prflSetProfiling(
                files:[${inputfiles}]
              ){
                id
              }
            }`
        }).then(({ data }) => {
          console.log(data)
        }).catch((error) => {
          console.error('ProfilingAdd, setProfiling: ', error)
        })
    }
  }
}
</script>
