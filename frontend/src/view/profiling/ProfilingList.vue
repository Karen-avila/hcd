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
    q-table.q-mt-lg(
      row-key='id'
      bordered=false
      flat=true
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
          q-td(
            v-for='col in props.cols'
            :key='col.name'
            :props='props'
          ) {{ col.value }}
        q-tr(
          v-show='props.expand'
          :props='props'
        )
          q-td.bg-grey-3(
            colspan='100%'
          )
            router-link(
              v-for="file in props.row.getProfilingFiles"
              :to='{ name: "profilingFileView", params: { Id: file.id }}'
            )
              p(
              ) {{ file.filename }}

</template>

<script>
export default {
  name: 'ProfilingList',
  data () {
    return {
      columns: [
        { name: 'id', label: 'Folio', field: 'id', style: 'width: 10px' },
        { name: 'name', label: 'Nombre', field: 'name' },
        { name: 'status', label: 'Status', field: 'status' },
        { name: 'getLenProfilingFiles', label: 'No de archivos', field: 'getLenProfilingFiles' },
        { name: 'creationDateTime', label: 'Creación', field: 'creationDateTime' },
        { name: 'initialDateTime', label: 'Inicio', field: 'initialDateTime' },
        { name: 'finalDateTime', label: 'Termino', field: 'finalDateTime' }
      ],
      dataTable: []
    }
  },
  mounted () {
    this.getMyProfilings()
  },
  methods: {
    getMyProfilings () {
      this.$apollo
        .query({
          query: this.$gql`
            query{
              prflProfilingQuery(
                first: 10
              ) {
                edges {
                  node {
                    id
                    creationDateTime
                    initialDateTime
                    finalDateTime
                    getLenProfilingFiles
                    getProfilingFiles {
                      id
                      filename
                    }
                  }
                }
              }
            }
          `
        }).then(({ data }) => {
          this.dataTable = data.prflProfilingQuery.edges.map(item => {
            item.node.creationDateTime = item.node.creationDateTime ? this.$moment(item.node.creationDateTime).format('LL') : '-'
            item.node.finalDateTime = item.node.finalDateTime ? this.$moment(item.node.finalDateTime).format('LL') : '-'
            item.node.initialDateTime = item.node.initialDateTime ? this.$moment(item.node.initialDateTime).format('LL') : '-'
            return item.node
          })
        }).catch((error) => {
          console.error('ProfilingList, getMyProfilings: ', error)
        })
    }
  }
}
</script>
