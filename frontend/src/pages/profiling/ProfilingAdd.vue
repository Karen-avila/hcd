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
        h5 ¡Éxito!, estas a punto de enviar los siguientes archivos a perfilar:
        q-item(clickable='', v-ripple='' v-for="file in prflFiles")
          q-item-section(avatar='')
            q-avatar(:color="file.error ? 'negative' : 'positive'", text-color='white', :icon="file.error ? 'close' : 'check' ")
          q-item-section.text-subtitle2 {{file.path.split('/').pop()}}
      template(v-slot:navigation='')
        q-stepper-navigation
          q-btn(@click='$refs.stepper.next()', color='primary', :label="step === 3 ? 'Programar perfilamiento' : 'Continuar'" :disabled="validatorNext()" v-if="step != 3")
          q-btn(color='primary' v-if="step === 3" icon="update" label="Programar perfilamiento" @click="setProfiling")
          q-btn.q-ml-sm(v-if='step > 1', flat='', color='primary', @click='$refs.stepper.goTo(1)', label='Cancelar')
    q-dialog(v-model='dialog', persistent='')
      q-card
        q-card-section.row.items-center
          q-avatar(icon='check', color='primary', text-color='white')
          span.q-ml-lg Tu Perfilamiento se envió con éxito
        q-card-actions(align='right')
          q-btn(flat='', label='Entendido', color='primary', v-close-popup='' :to="{ name: 'profilingList' }")
</template>

<script>
import TreeFiles from '@/pages/components/TreeFiles.vue'
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
