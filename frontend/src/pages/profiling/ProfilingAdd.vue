<template lang='pug'>
  .q-pa-md
    q-breadcrumbs.text-grey(active-color='primary')
      template(v-slot:separator='')
        q-icon(size='1.2em', name='arrow_forward', color='accent')
      q-breadcrumbs-el(label='Inicio', icon='home', :to="{ name: 'dashboard'}")
      q-breadcrumbs-el(label='Perfilamiento', icon='widgets' :to="{ name: 'profilingList'}")
      q-breadcrumbs-el(label='Agregar')
    .row
      .q-pa-md.col-12
        q-card.my-card
          q-card-section.bg-primary.text-white
            .text-h6 Nuevo Perfilamiento
              // router-link(:to="{ name: 'dashboard'}")
                q-btn.float-right(color='secondary')
                  q-icon(left='', size='2em', name='add')
                  div NUEVO PERFILAMIENTO
            .text-subtitle2 ambiente Desarrollo
          q-separator
          q-stepper(
            v-model='step'
            ref='stepper'
            color='primary'
            animated=''
            @before-transition='beforeTransition'
          )
            q-step(
              :name='1'
              title='SELECCIONA'
              caption='Elige 1 o mas archivos'
              icon='create_new_folder'
              :done='step > 1'
            )
              p Archivos seleccionados ({{selectedFiles.length}}):
                span.text-weight-bolder
                  template(v-for="file in selectedFiles")
                    span.q-pa-xs {{file.split('/').pop()}}
              p.text-weight-bold Selecciona uno o más archivos de la lista:
              q-card.bg-blue-grey-1(flat=true, )
                TreeFiles.q-pa-md(
                  :selectedFiles.sync="selectedFiles"
                  :path="path"
                )
            q-step(
              :name='2'
              title='VALIDA'
              caption='Revisa las cabeceras'
              icon='file_copy'
              :done='step > 2'
            )
              template(v-if='profilingFiles.length > 0')
                q-card.bg-grey-2.q-mb-md(
                  flat=true
                  bordered=true
                  v-for='(file, index) in profilingFiles'
                  v-bind:data="file"
                  v-bind:key="file.path"
                )
                  q-card-section
                    HeadersFiles(
                      :file.sync="file"
                      :index.sync="index"
                    )
            q-step(:name='3', title='Ad template', icon='create_new_folder', disable='')
              | This step won't show up because it is disabled.
            q-step(:name='4', title='Create an ad', icon='add_comment')
              | Try out different ad text to see what brings in the most customers, and learn how to
              | enhance your ads using features like ad extensions. If you run into any problems with
              | your ads, find out how to tell if they're running and how to resolve approval issues.
            template(v-slot:navigation='')
              q-stepper-navigation
                q-btn(@click='$refs.stepper.next()', color='primary', :label="step === 4 ? 'Finish' : 'Continuar'" :disabled="validatorNext()")
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
      selectedFiles: [],
      profilingFiles: [],
      path: '/app/temp/'
    }
  },
  methods: {
    validatorNext () {
      if (this.step === 1) {
        if (this.selectedFiles.length > 0) return false
      }
      return true
    },
    beforeTransition (newStep, oldStep) {
      if (newStep === 2 && oldStep === 1) {
        this.profilingFiles = this.selectedFiles.map(file => {
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
    }
  }
}
</script>
