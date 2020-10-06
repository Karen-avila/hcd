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
            .text-subtitle2 por John Doe
          q-separator
          q-stepper(v-model='step', ref='stepper', color='primary', animated='')
            q-step(
              :name='1'
              title='Selecciona un archivo'
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
                )
            q-step(:name='2', title='Create an ad group', caption='Optional', icon='create_new_folder', :done='step > 2')
              | An ad group contains one or more ads which target a shared set of keywords.
            q-step(:name='3', title='Ad template', icon='create_new_folder', disable='')
              | This step won't show up because it is disabled.
            q-step(:name='4', title='Create an ad', icon='add_comment')
              | Try out different ad text to see what brings in the most customers, and learn how to
              | enhance your ads using features like ad extensions. If you run into any problems with
              | your ads, find out how to tell if they're running and how to resolve approval issues.
            template(v-slot:navigation='')
              q-stepper-navigation
                q-btn(@click='$refs.stepper.next()', color='primary', :label="step === 4 ? 'Finish' : 'Continuar'" :disabled="validatorNext()")
                q-btn.q-ml-sm(v-if='step > 1', flat='', color='primary', @click='$refs.stepper.previous()', label='Back')
</template>

<script>
import TreeFiles from '@/components/TreeFiles.vue'
export default {
  name: 'profilingAdd',
  components: {
    TreeFiles
  },
  data () {
    return {
      step: 1,
      selectedFiles: []
    }
  },
  methods: {
    validatorNext () {
      if (this.step === 1) {
        if (this.selectedFiles.length > 0) return false
      }
      return true
    }
  },
  watch: {
    selectedFiles (newValue) {
      console.log(newValue)
    }
  }
}
</script>
