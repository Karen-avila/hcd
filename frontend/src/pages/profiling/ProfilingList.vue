<template lang='pug'>
  div
    q-breadcrumbs.text-grey.q-pa-sm(active-color='primary')
      template(v-slot:separator='')
        q-icon(size='1.2em', name='arrow_forward', color='accent')
      q-breadcrumbs-el(label='Inicio', icon='home', :to="{ name: 'dashboard'}")
      q-breadcrumbs-el.text-weight-bolder(label='PERFILAMIENTOS')
      q-space
      router-link(:to="{ name: 'profilingAdd'}")
        q-btn.float-right(
          color='secondary'
          size='md'
        )
          q-icon(left='', size='2em', name='add')
          div NUEVO PERFILAMIENTO
    q-table.q-mt-lg(
      :data='data'
      :columns='columns'
      row-key='name'
      bordered=false
      flat=true
    )
      template(v-slot:header='props')
        q-tr(:props='props')
          q-th(auto-width='')
          q-th(v-for='col in props.cols', :key='col.name', :props='props')
            | {{ col.label }}
      template(v-slot:body='props')
        q-tr(:props='props')
          q-td(auto-width='')
            q-btn(
              size='sm'
              color='secondary'
              round=''
              dense=''
              @click='props.expand = !props.expand'
              :icon="props.expand ? 'remove' : 'add'"
            )
          q-td(v-for='col in props.cols', :key='col.name', :props='props')
            | {{ col.value }}
        q-tr(v-show='props.expand', :props='props')
          q-td(colspan='100%')
            .text-left This is expand slot for row above: {{ props.row.name }}.
</template>

<script>
export default {
  name: 'profilingList',
  data () {
    return {
      columns: [
        { name: 'id', label: 'Folio', field: 'id', style: 'width: 10px' },
        { name: 'name', label: 'Nombre', field: 'name' },
        { name: 'status', label: 'Status', field: 'status' },
        { name: 'fileLength', label: 'No de archivos', field: 'fileLength' },
        { name: 'creationDateTime', label: 'Creación', field: 'creationDateTime' },
        { name: 'initalDateTime', label: 'Inicio', field: 'initalDateTime' },
        { name: 'finalDateTime', label: 'Termino', field: 'finalDateTime' }
      ],
      data: [
        {
          id: 'Frozen Yogurt',
          name: 'Frozen Yogurt',
          status: 159,
          fileLength: 6.0,
          creationDateTime: 24,
          initalDateTime: 4.0,
          finalDateTime: 87
        }
      ]
    }
  }
}
</script>
