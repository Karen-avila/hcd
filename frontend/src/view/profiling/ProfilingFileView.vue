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
       <div class="text-h6">Variables</div>
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
          <!-- TABS -->
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
      </q-card-section>
      <q-card-section class="q-pt-none">
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
                <div class="text-h6">Grafica</div>
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
      </q-card-section>
        <q-card-section class="q-pt-none">
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
      </q-card-section>
        <q-card-section class="q-pt-none">
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
                <div class="text-h6">doble tab</div>
              </q-tab-panel>
              <q-tab-panel name="longitud">
                <div class="text-h6">Grafica</div>
              </q-tab-panel>
               <q-tab-panel name="unicode">
                <div class="text-h6">doble tab</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </q-card-section>
       <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Nombre</h6>
            <p>Categórico</p>
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
        </div>
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="frecuencias2" label="Frecuencias" />
              <q-tab name="longitud2" label="Longitud" />
              <q-tab name="unicode2" label="Unicode" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="frecuencias2">
                <div class="text-h6">Mails</div>
              </q-tab-panel>
              <q-tab-panel name="longitud2">
                <div class="text-h6">Alarms</div>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
              </q-tab-panel>
               <q-tab-panel name="unicode2">
                <div class="text-h6">Alarms</div>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </q-card-section>
        <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Sexo</h6>
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
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas" label="Estadisticas" />
              <q-tab name="histograma" label="Histograma" />
              <q-tab name="valorescomunes3" label="Valores comunes" />
              <q-tab name="valoresextremos3" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas">
                <div class="text-h6">Mails</div>
              </q-tab-panel>
              <q-tab-panel name="histograma">
                <div class="text-h6">Alarms</div>
              </q-tab-panel>
              <q-tab-panel name="valorescomunes3">
                <div class="text-h6">Alarms</div>
              </q-tab-panel>
              <q-tab-panel name="valoresextremos3">
                <div class="text-h6">Alarms</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
            <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Edad</h6>
            <p>Número real (R ≥ 0)</p>
            <p>MISSING</p>
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
          <!-- TABS -->
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
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas4" label="Estadisticas" />
              <q-tab name="histograma4" label="Histograma" />
              <q-tab name="valorescomunes4" label="Valores comunes" />
              <q-tab name="valoresextremos4" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas4">
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
              <q-tab-panel name="histograma4">
                <div class="text-h6">Grafica</div>
              </q-tab-panel>
              <q-tab-panel name="valorescomunes4">
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
              <q-tab-panel name="valoresextremos4">
                <div class="text-h6">doble tab</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
            <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Número real de SibSp</h6>
            <p>(R ≥ 0)</p>
            <p>ZEROS</p>
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
          <!-- TABS -->
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
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas5" label="Estadisticas" />
              <q-tab name="histograma5" label="Histograma" />
              <q-tab name="valorescomunes5" label="Valores comunes" />
              <q-tab name="valoresextremos5" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas5">
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
              <q-tab-panel name="histograma5">
               <div class="text-h6">Grafica</div>
              </q-tab-panel>
              <q-tab-panel name="valorescomunes5">
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
              <q-tab-panel name="valoresextremos5">
                <div class="text-h6">doble tab</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
        <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Parch</h6>
            <p>Número real (R ≥ 0)</p>
            <span>ZEROS</span>
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
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas6" label="Estadisticas" />
              <q-tab name="histograma6" label="Histograma" />
              <q-tab name="valores_comunes6" label="Valores comunes" />
              <q-tab name="valores_extremos6" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas6">
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
              <q-tab-panel name="histograma6">
                <div class="text-h6">grafica</div>
              </q-tab-panel>
              <q-tab-panel name="valores_comunes6">
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
               <q-tab-panel name="valores_extremos6">
                <div class="text-h6">doble tab</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
           <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Ticket</h6>
            <p>Categórico</p>
            <p> HIGH CARDINALITY UNIFORM</p>
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
                <div class="col"></div>
              </tbody>
            </q-markup-table>
          </div>
        </div>
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="frecuencia7" label="Frecuencias" />
              <q-tab name="longitud7" label="Longitud" />
              <q-tab name="unicode" label="Unicode" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="frecuencia7">
              </q-tab-panel>
              <q-tab-panel name="longitud7">
                <div class="text-h6">Grafica</div>
              </q-tab-panel>
              <q-tab-panel name="unicode7">
                <div class="text-h6">doble tabl</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
          <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Tarifa</h6>
            <p>Número real (R ≥ 0)</p>
            <p>ZEROS</p>
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
      </q-card-section>
        <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="estadisticas8" label="Estadísticas" />
              <q-tab name="histograma8" label="Histograma" />
              <q-tab name="valorescomunes8" label="Valores comunes" />
              <q-tab name="valoresextremos8" label="Valores extremos" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="estadisticas8">
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
              <q-tab-panel name="histograma8">
                <div class="text-h6">grafica</div>
              </q-tab-panel>
              <q-tab-panel name="valorescomunes8">
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
              <q-tab-panel name="valoresextremos8">
                <div class="text-h6">Alarms</div>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
        </q-card-section>
         <q-card-section>
        <div class="row">
          <div class="col">
            <h6>Cabina</h6>
            <p>Categórica</p>
            <p>HIGH CARDINALITY MISSING UNIFORM</p>
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
      </q-card-section>
      <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col">
            <q-tabs v-model="tab" dense class="text-grey" active-color="primary" indicator-color="primary" align="justify" narrow-indicator>
              <q-tab name="frecuencia0" label="Frecuencias" />
              <q-tab name="longitud0" label="Longitud" />
              <q-tab name="unicode0" label="Unicode" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="frecuencia0">
              </q-tab-panel>
              <q-tab-panel name="longitud0">
                <div class="text-h6">Grafica</div>
              </q-tab-panel>
              <q-tab-panel name="unicode0">
                <div class="text-h6">doble tabl</div>
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </q-card-section>
        <q-card-section>
        <div class="row">
          <div class="col">
            <p>Categórico</p>
            <h6>embarcado</h6>
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
              <q-tab name="frecuencia11" label="Frecuencias" />
              <q-tab name="longitud11" label="Longitud" />
              <q-tab name="unicode11" label="Unicode" />
            </q-tabs>
            <q-separator />
            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="frecuencia11">
              </q-tab-panel>
              <q-tab-panel name="longitud11">
                <div class="text-h6">Grafica</div>
              </q-tab-panel>
              <q-tab-panel name="unicode11">
                <div class="text-h6">doble tabl</div>
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
