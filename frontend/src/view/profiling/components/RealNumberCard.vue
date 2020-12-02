<script src='./RealNumberCard.js'></script>

<template lang="pug">
  q-card.q-my-lg.q-py-md(
    flat
    bordered
  )
    // ARCHIVO
    q-card-section.q-pt-none
      .row.q-col-gutter-lg
        .col-2
          .text-h6.text-weight-bold.text-primary {{cardName}}
          p Número real (R ≥ 0)
          p.text-weight-bold.text-negative ÚNICO
        .col
          q-markup-table(
            flat='flat'
            dense
          )
            tbody
              tr
                td.text-left.text-weight-bold Número de distintos
                td.text-right {{data.n_distinct}}
              tr
                td.text-left.text-weight-bold Porcentaje de distintos (%)
                td.text-right {{(data.p_distinct * 100).toFixed(2)}} %
              tr
                td.text-left.text-weight-bold Datos Faltantes/Vacíos
                td.text-right {{data.n_missing}}
              tr
                td.text-left.text-weight-bold Porcentaje datos Faltantes/Vacíos (%)
                td.text-right {{(data.p_missing * 100).toFixed(2)}} %
              tr
                td.text-left.text-weight-bold Número de valores numéricos infinitos
                td.text-right {{data.n_infinite}}
              tr
                td.text-left.text-weight-bold Porcentaje Infinitos (%)
                td.text-right {{(data.p_infinite * 100).toFixed(2)}} %
        .col
          q-markup-table(
            flat='flat'
            dense
          )
            tbody
              tr
                td.text-left.text-weight-bold Media
                td.text-right {{data.mean}}
              tr
                td.text-left.text-weight-bold Mínimo
                td.text-right {{data.min}}
              tr
                td.text-left.text-weight-bold Máximo
                td.text-right {{data.max}}
              tr
                td.text-left.text-weight-bold Ceros
                td.text-right {{data.n_zeros}}
              tr
                td.text-left.text-weight-bold Ceros (%)
                td.text-right {{(data.p_zeros* 100).toFixed(2)}} %
              tr
                td.text-left.text-weight-bold Tamaño de la memoria
                td.text-right {{(data.memory_size / 1000).toFixed(2)}} KiB
        .col
          apexchart(type='bar', :options='chartOptions', :series='series')
      .row
        .col-12.text-right
          q-btn(
            color='white'
            text-color='black'
            @click='show = !show'
            label='Alternar detalles'
          )
      .row(v-show='show')
        .col
          q-tabs.text-grey(
            v-model='tab'
            dense=''
            active-color='primary'
            indicator-color='primary'
            align='justify'
            narrow-indicator=''
          )
            q-tab(
              name='estadisticas'
              label='Estadísticas'
            )
            q-tab(
              name='histograma'
              label='Histograma'
            )
            q-tab(
              name='valores_comunes'
              label='Valores comunes'
            )
            q-tab(
              name='valores_extremos'
              label='Valores extremos'
            )
          q-separator
          q-tab-panels(
            v-model='tab'
            animated=''
          )
            q-tab-panel(
              name='estadisticas'
            )
              .row.q-col-gutter-lg
                .col
                  .text-h6 Estadísticas cuantiles
                  q-markup-table(
                    flat='flat'
                    dense
                  )
                    tbody
                      tr
                        td.text-left.text-weight-bold Minimo
                        td.text-right {{data.min}}
                      tr
                        td.text-left.text-weight-bold 5%
                        td.text-right {{data['5%']}}
                      tr
                        td.text-left.text-weight-bold 25%
                        td.text-right {{data['25%']}}
                      tr
                        td.text-left.text-weight-bold 50% Mediana
                        td.text-right {{data['50%']}}
                      tr
                        td.text-left.text-weight-bold 75%
                        td.text-right {{data['50%']}}
                      tr
                        td.text-left.text-weight-bold 95%
                        td.text-right {{data['95%']}}
                      tr
                        td.text-left.text-weight-bold Máximo
                        td.text-right {{data.max}}
                      tr
                        td.text-left.text-weight-bold Rango
                        td.text-right {{data.range}}
                      tr
                        td.text-left.text-weight-bold Rango intercuartil (IQR)
                        td.text-right {{data.iqr}}
                .col
                  .text-h6 Estadísticas cuantiles
                  q-markup-table(
                    flat='flat'
                    dense
                  )
                    tbody
                      tr
                        td.text-left.text-weight-bold Desviación Estándar
                        td.text-right {{data.std.toFixed(6)}}
                      tr
                        td.text-left.text-weight-bold Coeficiente de variacíon (CV)
                        td.text-right {{data.cv.toFixed(10)}}
                      tr
                        td.text-left.text-weight-bold Curtosis
                        td.text-right {{data.kurtosis.toFixed(2)}}
                      tr
                        td.text-left.text-weight-bold Media
                        td.text-right {{data.mean}}
                      tr
                        td.text-left.text-weight-bold Desviacion absoluta media (MAD)
                        td.text-right {{data.mad}}
                      tr
                        td.text-left.text-weight-bold Oblicuidad
                        td.text-right {{data.skewness}}
                      tr
                        td.text-left.text-weight-bold Suma
                        td.text-right {{data.sum}}
                      tr
                        td.text-left.text-weight-bold Varianza
                        td.text-right {{data.variance}}
                      tr
                        td.text-left.text-weight-bold Monotocidad
                        td.text-right {{data.monotonic_increase_strict ? 'Estrictamente incremental' : 'No es'}}
            q-tab-panel(
              name='histograma'
            )
              apexchart(type='bar', :options='chartOptions', :series='series')
            q-tab-panel(
              name='valores_comunes'
            )
              .q-pa-md
                q-markup-table
                  thead
                    tr
                      th.text-left Valor
                      th.text-right Contador
                      th.text-right Frecuencia (%)
                  tbody
                    tr
                      td.text-left 891
                      td.text-right 1
                      td.text-right 0.1%
            q-tab-panel(
              name='valores_extremos'
            )
              q-card-section
                .row
                  .col
                    q-tabs.text-grey(
                      v-model='tab1'
                      dense=''
                      active-color='primary'
                      indicator-color='primary'
                      align='justify'
                      narrow-indicator=''
                    )
                      q-tab(
                        name='minimo_valores'
                        label='Minimo 5 valores'
                      )
                      q-tab(
                        name='maximo_valores'
                        label='Maximo 5 valores'
                      )
                      q-separator
                        q-tab-panels(
                          v-model='tab1'
                          animated=''
                        )
                          q-tab-panel(
                            name='minimo_valores'
                          )
                            p holi
                          q-tab-panel(
                            name='maximo_valores'
                          )
                            p equis
</template>
