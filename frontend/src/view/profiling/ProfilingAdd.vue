<template lang='pug'>
div.q-pa-md
  // BREADCRUMBS
  q-breadcrumbs.text-primary(
    active-color='primary'
  )
    template(
      v-slot:separator=''
    )
      q-icon(
        size='1.2em'
        name='arrow_forward'
        color='accent'
      )
    q-breadcrumbs-el(
      label='Inicio'
      icon='home'
      :to='{ name: "dashboard"}'
    )
    q-breadcrumbs-el(
      label='Perfilamiento'
      icon='widgets'
      :to='{ name: "profilingList"}'
    )
    q-breadcrumbs-el.text-weight-medium(
      label='NUEVO'
    )
  // STEPPER
  q-stepper(
    v-model='step'
    ref='stepper'
    color='primary'
    done-color='primary'
    active-color='primary'
    inactive-color='secondary'
    animated=true
    flat=true
    vertical=true
    @before-transition='beforeTransition'
  )
    // STEP 1
    q-step(
      title='SELECCIÓN'
      caption='de archivos'
      icon='create_new_folder'
      :name='1'
      :done='step > 1'
    )
      p.text-h6 Selecciona 1 o mas archivo
      span Seleccionados ({{selected.length}}):
      q-badge.q-mx-xs(
        v-for='file in selected'
        v-bind:data='file'
        v-bind:key='file'
        align='middle'
      ) {{file.split('/').pop()}}
      TreeFiles.q-mt-md(
        :selected.sync='selected'
        :path='path'
      )
    // STEP 2
    q-step(
      title='VALIDA'
      caption='Revisa las cabeceras'
      icon='file_copy'
      :name='2'
      :done='step > 2'
    )
      template(
        v-if='prflFiles.length > 0'
      )
        p.text-h6 Configura las cabeceras y tipos de dato
        HeadersFiles(
          v-for='(file, index) in prflFiles'
          v-bind:data='file'
          v-bind:key='file.path'
          :File.sync='file'
          :Index.sync='index'
        )
    // STEP 3
    q-step(
      title='Programa'
      caption='Hora de procesamiento'
      icon='update'
      :name='3'
    )
      h5 ¡Éxito!, estas a punto de enviar los siguientes archivos a perfilar
      q-item(
        v-for='file in prflFiles'
        clickable=''
        v-ripple=''
      )
        q-item-section(
          avatar=''
        )
          q-avatar(
            text-color='white'
            :color='file.error ? "negative" : "positive"'
            :icon='file.error ? "close" : "check"'
          )
        q-item-section.text-subtitle2(
        ) {{file.path.split('/').pop()}}
    // BUTTONS STEPPER
    template(
      v-slot:navigation=''
    )
      q-stepper-navigation
        q-btn(
          v-if='step != 3'
          outline=''
          color='accent'
          @click='$refs.stepper.next()'
          :label='step === 3 ? "Programar perfilamiento" : "Continuar"'
          :disabled='validatorNext()'
        )
        q-btn(
          v-if='step === 3'
          outline=''
          color='primary'
          icon='update'
          label='Programar perfilamiento'
          @click='setProfiling'
        )
        q-btn.q-ml-sm(
          v-if='step > 1'
          color='gray-8'
          label='Cancelar'
          outline=''
          flat=''
          @click='$refs.stepper.goTo(1)'
        )
  // DIALOG
  q-dialog(
    v-model='dialog'
    persistent=''
  )
    q-card.q-pa-md
      q-card-section.row.items-center
        q-avatar(
          icon='check'
          color='primary'
          text-color='white'
        )
        span.q-ml-lg(
        ) Tu Perfilamiento se envió con éxito
      q-card-actions(
        align='right'
      )
        q-btn(
          outline=''
          label='Entendido'
          color='primary'
          v-close-popup=''
          :to='{name:"profilingList"}'
        )
</template>

<script>
import TreeFiles from '@view/components/TreeFiles.vue'
import HeadersFiles from './HeadersFiles.vue'
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
