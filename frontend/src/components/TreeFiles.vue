<template lang="pug">
  div
    q-tree(
      :nodes="files"
      node-key='label'
      tick-strategy='leaf'
      :ticked.sync="ticked"
      default-expand-all
      @lazy-load='onLazyLoad'
    )
      template(v-slot:header-generic='prop')
        .row.items-center.q-py-xs
          q-icon.q-mr-sm(:name='prop.node.icon' color='secondary')
          span {{ prop.node.name }}
</template>

<script>
import gql from 'graphql-tag'
export default {
  name: 'TreeFiles',
  props: [
    'selectedFiles'
  ],
  data () {
    return {
      files: [],
      path: '/app/temp/',
      ticked: []
    }
  },
  mounted () {
    this.getDirectory(this.path).then(data => {
      this.files = data
    })
  },
  methods: {
    onLazyLoad ({ node, key, done, fail }) {
      this.getDirectory(node.label + '/').then(data => {
        done(data)
      })
    },
    getDirectory (path) {
      return this.$apollo
        .mutate({
          mutation: gql`
            mutation{
              qudaFileGetDirectory(path:"/app/temp")
            }
          `
        }).then(({ data }) => {
          return JSON.parse(data.qudagetdirectory.directory.getStructure).directory.map(node => {
            node.name = node.label
            node.label = path + node.label
            node.header = 'generic'
            node.lazy = (node.type === 'directory')
            node.path = path
            node.icon = (node.type === 'directory') ? 'folder' : 'insert_drive_file'
            node.noTick = (node.type === 'directory')
            node.iconColor = 'secondary'
            return node
          })
        }).catch((error) => {
          console.error('TreeFiles: ', error)
        })
    }
  },
  watch: {
    ticked (newValue) {
      this.$emit('update:selectedFiles', newValue)
      this.$emit('update:selectedFilesNames', newValue)
    }
  }
}
</script>
