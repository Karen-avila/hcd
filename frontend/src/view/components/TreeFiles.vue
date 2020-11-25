<template lang="pug">
  q-tree.bg-grey-2.q-pa-md(
    :nodes="files"
    node-key='label'
    tick-strategy='leaf'
    :ticked.sync="ticked"
    default-expand-all
    @lazy-load='onLazyLoad'
  )
    template(v-slot:header-generic='prop')
      q-icon(:name='prop.node.icon' :color='prop.node.iconColor')
      span {{ prop.node.name }}
</template>

<script>
export default {
  name: 'TreeFiles',
  props: [
    'path',
    'selected'
  ],
  data () {
    return {
      files: [],
      ticked: this.selected
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
    getDirectory (dirPath) {
      return this.$apollo
        .mutate({
          mutation: this.$gql`mutation{
              qudaFileGetDirectory(path:"${dirPath}")
            }`
        }).then(({ data }) => {
          return JSON.parse(data.qudaFileGetDirectory).directory.map(node => {
            node.name = node.label
            node.label = dirPath + node.label
            node.header = 'generic'
            node.lazy = (node.type === 'directory')
            node.path = dirPath
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
    ticked (value) {
      this.$emit('update:selected', value)
    }
  }
}
</script>
