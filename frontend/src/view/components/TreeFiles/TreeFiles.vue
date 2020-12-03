<template lang="pug">
  q-tree.bg-grey-2.q-pa-md(
    node-key='label'
    tick-strategy='leaf'
    default-expand-all
    :ticked.sync="ticked"
    :nodes="files"
    @lazy-load='onLazyLoad'
  )
    template(
      v-slot:header-generic='prop'
    )
      q-icon(
        :name='prop.node.icon'
        :color='prop.node.iconColor'
      )
      span(
      ) {{ prop.node.name }}
</template>

<script src='./TreeFiles.js'></script>
