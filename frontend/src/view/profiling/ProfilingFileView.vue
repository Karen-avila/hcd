<template lang='pug'>
<div class="q-pa-md">
  <q-breadcrumbs class="text-primary" active-color="primary">
    <template v-slot:separator="">
      <q-icon size="1.2em" name="arrow_forward" color="accent"></q-icon>
    </template>
    <q-breadcrumbs-el label="Inicio" icon="home" :to="{ name: &quot;dashboard&quot;}"></q-breadcrumbs-el>
    <q-breadcrumbs-el label="Archivo de Perfilamiento" icon="widgets" :to="{ name: &quot;profilingList&quot;}"></q-breadcrumbs-el>
    <q-breadcrumbs-el class="text-weight-medium"></q-breadcrumbs-el>
  </q-breadcrumbs>
  <template v-if="profilingFile">
    <q-card class="q-my-md shadow-12">
      <q-card-section>
       <div class="text-h5">Variables</div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        <div class="row q-gutter-lg">
          <div class="col">
            <h6>PassengerId</h6>
            <p> Número real (R ≥ 0)</p>
            <p>UNIQUE</p>
          </div>
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Distinto</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Distinto (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desaparecido (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desaparecido</td>
                  <td class="text-right">159</td>
                </tr>
                  <tr>
                  <td class="text-left">Infinito</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Infinito (%)</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Media</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Mínimo</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Máximo</td>
                  <td class="text-right">159</td>
                </tr>
                  <tr>
                  <td class="text-left">Ceros</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Ceros (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Tamaño de la memoria</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <div class="col"></div>
        </div>
         <div align="right"><q-btn color="white" text-color="black" v-on:click="show = !show" label="Alternar detalles" /></div>
      </q-card-section>
      <q-card-section class="q-pt-none" v-if="show">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas" label="Estadísticas" />
              <q-tab name="histograma" label="Histograma" />
              <q-tab name="valores_comunes" label="Valores comunes" />
              <q-tab name="valores_extremos" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas">
              <div class="row q-gutter-lg">
              <div class="col">
              <h6>Estadísticas cuantiles</h6>
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Minimo</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Percentil 5</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Q1</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Mediana</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Tercer trimestre</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Percentil 95</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Máximo</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Rango</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Rango intercuartil (IQR)</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
              </div>
              <div class="col">
              <h6>Estadísticas descriptivas</h6>
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Desviación Estándar</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Coeficiente de variacíon (CV)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Curtosis</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Media</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desviacion absoluta media (MAD)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Oblicuidad</td>
                  <td class="text-right">159</td>
                </tr>
                 <tr>
                  <td class="text-left">Suma</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Diferencia</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Monotocidad</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
              </div>
              </div>
              </q-tab-panel>
              <q-tab-panel name="histograma">
                <div class="text-h6">Gráfica</div>
              </q-tab-panel>
              <q-tab-panel name="valores_comunes">
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
              <td class="text-right">1</td>
              <td class="text-right">0.1%</td>
            </tr>
            </tbody>
            </q-markup-table>
              </div>
              </q-tab-panel>
               <q-tab-panel name="valores_extremos">
                <q-card-section class="q-pt-none">
                  <div class="row">
                    <div class="col">
                        <q-tabs v-model="tab1" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
                          <q-tab name="minimo_valores" label="Minimo 5 valores" />
                          <q-tab name="maximo_valores" label="Maximo 5 valores" />
                        </q-tabs>
                        <q-separator />
                        <q-tab-panels v-model="tab1" animated>
                          <q-tab-panel name="minimo_valores">
                          <p>holi</p>
                          </q-tab-panel>
                          <q-tab-panel name="maximo_valores">
                          <p>equis</p>
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
        <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Booleano</h6>
            <p>Sobrevivido</p>
          </div>
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Distinto</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Distinto (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desaparecido</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desaparecido (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Tamaño de la memoria</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <div class="col"></div>
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
              <td class="text-right">1</td>
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
       <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Pclass</h6>
            <p>Categórico</p>
          </div>
          <div class="col">
            <q-markup-table flat="flat">
              <tbody>
                <tr>
                  <td class="text-left">Distinto</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Distinto (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Desaparecido</td>
                  <td class="text-right">159</td>
                </tr>
                 <tr>
                  <td class="text-left">Desaparecido (%)</td>
                  <td class="text-right">159</td>
                </tr>
                <tr>
                  <td class="text-left">Tamaño de la memoria</td>
                  <td class="text-right">159</td>
                </tr>
              </tbody>
            </q-markup-table>
          </div>
          <div class="col"></div>
        </div>
        <div align="right"><q-btn color="white" text-color="black" v-on:click="show = !show" label="Alternar detalles" /></div>
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
                          </q-tab-panel>
                          <q-tab-panel name="grafico">
                          <p></p>
                          </q-tab-panel>
                        </q-tab-panels>
                    </div>
                  </div>
                </q-card-section>
              </q-tab-panel>
              <q-tab-panel name="longitud">
                <div class="text-h6">Grafica</div>
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
      tab: 'mails',
      tab1: 'mails',
      show: false
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
