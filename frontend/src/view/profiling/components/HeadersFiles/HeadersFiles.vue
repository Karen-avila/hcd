<template lang='pug'>
  div
    template(
      v-if='file.headers.length < 1 && file.data.length < 1 && !file.error'
    )
      q-toolbar.bg-grey.text-white.rounded-borders.q-mb-md.q-px-xl
        q-spinner.q-mr-md(
          color='white'
          size='1rem'
          :thickness='10'
        )
        span(
        ) Descargando: {{file.path.split('/').pop()}}
    template(
      v-if='file.headers.length > 1 && file.data.length > 1 && !file.error'
    )
      q-toolbar.bg-secondary.text-white.rounded-borders
        span(
        ) {{file.path.split('/').pop()}}
        q-space
        q-toggle.q-mr-md(
          v-model='file.haveHeaders'
          color='white'
          left-label
          :label='file.haveHeaders ? "Contiene encabezados" : "Sin encabezados"'
        )
        q-tabs(
          v-model='tab'
          shrink=''
          stretch=''
        )
          q-tab(
            name='table'
            label=''
            icon='table_view'
          )
            q-tooltip(
              content-class='bg-accent'
              anchor='top middle'
              self='bottom middle'
            ) Ver Tabla
          q-tab(
            name='type'
            label=''
            icon='spellcheck'
          )
            q-tooltip(
              content-class='bg-accent'
              anchor='top middle'
              self='bottom middle'
            ) Forzar datos
      q-card.card-file.bg-grey-2.q-mt-sm.q-mb-lg
        q-table.bg-grey-2(
          v-if='tab === "table"'
          dense=true
          bordered=false
          flat=true
          title=''
          row-key='name'
          separator='vertical'
          hide-bottom=true
          virtual-scroll
          :data='file.data'
          :columns='file.headers'
        )
        q-card-section(
          v-if='tab === "type" && dataTypes.length > 0'
        )
          p(
          ) Puedes elegir una opción para forzar el perfilamiento a ese tipo de dato
          .row
            .col-md-6.q-pa-xs(
              v-for='header in file.headers'
            )
              q-select(
                dense=true
                filled=''
                v-model='header.type'
                :options='dataTypes'
                :label='header.label'
              )
    template(
      v-if='file.error'
      align='center'
    )
      q-toolbar.bg-accent.text-white.rounded-borders
        span(
        ) {{file.path.split('/').pop()}}
        q-space
        span(
        ) {{file.error}}
      q-card.card-file.bg-grey-2.q-mt-xs.q-mb-lg
        .absolute-center
          q-form.q-gutter-md.row
            q-input(
              v-model='file.separator'
              clearable=''
              label='Separador'
              clear-icon='close'
              dense=true
            )
            q-input(
              v-model='file.codification'
              clearable=''
              label='Codificación'
              clear-icon='close'
              dense=true
            )
          .row.q-mt-md
            q-btn(
              label='Descargar de nuevo'
              type='button'
              color='primary'
              @click='updateTable'
            )
            q-btn.q-ml-lg(
              label=''
              icon='delete'
              type='button'
              color='negative'
              @click='deleteTable'
            )
</template>

<script src='./HeadersFiles.js'></script>
<style lang="sass" src='./HeadersFiles.sass' scoped></style>
