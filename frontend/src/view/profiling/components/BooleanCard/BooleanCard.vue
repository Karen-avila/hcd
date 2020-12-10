<template lang="pug">
q-card.q-my-lg.q-py-md(
    flat
    bordered
)
    <q-card-section>
        <div class="row">
        <div class="col">
            <p>Booleano</p>
            <p class="text-h6 text-weight-bold text-primary">{{cardName}}</p>
        </div>
        <div class="col">
            <q-markup-table flat="flat">
            <tbody>
                <tr>
                    <td class="text-left text-weight-bold">Número de distintos</td>
                    <td class="text-right">{{data.n_distinct}}</td>
                </tr>
                <tr>
                    <td class="text-left text-weight-bold">Porcentaje Distinto (%)</td>
                    <td class="text-right">{{(data.p_distinct * 100).toFixed(2)}} %</td>
                </tr>
                <tr>
                    <td class="text-left text-weight-bold">Datos Faltantes/Vacíos</td>
                    <td class="text-right">{{data.n_missing}}</td>
                </tr>
                <tr>
                    <td class="text-left text-weight-bold">Porcentaje datos Faltantes/Vacíos (%)</td>
                    <td class="text-right">{{(data.p_missing * 100).toFixed(2)}} %</td>
                </tr>
                <tr>
                    <td class="text-left text-weight-bold">Tamaño de la memoria</td>
                    <td class="text-right">{{(data.memory_size / 1000).toFixed(2)}} KiB</td>
                </tr>
            </tbody>
            </q-markup-table>
        </div>
        <div class="col">
        apexchart(type='bar', :options='chartOptions2', :series='series2')
        </div>
        </div>
        <div align="right"><q-btn color="white" text-color="black" v-on:click="show = !show" label="Alternar detalles" /></div>
    </q-card-section>
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
            apexchart(type='pie', :options='chartOptions', :series='series')
            </q-tab-panel>
            </q-tab-panels>
        </div>
        </div>
    </q-card-section>
</template>

<script src='./BooleanCard.js'></script>a
