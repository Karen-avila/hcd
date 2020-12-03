import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters([
      'errors',
      'isAuthenticated',
      'authenting'
    ])
  },
  data () {
    return {
      form: {
        username: `${process.env.DEBUG ? 'admin' : ''}`,
        password: `${process.env.DEBUG ? 'admin' : ''}`,
        remember: true
      },
      isPwd: 'password'
    }
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) return 1
      return 0
    },
    login () {
      if (!this.validate()) return 0
      this.$store.dispatch('logout')
      const username = process.env.ORGANIZATION + '__' + this.form.username
      const password = this.form.password
      this.$store.dispatch('login', { username, password })
        .then(() => {
          if (this.isAuthenticated) this.$router.push({ name: 'dashboard' })
        })
    }
  }
}
