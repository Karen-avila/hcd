<template lang="pug">
.q-pa-md
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
      label='Archivo de Perfilamiento'
      icon='widgets'
      :to='{ name: "profilingList"}'
    )
    q-breadcrumbs-el.text-weight-medium
  // ARCHIVO
  template(
    v-if='variables'
    v-for='(item, key) in variables'
  )
    BooleanCard(
      v-if='item.type === "Variable.TYPE_BOOL"'
      :cardData='item'
      :cardName='key'
    )
    template(
    v-if='variables'
    v-for='(item, key) in variables'
  )
    RealNumberCard(
      v-if='item.type === "Variable.TYPE_NUM"'
      :cardData='item'
      :cardName='key'
    )
    template(
    v-if='variables'
    v-for='(item, key) in variables'
  )
    CategoricalCard(
      v-if='item.type === "Variable.TYPE_CAT"'
      :cardData='item'
      :cardName='key'
    )
    template(
    v-if='variables'
    v-for='(item, key) in variables'
  )
    DateCard(
      v-if='item.type === "Variable.DATE"'
      :cardData='item'
      :cardName='key'
    )
     template(
    v-if='variables'
    v-for='(item, key) in variables'
  )
    DateCard(
      v-if='item.type === "Variable.Url"'
      :cardData='item'
      :cardName='key'
    )
</template>

<script src='./ProfilingFileView.js'></script>
