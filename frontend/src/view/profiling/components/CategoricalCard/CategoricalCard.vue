<template lang="pug">
  q-card.q-my-lg.q-py-md(
    flat
    bordered
  )
    <q-card-section>
        <div class="row">
          <div class="col">
            <h6 class="text-h6 text-weight-bold text-primary">{{cardName}}</h6>
            <p>Categórico</p>
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
          apexchart(type='bar', :options='chartOptions4', :series='series4')
          </div>
        </div>
        <div align="right"><q-btn color="white" text-color="black" v-on:click="show = !show" label="Alternarr detalles" /></div>
        </q-card-section>
        <q-card-section class="q-pt-none" v-if="show">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="frecuencias" label="Frecuencias" />
              <q-tab name="longitud" label="Longitud" />
              <q-tab name="unicode" label="Unicode" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="frecuencias">
                <q-card-section class="q-pt-none">
                  <div class="row">
                    <div class="col">
                        <q-tabs v-model="tab1" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
                          <q-tab name="valores_comunes" label="Valores comunes" />
                          <q-tab name="vision_general" label="Visión General" />
                          <q-tab name="grafico" label="Gráfico" />
                        </q-tabs>
                        <q-separator />
                        <q-tab-panels v-model="tab1" animated>
                          <q-tab-panel name="valores_comunes">
                          <p></p>
                          </q-tab-panel>
                          <q-tab-panel name="vision_general">
                          <div class="row q-gutter-lg">
                          <div clas="col">
                          apexchart(type='bar', :options='chartOptions', :series='series')
                          </div>
                          <div class="col">
                           <q-markup-table flat="flat">
                           <tbody>
                            <p>Único</p>
                            <tr>
                              <td class="text-left">Único</td>
                              <td class="text-right">{{data.n_unique}}</td>
                            </tr>
                            <tr>
                              <td class="text-left">Único (%)</td>
                              <td class="text-right">{{(data.p_unique * 100).toFixed(1)}}%</td>
                            </tr>
                            </tbody>
                          </q-markup-table>
                            </div>
                          </div>
                          </q-tab-panel>
                          <q-tab-panel name="grafico">
                           apexchart(type='pie' width="380" :options='chartOptions3', :series='series3')
                          </q-tab-panel>
                        </q-tab-panels>
                    </div>
                  </div>
                </q-card-section>
              </q-tab-panel>
              <q-tab-panel name="longitud">
              <div class="row q-gutter-lg">
              <div class="col">
              apexchart(type='bar', :options='chartOptions2', :series='series2')
              </div>
              <div class="col">
              <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Longitud</td>
                </tr>
                <tr>
                  <td class="text-left">Longitud máxima</td>
                  <td class="text-right">{{data.max_length}}</td>
                </tr>
                <tr>
                  <td class="text-left">Longitud mediana</td>
                  <td class="text-right">{{data.median_length}}</td>
                </tr>
                <tr>
                  <td class="text-left">Longitud media</td>
                  <td class="text-right">{{data.mean_length}}</td>
                </tr>
                  <tr>
                  <td class="text-left">Longitud mínima</td>
                  <td class="text-right">{{data.min_length}}</td>
                </tr>
              </tbody>
              </q-markup-table>
              </div>
              </div>
              </q-tab-panel>
               <q-tab-panel name="unicode">
                  <q-card-section class="q-pt-none">
                  <div class="row">
                    <div class="col">
                        <q-tabs v-model="tab1" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
                          <q-tab name="vision_general" label="Visión general" />
                          <q-tab name="caracteres" label="Caracteres" />
                          <q-tab name="categorias" label="Categorías" />
                          <q-tab name="guiones" label="Guiones" />
                          <q-tab name="bloques" label="Bloques" />
                        </q-tabs>
                        <q-separator />
                        <q-tab-panels v-model="tab1" animated>
                          <q-tab-panel name="vision_general">
                            <h6>Descripción general de las propiedades de Unicode</h6>
                              <q-markup-table flat="flat">
                                <tbody>
                                    <tr>
                                      <td class="text-left">Caracteres unicode únicos</td>
                                      <td class="text-right">159</td>
                                    </tr>
                                    <tr>
                                      <td class="text-left">Categorías unicode únicas</td>
                                      <td class="text-right">159</td>
                                    </tr>
                                      <tr>
                                      <td class="text-left">Scripts unicode únicos</td>
                                      <td class="text-right">159</td>
                                    </tr>
                                    <tr>
                                      <td class="text-left">Bloques unicode únicos</td>
                                      <td class="text-right">159</td>
                                    </tr>
                                </tbody>
                              </q-markup-table>
                          </q-tab-panel>
                          <q-tab-panel name="caracteres">
                            <div class="q-pa-md">
                            <h6>Personajes más frecuentes</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                            </div>
                          </q-tab-panel>
                          <q-tab-panel name="categorias">
                            <div class="q-pa-md">
                            <h6>Categorías más frecuentes</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                             <h6>Caracteres de números decimales más frecuentes</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                            </div>
                          </q-tab-panel>
                          <q-tab-panel name="guiones">
                           <div class="q-pa-md">
                            <h6>La mayoría de los scripts que ocurren</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                             <h6>Caracteres comunes más frecuentes</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                            </div>
                          </q-tab-panel>
                          <q-tab-panel name="bloques">
                           <div class="q-pa-md">
                            <h6>La mayoría de los bloques que ocurren</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                             <h6>Caracteres ASCII más frecuentes</h6>
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
                                  <td class="text-left">891</td>
                                  <td class="text-right">1</td>
                                  <td class="text-right">0.1%</td>
                                </tr>
                              </tbody>
                            </q-markup-table>
                            </div>
                          </q-tab-panel>
                        </q-tab-panels>
                    </div>
                  </div>
                  </q-card-section>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
    </q-card-section>
</template>

<script src='./CategoricalCard.js'></script>
