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
        label='Archicho de Perfilamiento'
        icon='widgets'
        :to='{ name: "profilingList"}'
      )
      q-breadcrumbs-el.text-weight-medium(
      )
    template(
      v-if='profilingFile'
    )
      q-card.q-my-md.shadow-12
        q-card-section
          .text-h6 Variables
          .text-subtitle2 Que significa esto?
        q-card-section.q-pt-none
          .row.q-gutter-lg
            .col
              h6 PassengerId
              span PassengerId
            .col
              q-markup-table(
                bordered=false
                flat
              )
                tbody
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
            .col
              q-markup-table(
                bordered=false
                flat
              )
                tbody
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
                  tr
                    td.text-left Frozen Yogurt
                    td.text-right 159
            .col
        q-card-section.q-pt-none
          .row
            .col
              <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
                <q-tab name="mails" label="Mails" />
                <q-tab name="alarms" label="Alarms" />
                <q-tab name="movies" label="Movies" />
              </q-tabs>
              <q-separator />
              <q-tab-panels v-model="tab" animated>
                <q-tab-panel name="mails">
                  <div class="text-h6">Mails</div>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                </q-tab-panel>
                <q-tab-panel name="alarms">
                  <div class="text-h6">Alarms</div>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                </q-tab-panel>
                <q-tab-panel name="movies">
                  <div class="text-h6">Movies</div>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                </q-tab-panel>
              </q-tab-panels>
</template>

<script>
export default {
  name: 'ProfilingFileView',
  data () {
    return {
      profilingFile: null,
      tab: 'mails'
    }
  },
  mounted () {
    this.getProfilingFile()
  },
  methods: {
    getProfilingFile () {
      this.$apollo
        .mutate({
          mutation: this.$gql`
            mutation {
              prflProfilingFile(id: "${this.$route.params.Id}") {
                id
                filename
                sep
                encoding
                haveHeaders
                analysis
                variables
                scatter
              }
            }
          `
        }).then(({ data }) => {
          this.profilingFile = data.prflProfilingFile
          console.log(JSON.parse(this.profilingFile.variables))
        })
    }
  }
}
</script>
