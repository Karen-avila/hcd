<template lang="pug">
  q-card.q-my-lg.q-py-md(
    flat
    bordered
  )
    // ARCHIVO
    q-card-section.q-pt-none
      .row.q-col-gutter-lg
        .col-2
          p Booleano
          .text-h6.text-weight-bold.text-primary {{cardName}}
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
    <q-card-section class="q-pt-none" v-if="show">
        <div class="row">
        <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
            <q-tab name="valor_comunes2" label="Valores Comunes" />
            <q-tab name="grafico" label="Gráfico" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="valor_comunes2">
            <div class="q-pa-md">
            <q-markup-table>
            <thead>
            <tr>
                <th class="text-left">Valor</th>
                <th class="text-right">Contador</th>
                <th class="text-right">Frecuencia (%)</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td class="text-left">891</td>
                <td class="text-right"></td>
                <td class="text-right">0.1%</td>
            </tr>
            </tbody>
            </q-markup-table>
            </div>
            </q-tab-panel>
            <q-tab-panel name="grafico">
            <div class="text-h6">Gráfico</div>
            </q-tab-panel>
            </q-tab-panels>
        </div>
        </div>
    </q-card-section>
</template>

<script src='./DateCard.js'></script>
