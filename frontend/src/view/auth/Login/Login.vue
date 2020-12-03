<template lang='pug'>
q-layout
  q-page-container.bg-login
    q-page.bg-image.flex.flex-center
      q-card.q-card-bordered.shadow-12.q-py-lg(
        v-bind:style='$q.screen.lt.sm ? {"width": "80%"} : {"width":"30%"}'
      )
        //  q-card-section
              q-avatar.absolute-center(size='103px')
                img(src='~assets/img/auth/user.png')
        q-card-section
          .text-center.q-pt-lg
            .col.text-h6.ellipsis(
            ) CALIDAD DE DATOS
        q-card-section
          template(
            v-if='errors.length >= 1'
            role='alert'
            v-bind:class='{ show: errors.length }'
          )
            span.text-negative(
              v-for='(error, i) in errors' :key='i'
            ) {{ error }}
          q-form.q-gutter-sm(
            ref='form'
            lazy-validation
            @submit.stop.prevent='login'
          )
            q-input(
              v-model='form.username'
              label='Tu usuario o correo electrónico'
              outlined=''
              lazy-rules=''
              color='primary'
              :rules='[() => !!form.username || "Ingresa un nombre"]'
            )
            q-input(
              v-model='form.password'
              label='Tu contraseña'
              outlined=''
              lazy-rules=''
              color='primary'
              :type="isPwd ? 'password' : 'text'"
              :rules='[ () => !!form.password || "Ingresa una contraseña"]'
            )
              template(
                v-slot:append=''
              )
                q-icon.cursor-pointer(
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  @click='isPwd = !isPwd'
                )
            q-item
              q-checkbox.full-width(
                v-model='form.remember'
                dense=''
                outlined=''
                label='Recuerdame'
              )
            .row
              .col-12.text-right
                q-btn.text-capitalize(
                  type='submit'
                  color='accent'
                  outline=''
                  style='min-width: 170px'
                  :loading='authenting'
                ) Acceder
                  template(
                    v-slot:loading=''
                  )
                    q-spinner.on-left(
                    ) Verificando...
</template>

<style lang="sass" src='./Login.sass' scoped></style>
<script src='./Login.js'></script>
