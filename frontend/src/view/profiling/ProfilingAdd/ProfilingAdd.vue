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
      label='Perfilamientos'
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
    vertical=false
    @before-transition='beforeTransition'
  )
    // STEP 1
    q-step(
      title='NUEVO'
      caption='perfilamiento'
      icon='create_new_folder'
      :name='1'
      :done='step > 1'
    )
      p.text-h6 Estas a punto de programar un perfilamiento
      q-form(
        ref='form'
        lazy-validation=''
        style='max-width:800px;'
      )
        q-input(
          outlined=true
          v-model='profilingName'
          label='Nombre del perfilamiento'
          hint='Ingresa el nombre con el que identificarás este perfilamiento'
          lazy-rules=''
          :rules="[ val => val && val.length > 2 || 'Ingresa un nombre mayor a 3 caracteres']"
        )
    // STEP 2
    q-step(
      title='SELECCIÓN'
      caption='de archivos'
      icon='create_new_folder'
      :name='2'
      :done='step > 2'
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
    // STEP 3
    q-step(
      title='VALIDA'
      caption='Revisa las cabeceras'
      icon='file_copy'
      :name='3'
      :done='step > 3'
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
          :PrflFiles.sync='prflFiles'
        )
    // STEP 4
    q-step(
      title='Programa'
      caption='Hora de procesamiento'
      icon='update'
      :name='4'
    )
      h5 ¡Éxito!, estas a punto de enviar los siguientes archivos a perfilar
      q-item(
        v-for='file in prflFiles'
        v-bind:data='file'
        v-bind:key='file.path'
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
          v-if='step != 4'
          outline=''
          color='accent'
          label='Continuar'
          :disabled='validatorNext()'
          @click='$refs.stepper.next()'
        )
        q-btn(
          v-if='step === 4'
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

<script src='./ProfilingAdd.js'></script>
