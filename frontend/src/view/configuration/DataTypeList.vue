<template lang='pug'>
  div
    q-breadcrumbs.text-primary.q-pa-sm(active-color='primary')
      template(v-slot:separator='')
        q-icon(size='1.2em', name='arrow_forward', color='accent')
      q-breadcrumbs-el(label='Inicio', icon='home', :to="{ name: 'dashboard'}")
      q-breadcrumbs-el.text-weight-bolder(label='TIPOS DE DATO')
      q-space
      router-link(:to="{ name: 'profilingAdd'}")
        q-btn.float-right(
          color='secondary'
          size='md'
        )
          q-icon(left='', size='2em', name='add')
          div NUEVO TIPO DE DATO
    q-table.q-mt-lg(
      :data='dataTable'
      :columns='columns'
      row-key='name'
      flat=true
      bordered=false
    )
</template>

<script>
export default {
  name: 'profilingList',
  data () {
    return {
      columns: [
        // {
        //   name: 'name',
        //   required: true,
        //   label: 'Dessert (100g serving)',
        //   align: 'left',
        //   field: row => row.name,
        //   format: val => `${val}`,
        //   sortable: true
        // },
        { name: 'name', align: 'center', label: 'Nombre', field: 'name' },
        { name: 'isValid', align: 'center', label: 'Es Valido?', field: 'isValid', format: val => `${val ? 'Válido' : 'Inválido'}` }
      ],
      dataTable: []
    }
  },
  mounted () {
    this.getDataTypes()
  },
  methods: {
    getDataTypes () {
      this.$apollo
        .query({
          query: this.$gql`query{
            qudaDataTypeQuery(
              after: "DataTypeNode:0"
              isDefault: true
            ) {
              edges {
                node {
                  id
                  name
                  code
                  isValid
                }
              }
            }
          }`
        }).then(({ data }) => {
          this.dataTable = data.qudaDataTypeQuery.edges.map(item => {
            return item.node
          })
        }).catch((error) => {
          console.error('DataTypeList, getDataTypes: ', error)
        })
    }
  }
}
</script>
