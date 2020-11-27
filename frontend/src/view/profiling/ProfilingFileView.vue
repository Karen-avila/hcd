<template lang='pug'>

<div class="q-pa-md">
  <!-- BREADCRUMBS-->
  <q-breadcrumbs class="text-primary" active-color="primary">
    <template v-slot:separator="">
      <q-icon size="1.2em" name="arrow_forward" color="accent"></q-icon>
    </template>
    <q-breadcrumbs-el label="Inicio" icon="home" :to="{ name: &quot;dashboard&quot;}"></q-breadcrumbs-el>
    <q-breadcrumbs-el label="Archicho de Perfilamiento" icon="widgets" :to="{ name: &quot;profilingList&quot;}"></q-breadcrumbs-el>
    <q-breadcrumbs-el class="text-weight-medium"></q-breadcrumbs-el>
  </q-breadcrumbs>
  <!-- ARCHIVO -->
  <template v-if="profilingFile">
    <q-card class="q-my-md shadow-12">
      <!-- TÍTULO -->
      <q-card-section>
        <div class="text-h6">Variables</div>
        <div class="text-subtitle2">Que significa esto?</div>
      </q-card-section>
      <!-- ARCHIVO -->
      <q-card-section class="q-pt-none">
        <div class="row q-gutter-lg">
          <div class="col">
            <h6>PassengerId</h6><span>PassengerId</span>
          </div>
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <!-- TABS -->
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Frozen Yogurt</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <div class="col"></div>
        </div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
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
          </div>
        </div>
      </q-card-section>
    </q-card>
  </template>
</div>
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
