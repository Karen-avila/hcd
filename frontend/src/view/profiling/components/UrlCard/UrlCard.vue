<template lang="pug">
  q-card.q-my-lg.q-py-md(
    flat
    bordered
  )
    <q-card-section>
    <div class="row">
        <div class="col">
            <h6>URL</h6>
            <p>loc</p>
        </div>
        <div class="col">
            <q-markup-table flat="flat">
            <tbody>
            <tr>
                <td class="text-left">Distinto</td>
                <td class="text-right">{{data.n_distinct}} </td>
            </tr>
            <tr>
                <td class="text-left">Distinto (%)</td>
                <td class="text-right">{{(data.p_distinct * 100).toFixed(2)}} %</td>
            </tr>
            <tr>
                <td class="text-left">Desaparecido</td>
                <td class="text-right">{{data.n_missing}}</td>
            </tr>
            <tr>
                <td class="text-left">Desaparecido (%)</td>
                <td class="text-right">{{(data.p_missing * 100).toFixed(2)}} %</td>
                </tr>
            <tr>
                <td class="text-left">Tamaño de la memoria</td>
                <td class="text-right">{{(data.p_infinite * 100).toFixed(2)}} %</td>
            </tr>
            </tbody>
            </q-markup-table>
        </div>
        <div class="col">
            <q-markup-table flat="flat">
            <tbody>
            <tr>
                <td class="text-left">url</td>
                <td class="text-right"></td>
            </tr>
            <tr>
                <td class="text-left">url</td>
                <td class="text-right"></td>
            </tr>
            </tbody>
            </q-markup-table>
        </div>
        <div class="col"></div>
    </div>
    <div align="right"><q-btn color="white" text-color="black" v-on:click="show = !show" label="Alternar detalles" /></div>
    </q-card-section>
    <q-card-section class="q-pt-none">
        <div class="row">
        <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
            <q-tab name="lleno" label="Lleno" />
            <q-tab name="esquema" label="Esquema" />
            <q-tab name="netloc" label="Netloc" />
            <q-tab name="camino" label="Camino" />
            <q-tab name="consulta" label="Consulta" />
            <q-tab name="fragmento" label="Fragmento" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="lleno">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            <q-tab-panel name="esquema">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            <q-tab-panel name="netloc">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            <q-tab-panel name="camino">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            <q-tab-panel name="consulta">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            <q-tab-panel name="fragmento">
                <q-markup-table>
                <thead>
                    <tr>
                        <th class="text-left">Valor</th>
                        <th class="text-right">Contar</th>
                        <th class="text-right">Frecuencia (%)</th>
                    </tr>
                </thead>
                    <tbody>
                    <tr>
                        <td class="text-left"></td>
                        <td class="text-right"></td>
                        <td class="text-right"></td>
                    </tr>
                    </tbody>
                </q-markup-table>
            </q-tab-panel>
            </q-tab-panels>
        </div>
        </div>
    </q-card-section>
</template>

<script src='./UrlCard.js'></script>
