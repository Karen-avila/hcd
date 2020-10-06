<template lang='pug'>
  .q-pa-md
    q-breadcrumbs.text-grey(active-color='primary')
      template(v-slot:separator='')
        q-icon(size='1.2em', name='arrow_forward', color='accent')
      q-breadcrumbs-el(label='Inicio', icon='home', :to="{ name: 'dashboard'}")
      q-breadcrumbs-el(label='Perfilamiento', icon='widgets')
      q-breadcrumbs-el(label='Lista')
    .bg-white
      q-toolbar
        q-toolbar-title PERFILAMIENTO
        router-link(:to="{ name: 'profilingAdd'}")
          q-btn.float-right(color='secondary')
            q-icon(left='', size='2em', name='add')
            div NUEVO PERFILAMIENTO
    .row
      q-card.my-card
        q-card-section.bg-primary.text-white
          .text-h6 Our Changing Plane
          .text-subtitle2 by John Doe
        q-separator
        q-markup-table
          thead
            tr
              th.text-left Dessert (100g serving)
              th.text-right Calories
              th.text-right Fat (g)
              th.text-right Carbs (g)
              th.text-right Protein (g)
              th.text-right Sodium (mg)
          tbody
            tr
              td.text-left Frozen Yogurt
              td.text-right 159
              td.text-right 6
              td.text-right 24
              td.text-right 4
              td.text-right 87
            tr
              td.text-left Ice cream sandwich
              td.text-right 237
              td.text-right 9
              td.text-right 37
              td.text-right 4.3
              td.text-right 129
</template>

<script>
import List from '@/components/List.vue'
export default {
  name: 'profilingList',
  components: {
    List
  },
  data () {
    return {
    }
  }
}
</script>
