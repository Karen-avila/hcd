<template lang="pug">
q-layout
  q-page-container
    q-page.bg-image.flex.flex-center
      q-card.q-card-bordered.shadow-12(v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}")
        q-card-section
          q-avatar.absolute-center(size='103px')
            img(src='~assets/img/auth/user.png')
        q-card-section
          .text-center.q-pt-lg
            .col.text-h6.ellipsis
              | HERRAMIENTA CALIDAD DE DATOS
        q-card-section
          template(role='alert', v-if="errors.length >= 1" v-bind:class='{ show: errors.length }')
            span.text-negative(v-for='(error, i) in errors', :key='i')
              | {{ error }}
          q-form.q-gutter-sm(
            ref='form'
            lazy-validation
            @submit.stop.prevent='onSubmit'
          )
            q-input(
              outlined=''
              v-model='form.username'
              label='Tu usuario o correo electrónico'
              lazy-rules=''
              color='primary'
              :rules="[() => !!form.username || 'Ingresa un nombre']"
            )
            q-input(
              outlined=''
              v-model='form.password'
              :type="isPwd ? 'password' : 'text'"
              label='Tu contraseña'
              lazy-rules=''
              color='primary'
              :rules="[() => !!form.password || 'Ingresa una contraseña']"
            )
              template(v-slot:append='')
                q-icon.cursor-pointer(:name="isPwd ? 'visibility_off' : 'visibility'", @click='isPwd = !isPwd')
            q-item
              q-checkbox.full-width(dense='', outlined='', v-model='form.remember', label='Recuerdame')
            .row
              .col-12.text-right
                q-btn.text-capitalize(
                  :loading='authenting'
                  type='submit'
                  color='accent'
                  outline=''
                  style='min-width: 170px'
                )
                  | Acceder
                  template(v-slot:loading='')
                    q-spinner.on-left
                    | Verificando...
</template>

<script>
import { mapGetters } from 'vuex'
export default {
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
  computed: {
    ...mapGetters([
      'errors',
      'isAuthenticated',
      'authenting'
    ])
  },
  created () {},
  methods: {
    validate () {
      if (this.$refs.form.validate()) return 1
      return 0
    },
    onSubmit () {
      if (this.validate()) {
        const username = process.env.ORGANIZATION + '__' + this.form.username
        const password = this.form.password
        this.$store.dispatch('logout')
        this.$store.dispatch('login', { username, password })
          .then(() => {
            if (this.isAuthenticated) this.$router.push({ name: 'dashboard' })
          })
      }
    }
  }
}
</script>

<style lang="sass">
  .bg-image
    background-image: url(~assets/img/auth/gradient.png)
    background-position: left bottom
    background-size: cover
</style>
