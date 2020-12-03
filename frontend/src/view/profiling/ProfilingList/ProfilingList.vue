<template lang='pug'>
  div
    q-breadcrumbs.text-primary.q-pa-sm(
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
      q-breadcrumbs-el.text-weight-medium(
        label='PERFILAMIENTOS'
      )
      q-space
      router-link(
        :to='{ name: "profilingAdd"}'
      )
        q-btn.float-right(
          color='accent'
          size='md'
          outline=''
        )
          q-icon(
            left=''
            size='2em'
            name='add'
          )
          div(
          ) NUEVO PERFILAMIENTO
    q-table.q-mt-sm(
      row-key='id'
      bordered=false
      flat=true
      rows-per-page-label=50
      :rows-per-page-options='[25, 50, 100]'
      :data='dataTable'
      :columns='columns'
    )
      template(
        v-slot:header='props'
      )
        q-tr(
          :props='props'
        )
          q-th(
            auto-width=''
          )
          q-th(
            v-for='col in props.cols'
            :key='col.name'
            :props='props'
          ) {{ col.label }}
      template(
        v-slot:body='props'
      )
        q-tr(
          :props='props'
        )
          q-td(
            auto-width=''
          )
            q-btn(
              size='sm'
              color='secondary'
              round=''
              dense=''
              :icon='props.expand ? "remove" : "add"'
              @click='props.expand = !props.expand'
            )
          q-td.cursor-pointer(
            v-for='col in props.cols'
            :key='col.name'
            :props='props'
            @click='props.expand = !props.expand'
          )
            span(
              v-if='col.field.includes("DateTime")'
            ) {{col.value | DateTime}}
            span(
              v-else
            ) {{col.value}}
        q-tr(
          v-show='props.expand'
          :props='props'
        )
          q-td.bg-grey-3(
            colspan='100%'
          )
            q-markup-table.q-my-md.transparent(
              flat=true
              bordered=false
              dense=true
            )
              thead
                tr
                  th.text-right Nombre del archivo
                  th.text-right Status
                  th.text-right Fecha/Hora de inicio
                  th.text-right Fecha/Hora de terminado
                  th.text-center Acciones
              tbody
                tr(
                  v-for="file in props.row.getProfilingFiles"
                )
                  td.text-right {{file.filename.split('/').pop()}}
                  td.text-right {{file.getStatus}}
                  td.text-right {{file.initialDateTime | DateTime}}
                  td.text-right {{file.finalDateTime | DateTime}}
                  td.text-center
                    q-btn(
                      outline=''
                      color='primary'
                      label='Ver resultados'
                      size='sm'
                      icon='description'
                      :disabled='!file.finalDateTime'
                      :to='{name:"profilingFileView", params: {Id:file.id}}'
                    )
</template>

<script src='./ProfilingList.js'></script>
